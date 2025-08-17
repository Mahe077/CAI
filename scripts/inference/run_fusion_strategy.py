# run_fusion_strategy.py
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import ccxt
import pandas_ta as ta
import joblib
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# -----------------------------
# Config
# -----------------------------
# --- Model Paths (Update with your actual paths) ---
REGIME_MODEL_PATH = "/Users/maheshlakshan/Personal/DEV/Reaserch/crypto-trading-ai-research/models/regime_classifier/20250817_200859/rf_regime_BTC-USDT_1h_20250817T143909Z.joblib"
VOLATILITY_MODEL_PATH = "/Users/maheshlakshan/Personal/DEV/Reaserch/crypto-trading-ai-research/models/volatility_lstm/20250817_193236/best_volatility_model.h5"

# --- Data & Feature Config ---
SYMBOL = "BTC/USDT"
TIMEFRAME = "1h"
LIMIT = 5000

# --- LSTM & Sequence Config ---
SEQUENCE_LENGTH = 24

# --- Strategy Config ---
BREAKOUT_THRESHOLD = 0.25  # e.g., 0.25 = predict 25% increase in ATR
HOLDING_PERIOD = 12      # Hold trade for 12 hours

# (Helper functions from training scripts)
def fetch_ohlcv_ccxt(symbol: str, timeframe: str, limit: int) -> pd.DataFrame:
    # (Same as in training scripts)
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
    # (Same as in training scripts)
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

def create_sequences(X, sequence_length):
    Xs = []
    for i in range(len(X) - sequence_length + 1):
        Xs.append(X.iloc[i:(i + sequence_length)].values)
    return np.array(Xs)

def run_backtest(close_prices: pd.Series, signals: pd.Series, holding_period: int, fee=0.0004):
    cash = 1.0
    equity_curve = []
    position = 0
    entry_price = 0
    exit_time = None

    for i in range(len(close_prices)):
        current_price = close_prices.iloc[i]

        # Exit logic
        if position == 1 and i >= exit_time:
            pnl = (current_price / entry_price) - 1.0
            cash *= (1 + pnl) * (1 - fee) # Pay fee on exit
            position = 0
            entry_price = 0

        # Entry logic
        if signals.iloc[i] == 1 and position == 0:
            position = 1
            entry_price = current_price
            # Fee paid on exit in this simplified model
            exit_time = i + holding_period
        
        # Mark-to-market equity calculation
        if position == 1:
            unrealized_pnl = (current_price / entry_price) - 1.0
            equity = cash * (1 + unrealized_pnl)
            equity_curve.append(equity)
        else:
            equity_curve.append(cash)

    return pd.Series(equity_curve, index=close_prices.index)

def run_backtest_realistic(close_prices: pd.Series, signals: pd.Series,
                           atr: pd.Series, holding_period: int,
                           risk_per_trade=0.02, fee=0.0004, slippage=0.0005):
    """
    close_prices : pd.Series of close prices
    signals : pd.Series of 0/1 buy signals
    atr : pd.Series of ATR values for stop-loss
    holding_period : int, number of bars to hold
    risk_per_trade : fraction of capital to risk per trade
    fee : proportional trading fee
    slippage : assumed slippage per trade
    """
    capital = 1.0
    equity_curve = []
    position = 0
    entry_price = 0
    exit_index = None
    trade_size = 0

    for i in range(len(close_prices)):
        price = close_prices.iloc[i]

        # Exit logic
        if position == 1:
            # Stop-loss
            stop_loss_price = entry_price - atr.iloc[i]
            take_profit_price = entry_price + atr.iloc[i]  # optional, can be adjusted
            exit_flag = False

            if price <= stop_loss_price or price >= take_profit_price or i >= exit_index:
                pnl = (price / entry_price - 1.0) * trade_size
                # Deduct fees + slippage
                pnl = pnl * (1 - fee) - slippage * trade_size
                capital += pnl
                position = 0
                entry_price = 0
                exit_index = None
                trade_size = 0
                exit_flag = True

            # Mark-to-market for unrealized PnL
            if not exit_flag:
                unrealized_pnl = (price / entry_price - 1.0) * trade_size
                equity_curve.append(capital + unrealized_pnl)
                continue

        # Entry logic
        if signals.iloc[i] == 1 and position == 0:
            position = 1
            entry_price = price
            exit_index = i + holding_period
            trade_size = capital * risk_per_trade
            # Deduct entry fee + slippage
            capital -= trade_size * (fee + slippage)

        # Equity tracking when no open position
        equity_curve.append(capital)

    return pd.Series(equity_curve, index=close_prices.index)

