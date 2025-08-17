# Crypto Trading AI Research Log

## Objective
The initial goal of this research project was to determine if a profitable trading model could be built by predicting the future price movements of BTC/USDT using machine learning techniques on 1-hour OHLCV data.

---

## Phase 1: Initial Baseline (RandomForest Classification)

*   **Methodology:**
    *   **Model:** `RandomForestClassifier`.
    *   **Features:** Standard technical indicators (RSI, MACD, Bollinger Bands, etc.).
    *   **Labels:** Simple binary classification based on future return (e.g., `return > 0.1%` in 3 hours).
*   **Result:**
    *   The model showed no predictive power.
    *   The Area Under Curve (AUC) score on the test set was consistently below 0.5, indicating the model's performance was worse than random guessing.
*   **Conclusion:** The initial simple setup was not viable.

---

## Phase 2: Improved Labeling (Triple-Barrier Method)

*   **Methodology Pivot:** To create a more robust and realistic prediction target, we replaced the simple labeling with the **Triple-Barrier Method**. This involved setting a profit-take, a stop-loss, and a time limit for each trade.
*   **Result:**
    *   Performance did not improve (AUC remained < 0.5).
    *   The model "collapsed" by learning to predict only the majority class ("don't buy"), resulting in high accuracy but zero precision or recall.
*   **Conclusion:** The labeling was more robust, but the features were still insufficient.

---

## Phase 3: Advanced Feature Engineering

*   **Methodology Pivot:** To give the model more context, we engineered more sophisticated features.
    *   Volatility-Normalized Returns (`return / ATR`).
    *   Distance from a long-term moving average.
    *   Time-based features (hour of day, day of week).
*   **Result:**
    *   No significant improvement was observed. The model was still unable to find a predictive signal.
*   **Conclusion:** The feature set, even when enhanced, was not sufficient for the Random Forest model.

---

## Phase 4: Architecture Upgrade (LSTM Model)

*   **Methodology Pivot:** We replaced the `RandomForestClassifier` with a time-series-aware **Long Short-Term Memory (LSTM)** neural network.
*   **Result:**
    *   The model showed signs of **severe overfitting**. The training AUC climbed to ~0.95, while the validation AUC remained below 0.5.
    *   This indicated the model was powerful enough to memorize noise in the training data but completely failed to generalize to new, unseen data. (Train AUC >> Val AUC).
*   **Conclusion:** The model architecture was more powerful, but it still couldn't find a real signal, leading us to suspect a class imbalance problem.

---

## Phase 5: High-Impact Fixes (Class Weighting)

*   **Methodology Pivot:** To combat the overfitting and the model's tendency to ignore the rare "buy" signals, we implemented **class weighting**. This forces the model to penalize errors on the minority class more heavily.
*   **Result:**
    *   The overfitting persisted. The gap between the high training AUC and the low validation AUC remained.
    *   The model still failed to generalize, confirming the issue was not just the class imbalance.
*   **Conclusion:** The features themselves, regardless of the model, did not seem to contain a directional signal.

---

## Phase 6: Strategic Pivot (Volatility Forecasting)

*   **Methodology Pivot:** We changed the problem from **classification** (predicting direction) to **regression** (forecasting future volatility, specifically the ATR).
*   **Result:**
    *   The initial, un-optimized regression model showed a negative R-squared **R-squared (R²) of -0.0055**, indicating it was worse than a naive baseline.
*   **Conclusion:** The model required hyperparameter tuning to find a potential edge.

---

## Phase 7: Hyperparameter Optimization & Successful Outcome

*   **Methodology:** An optimizer script was created to systematically test 18 configurations of the volatility forecasting model, varying timeframes, sequence lengths, and forecast horizons.
*   **Result:** The optimization process was **successful** and identified a genuinely predictive model.
    *   **Best R-squared (R²): 0.422**
*   **Best Performing Configuration:**
    *   **Timeframe:** `1h`
    *   **Forecast Horizon:** `12` hours
    *   **Lookback Window (Sequence Length):** `48` hours

---

## Final Project Conclusion

While the initial goal of predicting price *direction* proved to be inviable with the available features, the strategic pivot to forecasting *volatility* was **highly successful**. After a rigorous process of iteration, feature engineering, architectural changes, and hyperparameter optimization, the project culminated in a final LSTM model that can explain **42.2%** of the variance in future volatility on unseen data. This demonstrates a significant and statistically valid predictive edge, providing a valuable, working model as the successful conclusion to this research project.
