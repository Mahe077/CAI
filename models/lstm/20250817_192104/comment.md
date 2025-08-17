# Comment
This is the most important result we've had so far. Thank you for running it. The script and the pipeline we've built are working perfectly, and they have given us a crystal clear, albeit disappointing, answer.

Final Analysis: We've Hit a Wall

Let's look at the training history, which tells the whole story:
* Training AUC: Climbed to almost 0.95. This means the LSTM model was powerful enough to almost perfectly "learn" the training dataset. It successfully found patterns in that specific slice of historical data.
* Validation AUC: Started at 0.43 and never improved. This is the crucial part. When the model was shown new data it had never seen before (the validation set), its performance was worse than random. It had zero predictive power on new data.

This is a classic, textbook case of severe overfitting.

Conclusion: The model is memorizing noise in the training data, not learning a generalizable, predictive signal. We can now say with high confidence that the features we have engineered, even the advanced ones, do not contain a reliable, predictive signal for the 
future price direction using this methodology.

Continuing to tune this model (e.g., changing the number of LSTM layers or the learning rate) will not solve this fundamental problem. We need to change the question we are asking.

The Strategic Pivot: From Prediction to Volatility Forecasting

Instead of trying to predict the direction of the market (which is famously difficult), I propose we pivot to a more common and often more successful task in quantitative finance: predicting market volatility.

Instead of a classification problem ("will the price go up?"), we would change it to a regression problem ("how much will the price move?").

This would involve re-framing our goal:
* New Label: Instead of a 0 or 1, our target y would be a future value of a volatility indicator, like the atr_14.
* New Model Goal: The LSTM would predict the future volatility.
* New Output: The model's output would be a number (e.g., the predicted ATR), not a probability.

A successful volatility-forecasting model is a valuable tool. It can be used to size trades, for options pricing, or to build more advanced risk management systems.

This is a major pivot, but it's driven by the data and the clear results we've obtained. It's better to change our approach than to continue trying to force a model to find a signal that isn't there.


# Log
Fetching BTC/USDT 1h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 3321.78it/s]
Making Triple-Barrier Labels: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4773/4773 [00:01<00:00, 3021.26it/s]
2025-08-17 19:21:10.269765: I metal_plugin/src/device/metal_device.cc:1154] Metal device set to: Apple M3 Pro
2025-08-17 19:21:10.269865: I metal_plugin/src/device/metal_device.cc:296] systemMemory: 18.00 GB
2025-08-17 19:21:10.269959: I metal_plugin/src/device/metal_device.cc:313] maxCacheSize: 6.00 GB
2025-08-17 19:21:10.270107: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:305] Could not identify NUMA node of platform GPU ID 0, defaulting to 0. Your kernel may not have been built with NUMA support.
2025-08-17 19:21:10.270181: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:271] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 0 MB memory) -> physical PluggableDevice (device: 0, name: METAL, pci bus id: <undefined>)

Using class weights: {0: 0.6517403206883066, 1: 2.1475515463917527}
Epoch 1/100
2025-08-17 19:21:12.236994: I tensorflow/core/grappler/optimizers/custom_graph_optimizer_registry.cc:117] Plugin optimizer for device_type GPU is enabled.
105/105 ━━━━━━━━━━━━━━━━━━━━ 11s 51ms/step - accuracy: 0.6085 - auc: 0.6267 - loss: 0.6677 - val_accuracy: 0.7658 - val_auc: 0.4353 - val_loss: 0.6156
Epoch 2/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - accuracy: 0.6937 - auc: 0.7698 - loss: 0.5733 - val_accuracy: 0.5589 - val_auc: 0.3102 - val_loss: 0.8844
Epoch 3/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - accuracy: 0.7480 - auc: 0.8449 - loss: 0.4871 - val_accuracy: 0.5632 - val_auc: 0.3179 - val_loss: 1.0722
Epoch 4/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - accuracy: 0.7984 - auc: 0.8868 - loss: 0.4201 - val_accuracy: 0.5747 - val_auc: 0.3575 - val_loss: 1.0625
Epoch 5/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - accuracy: 0.8323 - auc: 0.9108 - loss: 0.3703 - val_accuracy: 0.6034 - val_auc: 0.3294 - val_loss: 1.2173
Epoch 6/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 3s 24ms/step - accuracy: 0.8557 - auc: 0.9305 - loss: 0.3249 - val_accuracy: 0.6006 - val_auc: 0.3103 - val_loss: 1.3635
Epoch 7/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - accuracy: 0.8578 - auc: 0.9340 - loss: 0.3157 - val_accuracy: 0.5704 - val_auc: 0.3497 - val_loss: 1.3451
Epoch 8/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - accuracy: 0.8605 - auc: 0.9395 - loss: 0.3056 - val_accuracy: 0.6049 - val_auc: 0.3034 - val_loss: 1.4067
Epoch 9/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - accuracy: 0.8632 - auc: 0.9426 - loss: 0.2972 - val_accuracy: 0.6149 - val_auc: 0.3090 - val_loss: 1.4724
Epoch 10/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - accuracy: 0.8707 - auc: 0.9472 - loss: 0.2756 - val_accuracy: 0.6049 - val_auc: 0.3265 - val_loss: 1.4596
Epoch 11/100
105/105 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - accuracy: 0.8617 - auc: 0.9452 - loss: 0.2883 - val_accuracy: 0.5733 - val_auc: 0.2910 - val_loss: 1.6478
Epoch 11: early stopping
Restoring model weights from the end of the best epoch: 1.
WARNING:absl:You are saving your model as an HDF5 file via `model.save()` or `keras.saving.save_model(model)`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')` or `keras.saving.save_model(model, 'my_model.keras')`. 

=== Plotting Training History ===
Saved training history plot → models/lstm/20250817_192104/training_history.png
22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 13ms/step 
22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 6ms/step 

=== Validation ===
{'split': 'val', 'acc': 0.7658, 'prec': 0.0, 'rec': 0.0, 'f1': 0.0, 'auc': 0.4353}
Confusion Matrix (val): [[545, 0], [151, 0]]

=== Test ===
{'split': 'test', 'acc': 0.8549, 'prec': 0.0, 'rec': 0.0, 'f1': 0.0, 'auc': 0.516}
Confusion Matrix (test): [[595, 0], [101, 0]]
Simplified PnL Estimate (test): 0.0000