# Risk Analysis

This document outlines assumptions, limitations, and robustness tests related to the project.

## Assumptions

*   **Market data is sufficient:** The core assumption, which was ultimately challenged, was that 1-hour OHLCV data contains enough information to build a predictive model.
*   **Past predicts future:** The model operates on the assumption that patterns learned from historical data will continue to be valid in the future. This is not guaranteed.

## Limitations & Discovered Risks

*   **Directional Prediction Failure:** The primary finding of this research is that the tested features and models **cannot reliably predict price direction**. Any strategy based on this would be unprofitable.
*   **Volatility Model is Not a Trading Signal:** The final, successful model predicts *volatility*, not direction. It does not, by itself, provide a "buy" or "sell" signal. Using it directly for directional trading would be a misapplication of the model.
*   **Overfitting Risk:** The LSTM models showed a strong tendency to overfit. While techniques like Early Stopping were used, any change to the model or features requires careful monitoring of the validation loss to ensure the model is generalizing.
*   **Regime Dependence:** The model's performance is likely dependent on the market regime. The R² score of 0.42 is an average over the test period; performance during specific market conditions (e.g., a black swan event) is not guaranteed and would require further stress-testing.
*   **Backtest Limitations:** The final fusion strategy backtest, while more realistic, still makes simplifying assumptions about fees, slippage, and order execution. Live performance could differ significantly.

## Robustness Tests & Future Work

To be deployed, the models from this project would require further robustness testing:

*   **Out-of-Sample Testing:** Test the final model on completely new data from a different time period.
*   **Sensitivity Analysis:** Analyze how model performance changes when its key parameters (timeframe, lookback, etc.) are varied slightly.
*   **Stationarity Analysis:** Perform statistical tests to understand how the underlying data distributions change over time, which can impact model performance.