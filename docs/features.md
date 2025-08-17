# Features

This document lists all the features engineered for the models during the research project.

## Feature Groups

### Price Action & Momentum
- `ret_1`, `ret_3`, `ret_12`: Price returns over 1, 3, and 12 periods.
- `ema_12`, `ema_26`, `ema_200`: Exponential Moving Averages.
- `dist_from_ema_200`: The percentage distance of the price from the 200-period EMA.
- `macd`, `macd_signal`, `macd_hist`: MACD indicator components.
- `rsi_14`: 14-period Relative Strength Index.

### Volatility
- `atr_14`: 14-period Average True Range.
- `volatility_pct`: Percentage-based rolling standard deviation of returns.
- `bb_width`: The width of the Bollinger Bands, normalized by the middle band.
- `boll_mid`, `boll_upper`, `boll_lower`: The Bollinger Bands themselves.
- `ret_1_norm_by_atr`: The 1-period return normalized by the ATR, to get a volatility-adjusted momentum measure.

### Volume
- `volume`: The raw trading volume.
- `vol_chg`: The percentage change in volume over 5 periods.

### Time-Based (Cyclical)
- `hour_of_day`: The hour of the day (0-23).
- `day_of_week`: The day of the week (0-6).