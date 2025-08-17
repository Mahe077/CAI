# train_lstm.py
import os
import json
import time
from datetime import datetime, timezone
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

import ccxt
import pandas_ta as ta
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_auc_score, confusion_matrix
from sklearn.utils import class_weight

from joblib import dump

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# -----------------------------
# Config
# -----------------------------
SYMBOL              = "BTC/USDT"
TIMEFRAME           = "1h"
LIMIT               = 5000

# --- Triple Barrier Config ---
HOLDOUT_HORIZON     = 24
UPPER_BARRIER_PCT   = 0.02
LOWER_BARRIER_PCT   = 0.01

# --- Model & Splitting ---
SEQUENCE_LENGTH     = 24
TEST_FRAC           = 0.15
VAL_FRAC            = 0.15
RANDOM_SEED         = 42

# --- Trading Sim ---
BUY_TH              = 0.55
SELL_TH             = 0.45

SAVE_DIR = f"models/lstm/{time.strftime('%Y%m%d_%H%M%S')}/"
os.makedirs(SAVE_DIR, exist_ok=True)

# (Functions fetch_ohlcv_ccxt, add_indicators, make_labels_triple_barrier, make_feature_matrix remain the same)
def fetch_ohlcv_ccxt(symbol: str, timeframe: str, limit: int) -> pd.DataFrame:
    exchange = ccxt.binance()
    exchange.load_markets()
    chunk_size = 1000
    all_ohlcv = []
    until = None
    with tqdm(total=limit, desc=f"Fetching {symbol} {timeframe}") as pbar:
        while len(all_ohlcv) < limit:
            fetch_limit = min(chunk_size, limit - len(all_ohlcv))
            if fetch_limit <= 0: break
            params = {'until': until} if until is not None else {}
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=None, limit=fetch_limit, params=params)
            if not ohlcv: break
            all_ohlcv = ohlcv + all_ohlcv
            until = ohlcv[0][0]
            pbar.update(len(ohlcv))
            if len(ohlcv) < fetch_limit: break
            time.sleep(exchange.rateLimit / 1000)
    if not all_ohlcv: raise RuntimeError("No OHLCV data fetched.")
    df = pd.DataFrame(all_ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
    df = df.drop_duplicates(subset=["timestamp"]).set_index("timestamp").sort_index()
    if len(df) > limit: df = df.iloc[-limit:]
    for col in ["open", "high", "low", "close", "volume"]: df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna()
    return df

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["rsi_14"] = ta.rsi(out["close"], length=14)
    out["ema_12"] = ta.ema(out["close"], length=12)
    out["ema_26"] = ta.ema(out["close"], length=26)
    macd = ta.macd(out["close"], fast=12, slow=26, signal=9)
    out["macd"] = macd["MACD_12_26_9"]
    out["macd_signal"] = macd["MACDs_12_26_9"]
    out["macd_hist"] = macd["MACDh_12_26_9"]
    bb = ta.bbands(out["close"], length=20, std=2)
    out["boll_mid"] = bb["BBM_20_2.0"]
    out["boll_upper"] = bb["BBU_20_2.0"]
    out["boll_lower"] = bb["BBL_20_2.0"]
    out["bb_width"] = (out["boll_upper"] - out["boll_lower"]) / out["boll_mid"]
    out["atr_14"] = ta.atr(out["high"], out["low"], out["close"], length=14)
    out["volatility_pct"] = out["close"].pct_change().rolling(20).std()
    out["ret_1"] = out["close"].pct_change(1)
    out["ret_3"] = out["close"].pct_change(3)
    out["ret_12"] = out["close"].pct_change(12)
    out["vol_chg"] = out["volume"].pct_change(5)
    out["ret_1_norm_by_atr"] = out["ret_1"] / out["atr_14"]
    out["ema_200"] = ta.ema(out["close"], length=200)
    out["dist_from_ema_200"] = (out["close"] / out["ema_200"]) - 1.0
    out["hour_of_day"] = out.index.hour
    out["day_of_week"] = out.index.dayofweek
    out = out.dropna()
    return out

def make_labels_triple_barrier(df: pd.DataFrame, horizon: int, upper_pct: float, lower_pct: float) -> pd.Series:
    outcomes = pd.Series(index=df.index, dtype=float).fillna(0.0)
    close_prices = df['close']
    for i in tqdm(range(len(df) - horizon), desc="Making Triple-Barrier Labels"):
        entry_time = df.index[i]
        entry_price = close_prices.loc[entry_time]
        upper_barrier = entry_price * (1 + upper_pct)
        lower_barrier = entry_price * (1 - lower_pct)
        window = df.iloc[i + 1 : i + 1 + horizon]
        time_to_upper = window.index[window['high'] >= upper_barrier].min()
        time_to_lower = window.index[window['low'] <= lower_barrier].min()
        if pd.notna(time_to_upper) and pd.notna(time_to_lower):
            if time_to_upper < time_to_lower: outcomes.loc[entry_time] = 1
            else: outcomes.loc[entry_time] = 0
        elif pd.notna(time_to_upper): outcomes.loc[entry_time] = 1
        elif pd.notna(time_to_lower): outcomes.loc[entry_time] = 0
        else: outcomes.loc[entry_time] = 0
    return outcomes.astype(int)

def make_feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "close","volume", "rsi_14","ema_12","ema_26", "macd","macd_signal","macd_hist",
        "boll_mid","boll_upper","boll_lower","bb_width", "atr_14","volatility_pct",
        "ret_1","ret_3","ret_12","vol_chg", "ret_1_norm_by_atr", 
        "dist_from_ema_200", "hour_of_day", "day_of_week"
    ]
    return df[cols].copy()

