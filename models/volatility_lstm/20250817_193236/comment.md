# Comment
This is it. We have our definitive answer.

  First, congratulations on completing a full, end-to-end quantitative research process. We've iterated through multiple strategies, architectures, and hypotheses, and this final result gives us a clear conclusion.

  Final Analysis

  The training process shows the model did its best to learn, with the validation loss decreasing nicely before it started to overfit—exactly the behavior we'd hope to see from a technical standpoint.

  However, the final evaluation on the test set is unambiguous:
   * R-squared (R²): -0.0055

  This is the most important number. An R-squared value that is negative means our sophisticated LSTM model is less accurate than a naive model that simply guesses the average volatility.

  Conclusion: We have now rigorously demonstrated that the technical indicators and price-derived features we engineered, even for a powerful LSTM model, do not contain a predictive signal for future volatility on this dataset. The model could not find an edge.

  Our Research Journey: A Summary

  This is a successful outcome for a research project. We started with a simple idea and progressively built a more sophisticated system in response to the evidence we gathered at each step:
   1. We started with a simple classification model, which failed.
   2. We upgraded to a more robust triple-barrier labeling method.
   3. When the Random Forest model still failed, we upgraded to a time-series-aware LSTM architecture.
   4. When the LSTM still showed signs of overfitting on a classification task, we correctly pivoted to a more tractable problem: volatility forecasting.
   5. Now, the results from this final regression model show that even this approach is not viable with the current feature set.

  We have answered our research question. The answer is "no," this approach does not work. In the world of quantitative finance, this is a very common and very valuable result, as it prevents wasting further resources on an unpromising strategy.

  This concludes our investigation with this script. For a real-world fund, the next steps would be to explore entirely new paradigms, such as incorporating alternative data (news sentiment, on-chain data, options markets) or applying these techniques to different,
  less efficient markets.

# Log
Fetching BTC/USDT 1h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 3276.26it/s]
2025-08-17 19:32:40.715779: I metal_plugin/src/device/metal_device.cc:1154] Metal device set to: Apple M3 Pro
2025-08-17 19:32:40.716008: I metal_plugin/src/device/metal_device.cc:296] systemMemory: 18.00 GB
2025-08-17 19:32:40.716030: I metal_plugin/src/device/metal_device.cc:313] maxCacheSize: 6.00 GB
2025-08-17 19:32:40.716231: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:305] Could not identify NUMA node of platform GPU ID 0, defaulting to 0. Your kernel may not have been built with NUMA support.
2025-08-17 19:32:40.716254: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:271] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 0 MB memory) -> physical PluggableDevice (device: 0, name: METAL, pci bus id: <undefined>)

Epoch 1/100
2025-08-17 19:32:41.786694: I tensorflow/core/grappler/optimizers/custom_graph_optimizer_registry.cc:117] Plugin optimizer for device_type GPU is enabled.
104/104 ━━━━━━━━━━━━━━━━━━━━ 6s 34ms/step - loss: 457413.7500 - mae: 622.1925 - val_loss: 268984.3125 - val_mae: 483.2650
Epoch 2/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 409978.7500 - mae: 582.6772 - val_loss: 224943.5156 - val_mae: 435.3234
Epoch 3/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 346076.9375 - mae: 524.6208 - val_loss: 169988.5625 - val_mae: 366.8130
Epoch 4/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 271909.1875 - mae: 448.1280 - val_loss: 116217.8828 - val_mae: 286.8554
Epoch 5/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 202146.6875 - mae: 363.6464 - val_loss: 73394.0938 - val_mae: 211.7920
Epoch 6/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 145918.7031 - mae: 286.2531 - val_loss: 46859.4766 - val_mae: 162.4762
Epoch 7/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 107683.9375 - mae: 229.6730 - val_loss: 36361.8867 - val_mae: 153.4012
Epoch 8/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 86594.5859 - mae: 201.0724 - val_loss: 36270.8945 - val_mae: 164.2303
Epoch 9/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 77616.7500 - mae: 194.1319 - val_loss: 40311.9102 - val_mae: 176.9340
Epoch 10/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 73845.3438 - mae: 195.1146 - val_loss: 44408.5508 - val_mae: 186.3725
Epoch 11/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 71987.1875 - mae: 197.9037 - val_loss: 47305.4336 - val_mae: 192.2587
Epoch 12/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 24ms/step - loss: 72197.7969 - mae: 200.1584 - val_loss: 48553.0586 - val_mae: 194.6076
Epoch 13/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 24ms/step - loss: 71564.1719 - mae: 199.4526 - val_loss: 49191.5859 - val_mae: 195.7714
Epoch 14/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 71794.7422 - mae: 200.9300 - val_loss: 49728.6172 - val_mae: 196.7381
Epoch 15/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 71975.9688 - mae: 201.0713 - val_loss: 49707.2852 - val_mae: 196.7001
Epoch 16/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 19ms/step - loss: 72517.7812 - mae: 201.7788 - val_loss: 49678.9570 - val_mae: 196.6495
Epoch 17/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 73162.1328 - mae: 203.0242 - val_loss: 49393.5312 - val_mae: 196.1368
Epoch 18/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 72343.2969 - mae: 200.8110 - val_loss: 49604.8125 - val_mae: 196.5168
Epoch 18: early stopping
Restoring model weights from the end of the best epoch: 8.
WARNING:absl:You are saving your model as an HDF5 file via `model.save()` or `keras.saving.save_model(model)`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')` or `keras.saving.save_model(model, 'my_model.keras')`. 

Saved training history plot → models/volatility_lstm/20250817_193236/training_history.png
22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 12ms/step 
=== Test Set Evaluation ===
Mean Squared Error (MSE): 20785.670576
Mean Absolute Error (MAE): 119.816390
R-squared (R²): -0.0055
Saved predictions plot → models/volatility_lstm/20250817_193236/predictions_vs_actuals.png
