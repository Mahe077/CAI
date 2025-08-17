# Label Generation

This document describes how prediction targets (labels) were derived during the different phases of the project.

## 1. Simple Return (Classification)
- **Goal:** Predict short-term price direction.
- **Method:** A binary label was created based on the return after a fixed horizon.
- **Formula:** `Label = 1 if (future_return > 0.1%) else 0`
- **Conclusion:** This method was found to be too noisy and did not lead to a predictive model.

## 2. Triple-Barrier Method (Classification)
- **Goal:** Create a more robust directional signal that incorporates risk management.
- **Method:** For each data point, three "barriers" were projected into the future:
    1.  **Upper Barrier:** A profit-take level (e.g., +2%).
    2.  **Lower Barrier:** A stop-loss level (e.g., -1%).
    3.  **Time Barrier:** A maximum holding period (e.g., 24 hours).
- **Formula:** `Label = 1` if the upper barrier was hit first. `Label = 0` if the lower or time barrier was hit first.
- **Conclusion:** While methodologically more sound, the model was still unable to predict these labels, suggesting the features did not contain a directional signal.

## 3. Future Volatility (Regression)
- **Goal:** Pivot from directional prediction to forecasting future market volatility.
- **Method:** The label became a continuous variable representing a future value of a volatility indicator.
- **Formula:** `Label = df['atr_14'].shift(-HORIZON)`
- **Conclusion:** This approach was **successful**. The final model was able to predict future volatility with a reasonable degree of accuracy (R² of 0.422).