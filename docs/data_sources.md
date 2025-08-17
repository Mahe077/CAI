# Data Sources

This document provides the rationale for each data source used in the project.

## Primary Data Source

-   **Source:** Binance Spot Market Data
-   **Provider:** `ccxt` Python library
-   **Asset:** BTC/USDT
-   **Timeframes Used:** 1-hour (`1h`), 4-hour (`4h`), and 1-day (`1d`).
-   **Rationale:** Binance provides high-quality, high-frequency historical data with significant depth, covering many years. The `ccxt` library provides a standardized and reliable way to access this data, handling API rate limits and pagination. This single source was deemed sufficient for the initial research phase focused on methodology and signal discovery from price data alone.

## Secondary Data Sources (Future Work)

The architectural design and research log identified that incorporating alternative data sources is a key next step for improving model performance. These were not used in the initial research but are recommended for future work:

-   **CoinGecko / CoinMarketCap:** For supplementary market data, historical snapshots, and developer/social metrics.
-   **Glassnode / On-Chain Data:** For network health, transaction flows, whale activity, and other fundamental blockchain metrics.
-   **Social Media & News Feeds:** For sentiment analysis using data from Twitter, Reddit, Telegram, and crypto news outlets.