def create_sequences(X, y, sequence_length):
    Xs, ys = [], []
    for i in range(len(X) - sequence_length):
        Xs.append(X.iloc[i:(i + sequence_length)].values)
        ys.append(y.iloc[i + sequence_length])
    return np.array(Xs), np.array(ys)

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', tf.keras.metrics.AUC(name='auc')])
    return model

def small_pnl_sim(close: pd.Series, probs: np.ndarray, buy_th=0.55, sell_th=0.45, fee=0.0004):
    pos, entry_price, cash = 0, 0.0, 1.0
    ret_curve = []
    for t in range(1, len(close)):
        p, price_now = probs[t], close.iloc[t]
        if p >= buy_th and pos == 0:
            pos, entry_price, cash = 1, price_now, cash * (1 - fee)
        elif p <= sell_th and pos == 1:
            pnl = (price_now / entry_price) - 1.0
            cash *= (1 + pnl) * (1 - fee)
            pos, entry_price = 0, 0.0
        
        if pos == 1:
            pnl_unreal = (price_now / entry_price) - 1.0
            ret_curve.append(cash * (1 + pnl_unreal))
        else:
            ret_curve.append(cash)
            
    if pos == 1: 
        pnl = (close.iloc[-1] / entry_price) - 1.0
        cash *= (1 + pnl) * (1 - fee)
    return pd.Series(ret_curve, index=close.index[1:]), cash - 1.0

