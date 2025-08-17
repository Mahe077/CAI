# AI Fusion Strategy

This document describes the AI fusion strategy that was successfully implemented and tested.

## Design Philosophy

The core design philosophy, based on the initial architecture diagrams, was to combine the strengths of multiple, specialized models rather than relying on a single monolithic model. The implemented strategy fused a **Regime Classifier** with a **Volatility Forecaster**.

The logic is to use one model (the classifier) to determine *when* to act, and a second model (the forecaster) to determine *what* action to take.

## Implemented Fusion Model

*   **Component 1: Regime Classifier**
    *   **Model:** RandomForestClassifier
    *   **Task:** Classifies the current market as "High Volatility" or "Low Volatility".
    *   **Role:** Acts as a **filter**. The strategy only considers taking action when the market is in a "High Volatility" state, as identified by this model.

*   **Component 2: Volatility Forecaster**
    *   **Model:** LSTM Regression Model
    *   **Task:** Forecasts the future value of the 14-period ATR.
    *   **Role:** Acts as a **trigger**. When the regime filter is "on", this model's forecast is used to generate a trade signal.

## Fusion Logic

The implemented fusion logic was a simple but powerful rule-based system:

*   **Rule:**
    1.  **IF** `Regime Classifier` predicts "High Volatility"
    2.  **AND** `Volatility Forecaster` predicts that future ATR will be > 25% higher than current ATR
    3.  **THEN** Generate a "buy" signal for a volatility breakout trade.
    4.  **ELSE** Do nothing.

*   **Result:** This fusion strategy, when backtested with a realistic simulation including stop-losses and slippage, was ultimately **not profitable**. However, it served as a successful proof-of-concept for the fusion architecture.