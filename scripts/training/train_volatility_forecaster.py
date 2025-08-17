# scripts/training/train_volatility_forecaster.py
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
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# (Helper functions remain the same)
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

def make_labels_regression(df: pd.DataFrame, horizon: int) -> pd.Series:
    return df['atr_14'].shift(-horizon)

def make_feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.copy()

def create_sequences(X, y, sequence_length):
    Xs, ys = [], []
    for i in range(len(X) - sequence_length):
        Xs.append(X.iloc[i:(i + sequence_length)].values)
        ys.append(y.iloc[i + sequence_length])
    return np.array(Xs), np.array(ys)

def build_lstm_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(25, activation='relu'),
        Dense(1, activation='linear')
    ])
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=[tf.keras.metrics.MeanAbsoluteError(name='mae')])
    return model

def run_training_pipeline(config: dict):
    """Main function to run the training pipeline with a given config."""
    print(f"--- Starting Training Run with Config ---")
    print(json.dumps(config, indent=2))

    np.random.seed(config['RANDOM_SEED'])
    tf.random.set_seed(config['RANDOM_SEED'])

    SAVE_DIR = f"{config['SAVE_DIR_BASE']}/{time.strftime('%Y%m%d_%H%M%S')}/"
    os.makedirs(SAVE_DIR, exist_ok=True)

    df = fetch_ohlcv_ccxt(config['SYMBOL'], config['TIMEFRAME'], config['LIMIT'])
    df_with_indicators = add_indicators(df)
    
    y = make_labels_regression(df_with_indicators, config['REGRESSION_HORIZON'])
    X = make_feature_matrix(df_with_indicators)
    
    keep_idx = y.dropna().index
    X = X.loc[keep_idx]
    y = y.loc[keep_idx]

    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=config['TEST_FRAC'], shuffle=False)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=config['VAL_FRAC']/(1-config['TEST_FRAC']), shuffle=False)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    X_train = pd.DataFrame(X_train_scaled, index=X_train.index, columns=X_train.columns)
    X_val = pd.DataFrame(X_val_scaled, index=X_val.index, columns=X_val.columns)
    X_test = pd.DataFrame(X_test_scaled, index=X_test.index, columns=X_test.columns)

    X_train_seq, y_train_seq = create_sequences(X_train, y_train, config['SEQUENCE_LENGTH'])
    X_val_seq, y_val_seq = create_sequences(X_val, y_val, config['SEQUENCE_LENGTH'])
    X_test_seq, y_test_seq = create_sequences(X_test, y_test, config['SEQUENCE_LENGTH'])

    model = build_lstm_model((X_train_seq.shape[1], X_train_seq.shape[2]))
    model_path = os.path.join(SAVE_DIR, "best_volatility_model.h5")
    early_stopping = EarlyStopping(monitor='val_loss', mode='min', patience=10, verbose=1, restore_best_weights=True)
    
    history = model.fit(X_train_seq, y_train_seq, epochs=100, batch_size=32,
                        validation_data=(X_val_seq, y_val_seq),
                        callbacks=[early_stopping], verbose=1)
    
    model.save(model_path)

    y_pred_test = model.predict(X_test_seq).flatten()
    r2 = r2_score(y_test_seq, y_pred_test)
    print(f"\n--- Run Finished ---")
    print(f"Test Set R-squared (R²): {r2:.4f}")
    print(f"Model saved to {model_path}")
    
    return r2

if __name__ == "__main__":
    DEFAULT_CONFIG = {
        "SYMBOL": "BTC/USDT",
        "TIMEFRAME": "1h",
        "LIMIT": 5000,
        "REGRESSION_HORIZON": 12,
        "SEQUENCE_LENGTH": 24,
        "TEST_FRAC": 0.15,
        "VAL_FRAC": 0.15,
        "RANDOM_SEED": 42,
        "SAVE_DIR_BASE": "models/volatility_lstm"
    }
    run_training_pipeline(DEFAULT_CONFIG)
