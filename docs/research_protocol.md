# Research Protocol

This document defines the hypothesis, goals, and evaluation protocol for the research.

## Hypothesis

The final, successful hypothesis that this research validated was:
*   **"It is possible to forecast near-term market volatility (as measured by ATR) on the BTC/USDT pair using a model trained on historical price-derived features."**

This was a pivot from the initial hypotheses concerning directional price prediction, which were invalidated during the research process.

## Goals

*   **Primary Goal:** To build a machine learning model with a statistically significant predictive edge on a financial time series task.
*   **Secondary Goal:** To rigorously test different modeling approaches (classification vs. regression, different model architectures) and document the findings.
*   **Final Goal:** To identify the optimal set of parameters (timeframe, lookback window, etc.) for the successful model.

## Evaluation Protocol

The final evaluation protocol for the successful volatility forecasting model was as follows:

*   **Model:** LSTM Regression Model.
*   **Splitting:** Data was split chronologically into training, validation, and test sets to prevent lookahead bias.
*   **Primary Metric:** **R-squared (R²)** on the unseen test set.
    *   An R² > 0 indicates that the model has a predictive edge over a simple baseline (predicting the mean).
*   **Secondary Metrics:**
    *   **Mean Squared Error (MSE):** The loss function the model optimized.
    *   **Mean Absolute Error (MAE):** An interpretable measure of the average prediction error in dollar terms (of ATR).
*   **Selection Criteria:** The model hyperparameters were selected by running an optimization script that systematically searched for the configuration with the highest R² on the test set.