def main():
    print("Loading models...")
    regime_model = joblib.load(REGIME_MODEL_PATH)
    volatility_model = tf.keras.models.load_model(VOLATILITY_MODEL_PATH)

    print("Fetching and preparing data...")
    df = fetch_ohlcv_ccxt(SYMBOL, TIMEFRAME, LIMIT)
    df_with_indicators = add_indicators(df)

    # --- Generate Predictions ---
    print("Generating predictions from models...")
    
    # 1. Regime Predictions
    regime_preds = regime_model.predict(df_with_indicators)
    regime_preds = pd.Series(regime_preds, index=df_with_indicators.index, name="regime")

    # 2. Volatility Predictions
    # Scale data for LSTM
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_with_indicators)
    X_scaled = pd.DataFrame(X_scaled, index=df_with_indicators.index, columns=df_with_indicators.columns)
    
    # Create sequences
    X_seq = create_sequences(X_scaled, SEQUENCE_LENGTH)
    
    # Predict
    vol_preds_scaled = volatility_model.predict(X_seq).flatten()
    
    # Inverse transform the predictions to get actual ATR values
    # We need a dummy array to inverse transform
    dummy_array = np.zeros((len(vol_preds_scaled), len(df_with_indicators.columns)))
    atr_col_index = df_with_indicators.columns.get_loc('atr_14')
    dummy_array[:, atr_col_index] = vol_preds_scaled
    vol_preds = scaler.inverse_transform(dummy_array)[:, atr_col_index]
    
    # Align predictions with original dataframe
    vol_preds = pd.Series(vol_preds, index=df_with_indicators.index[SEQUENCE_LENGTH-1:], name="predicted_atr")

    # --- Fusion Logic & Backtest ---
    print("Running fusion strategy and backtest...")
    
    # Combine all data into one DataFrame
    strategy_df = df_with_indicators.join(regime_preds).join(vol_preds).dropna()

    # Generate signals
    signals = pd.Series(0, index=strategy_df.index)
    
    # Condition 1: Regime must be High Volatility
    high_vol_periods = strategy_df['regime'] == 1
    
    # Condition 2: Predicted ATR must be > current ATR by a threshold
    breakout_condition = strategy_df['predicted_atr'] > strategy_df['atr_14'] * (1 + BREAKOUT_THRESHOLD)
    
    # Combine conditions
    buy_signals = high_vol_periods & breakout_condition
    signals[buy_signals] = 1

    print(f"Generated {signals.sum()} buy signals.")

    # Run backtest
    # equity_curve = run_backtest(strategy_df['close'], signals, HOLDING_PERIOD)

    equity_curve = run_backtest_realistic(
        strategy_df['close'],
        signals,
        strategy_df['atr_14'],
        HOLDING_PERIOD,
        risk_per_trade=0.02,
        fee=0.0004,
        slippage=0.0005
    )

    # --- Plotting ---
    print("Plotting equity curve...")
    plt.figure(figsize=(15, 7))
    equity_curve.plot()
    plt.title(f"Fusion Strategy Equity Curve - {SYMBOL}")
    plt.xlabel("Time")
    plt.ylabel("Equity")
    plt.grid(True)
    plt.show()
    
    final_equity = equity_curve.iloc[-1]
    print(f"\nFinal Equity: {final_equity:.4f}")

if __name__ == "__main__":
    main()
