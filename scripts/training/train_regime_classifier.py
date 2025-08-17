# train_regime_classifier.py
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_auc_score, confusion_matrix
from joblib import dump

# -----------------------------
# Config
# -----------------------------
SYMBOL              = "BTC/USDT"
TIMEFRAME           = "1h"
LIMIT               = 5000

# --- Regime Config ---
VOLATILITY_WINDOW   = 100         # Lookback for long-term volatility average

# --- Model & Splitting ---
TEST_FRAC           = 0.15
VAL_FRAC            = 0.15
RANDOM_SEED         = 42

SAVE_DIR = f"models/regime_classifier/{time.strftime('%Y%m%d_%H%M%S')}/"
os.makedirs(SAVE_DIR, exist_ok=True)

# (Functions fetch_ohlcv_ccxt and add_indicators are reused)
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

def make_regime_labels(df: pd.DataFrame, window: int) -> pd.Series:
    """Labels market regime based on volatility.
    1 = High Volatility, 0 = Low Volatility
    """
    long_term_vol = df['volatility_pct'].rolling(window=window).mean()
    # Label is 1 if current volatility is above the long-term average
    y = (df['volatility_pct'] > long_term_vol).astype(int)
    return y

def make_feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    # We can use all available indicators to predict the regime
    return df.copy()

def main():
    np.random.seed(RANDOM_SEED)

    df = fetch_ohlcv_ccxt(SYMBOL, TIMEFRAME, LIMIT)
    df_with_indicators = add_indicators(df)
    
    y = make_regime_labels(df_with_indicators, VOLATILITY_WINDOW)
    X = make_feature_matrix(df_with_indicators)

    # Align X and y, dropping NaNs from label creation
    keep_idx = y.dropna().index
    X = X.loc[keep_idx]
    y = y.loc[keep_idx]

    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=TEST_FRAC, shuffle=False)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=VAL_FRAC/(1-TEST_FRAC), shuffle=False)

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        min_samples_leaf=5,
        n_jobs=-1,
        random_state=RANDOM_SEED,
        class_weight="balanced"
    )
    model.fit(X_train, y_train)

    # --- Feature Importance ---
    print("\n=== Feature Importance ===")
    feature_importances = pd.DataFrame({
        'feature': X_train.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    print(feature_importances.to_string())

    # --- Evaluation ---
    def evaluate(split_name, Xs, ys):
        proba = model.predict_proba(Xs)[:, 1]
        pred  = model.predict(Xs)
        acc = accuracy_score(ys, pred)
        prec, rec, f1, _ = precision_recall_fscore_support(ys, pred, average="binary", zero_division=0)
        try: auc = roc_auc_score(ys, proba)
        except ValueError: auc = float("nan")
        cm = confusion_matrix(ys, pred).tolist()
        return {"split": split_name, "acc": acc, "prec": prec, "rec": rec, "f1": f1, "auc": auc, "cm": cm}

    val_metrics = evaluate("val", X_val, y_val)
    test_metrics = evaluate("test", X_test, y_test)

    print("\n=== Validation ===")
    print({k: round(v, 4) if isinstance(v, float) else v for k, v in val_metrics.items() if k != 'cm'})
    print("Confusion Matrix (val):", val_metrics["cm"])
    print("\n=== Test ===")
    print({k: round(v, 4) if isinstance(v, float) else v for k, v in test_metrics.items() if k != 'cm'})
    print("Confusion Matrix (test):", test_metrics["cm"])

    # --- Saving ---
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = f"rf_regime_{SYMBOL.replace('/','-')}_{TIMEFRAME}_{stamp}"
    model_path = os.path.join(SAVE_DIR, base + ".joblib")
    dump(model, model_path)
    print(f"\nSaved model → {model_path}")

if __name__ == "__main__":
    main()