def main():
    np.random.seed(RANDOM_SEED)
    tf.random.set_seed(RANDOM_SEED)

    df = fetch_ohlcv_ccxt(SYMBOL, TIMEFRAME, LIMIT)
    df = add_indicators(df)
    y = make_labels_triple_barrier(df, HOLDOUT_HORIZON, UPPER_BARRIER_PCT, LOWER_BARRIER_PCT)
    X = make_feature_matrix(df)
    
    keep = (~X.isna().any(axis=1)) & (~y.isna())
    X, y = X[keep], y[keep]
    close_prices = df.loc[X.index, "close"]

    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=TEST_FRAC, shuffle=False)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=VAL_FRAC/(1-TEST_FRAC), shuffle=False)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    X_train = pd.DataFrame(X_train_scaled, index=X_train.index, columns=X_train.columns)
    X_val = pd.DataFrame(X_val_scaled, index=X_val.index, columns=X_val.columns)
    X_test = pd.DataFrame(X_test_scaled, index=X_test.index, columns=X_test.columns)

    X_train_seq, y_train_seq = create_sequences(X_train, y_train, SEQUENCE_LENGTH)
    X_val_seq, y_val_seq = create_sequences(X_val, y_val, SEQUENCE_LENGTH)
    X_test_seq, y_test_seq = create_sequences(X_test, y_test, SEQUENCE_LENGTH)

    model = build_lstm_model((X_train_seq.shape[1], X_train_seq.shape[2]))
    
    class_weights_ = class_weight.compute_class_weight('balanced', classes=np.unique(y_train_seq), y=y_train_seq)
    class_weight_dict = dict(enumerate(class_weights_))
    print(f"Using class weights: {class_weight_dict}")

    model_path = os.path.join(SAVE_DIR, "best_model.h5")
    early_stopping = EarlyStopping(monitor='val_auc', mode='max', patience=10, verbose=1, restore_best_weights=True)
    
    history = model.fit(X_train_seq, y_train_seq, epochs=100, batch_size=32,
                        validation_data=(X_val_seq, y_val_seq),
                        class_weight=class_weight_dict,
                        callbacks=[early_stopping], verbose=1)
    
    model.save(model_path)

    # --- Plotting training history ---
    print("\n=== Plotting Training History ===")
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss'); plt.ylabel('Loss'); plt.xlabel('Epoch'); plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(history.history['auc'], label='Train AUC')
    plt.plot(history.history['val_auc'], label='Validation AUC')
    plt.title('Model AUC'); plt.ylabel('AUC'); plt.xlabel('Epoch'); plt.legend()
    plt.tight_layout()
    history_plot_path = os.path.join(SAVE_DIR, "training_history.png")
    plt.savefig(history_plot_path)
    print(f"Saved training history plot → {history_plot_path}")

    def evaluate(split_name, X_seq, y_seq, threshold):
        loss, acc, auc = model.evaluate(X_seq, y_seq, verbose=0)
        probs = model.predict(X_seq).flatten()
        preds = (probs >= threshold).astype(int)
        prec, rec, f1, _ = precision_recall_fscore_support(y_seq, preds, average="binary", zero_division=0)
        cm = confusion_matrix(y_seq, preds).tolist()
        return {"split": split_name, "acc": acc, "prec": prec, "rec": rec, "f1": f1, "auc": auc, "cm": cm, "proba": probs}

    val_metrics = evaluate("val", X_val_seq, y_val_seq, threshold=BUY_TH)
    test_metrics = evaluate("test", X_test_seq, y_test_seq, threshold=BUY_TH)

    close_test_sim = close_prices.loc[y_test.index[SEQUENCE_LENGTH:]]
    ret_curve, pnl = small_pnl_sim(close_test_sim, test_metrics["proba"], BUY_TH, SELL_TH)

    print("\n=== Validation ===")
    print({k: round(v, 4) if isinstance(v, float) else v for k, v in val_metrics.items() if k not in ["proba", "cm"]})
    print("Confusion Matrix (val):", val_metrics["cm"])
    print("\n=== Test ===")
    print({k: round(v, 4) if isinstance(v, float) else v for k, v in test_metrics.items() if k not in ["proba", "cm"]})
    print("Confusion Matrix (test):", test_metrics["cm"])
    print(f"Simplified PnL Estimate (test): {pnl:.4f}")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = f"lstm_{SYMBOL.replace('/','-')}_{TIMEFRAME}_{stamp}"
    model_path = os.path.join(SAVE_DIR, base + ".joblib")
    dump(model, model_path)
    meta = {
        "symbol": SYMBOL, "timeframe": TIMEFRAME, "limit": LIMIT, 
        "horizon": HOLDOUT_HORIZON, "upper_barrier_pct": UPPER_BARRIER_PCT, "lower_barrier_pct": LOWER_BARRIER_PCT,
        "buy_threshold": BUY_TH, "sell_threshold": SELL_TH,
        "val_metrics": {k: float(v) if isinstance(v, (np.floating, float)) else v for k,v in val_metrics.items() if k not in ["proba"]},
        "test_metrics": {k: float(v) if isinstance(v, (np.floating, float)) else v for k,v in test_metrics.items() if k not in ["proba"]},
        "final_cash_return_estimate": float(pnl),
        "created_utc": stamp, "features": list(X.columns), "model": "RandomForestClassifier",
    }
    meta_path = os.path.join(SAVE_DIR, base + ".json")
    with open(meta_path, "w") as f: json.dump(meta, f, indent=2)
    print(f"\nSaved model → {model_path}")
    print(f"Saved metadata → {meta_path}")
    ret_curve.to_csv(os.path.join(SAVE_DIR, base + "_test_equity.csv"))
    print("Saved test equity curve CSV.")

if __name__ == "__main__":
    main()
