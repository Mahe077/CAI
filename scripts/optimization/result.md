Starting optimization process for 18 experiments...

--- Running Experiment 1/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 12,
  "SEQUENCE_LENGTH": 24,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2971.07it/s]
2025-08-18 00:17:16.529232: I metal_plugin/src/device/metal_device.cc:1154] Metal device set to: Apple M3 Pro
2025-08-18 00:17:16.529469: I metal_plugin/src/device/metal_device.cc:296] systemMemory: 18.00 GB
2025-08-18 00:17:16.529494: I metal_plugin/src/device/metal_device.cc:313] maxCacheSize: 6.00 GB
2025-08-18 00:17:16.529690: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:305] Could not identify NUMA node of platform GPU ID 0, defaulting to 0. Your kernel may not have been built with NUMA support.
2025-08-18 00:17:16.529710: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:271] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 0 MB memory) -> physical PluggableDevice (device: 0, name: METAL, pci bus id: <undefined>)

Epoch 1/100
2025-08-18 00:17:17.331861: I tensorflow/core/grappler/optimizers/custom_graph_optimizer_registry.cc:117] Plugin optimizer for device_type GPU is enabled.
104/104 ━━━━━━━━━━━━━━━━━━━━ 5s 26ms/step - loss: 455541.0312 - mae: 620.6063 - val_loss: 267420.0625 - val_mae: 481.2248
Epoch 2/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 402588.5625 - mae: 576.2260 - val_loss: 218789.2500 - val_mae: 427.7226
Epoch 3/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 333592.9062 - mae: 512.5803 - val_loss: 161332.1406 - val_mae: 354.2457
Epoch 4/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 257397.0469 - mae: 431.4511 - val_loss: 106650.2344 - val_mae: 270.6515
Epoch 5/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 186453.1406 - mae: 343.1605 - val_loss: 65444.7891 - val_mae: 196.1473
Epoch 6/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 24ms/step - loss: 132299.3125 - mae: 266.2246 - val_loss: 42757.5977 - val_mae: 157.5391
Epoch 7/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 98968.7266 - mae: 216.7879 - val_loss: 35907.3359 - val_mae: 157.7790
Epoch 8/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 81610.9141 - mae: 196.0920 - val_loss: 37985.4805 - val_mae: 170.4533
Epoch 9/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 74850.6484 - mae: 193.6035 - val_loss: 42336.0312 - val_mae: 181.8624
Epoch 10/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 72471.6250 - mae: 195.3009 - val_loss: 46148.8203 - val_mae: 190.0093
Epoch 11/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 72057.0938 - mae: 199.0021 - val_loss: 48167.2852 - val_mae: 193.8830
Epoch 12/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 71922.6328 - mae: 200.4975 - val_loss: 49048.9336 - val_mae: 195.4832
Epoch 13/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 72765.9922 - mae: 201.9634 - val_loss: 49223.9375 - val_mae: 195.7962
Epoch 14/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 71687.8125 - mae: 200.8129 - val_loss: 49508.3398 - val_mae: 196.3037
Epoch 15/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 72120.4844 - mae: 200.6033 - val_loss: 49660.1719 - val_mae: 196.5724
Epoch 16/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 72112.6484 - mae: 202.0398 - val_loss: 49593.1016 - val_mae: 196.4539
Epoch 17/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 72203.3438 - mae: 200.8401 - val_loss: 49588.4766 - val_mae: 196.4458
Epoch 17: early stopping
Restoring model weights from the end of the best epoch: 7.
 
22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 12ms/step 

--- Run Finished ---
Test Set R-squared (R²): -0.0269
Model saved to models/volatility_lstm_optimized/20250818_001712/best_volatility_model.h5

--- Running Experiment 2/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 12,
  "SEQUENCE_LENGTH": 48,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 3040.14it/s]

Epoch 1/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 5s 28ms/step - loss: 451112.9375 - mae: 616.5545 - val_loss: 253305.6719 - val_mae: 465.2270
Epoch 2/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 364674.4062 - mae: 541.5370 - val_loss: 177659.1719 - val_mae: 375.2196
Epoch 3/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 265493.8750 - mae: 439.8846 - val_loss: 105978.1172 - val_mae: 268.0831
Epoch 4/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 176006.7812 - mae: 327.8456 - val_loss: 57304.0312 - val_mae: 180.9049
Epoch 5/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 115417.6953 - mae: 240.2752 - val_loss: 38215.3867 - val_mae: 157.7392
Epoch 6/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 85308.9453 - mae: 200.0974 - val_loss: 38479.0508 - val_mae: 171.7235
Epoch 7/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 74895.9766 - mae: 193.2063 - val_loss: 43799.0195 - val_mae: 185.6215
Epoch 8/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 24ms/step - loss: 73656.4453 - mae: 199.0041 - val_loss: 47436.2461 - val_mae: 193.0365
Epoch 9/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 72958.5000 - mae: 201.0146 - val_loss: 48978.9258 - val_mae: 195.8647
Epoch 10/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 5s 50ms/step - loss: 72776.6406 - mae: 201.6987 - val_loss: 49857.7461 - val_mae: 197.3989
Epoch 11/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 73196.9453 - mae: 202.9034 - val_loss: 49851.8086 - val_mae: 197.3887
Epoch 12/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 29ms/step - loss: 72406.4688 - mae: 202.4619 - val_loss: 49759.6133 - val_mae: 197.2301
Epoch 13/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 24ms/step - loss: 72308.5547 - mae: 202.0382 - val_loss: 49639.6250 - val_mae: 197.0230
Epoch 14/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 72547.1484 - mae: 201.5366 - val_loss: 47564.4023 - val_mae: 193.2268
Epoch 15/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 69485.3750 - mae: 191.5736 - val_loss: 29707.4141 - val_mae: 148.7241
Epoch 16/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 50520.9414 - mae: 156.2024 - val_loss: 23833.4688 - val_mae: 133.3279
Epoch 17/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 37695.3281 - mae: 134.6112 - val_loss: 27461.5312 - val_mae: 146.4902
Epoch 18/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 24ms/step - loss: 29829.3555 - mae: 120.6152 - val_loss: 24178.5723 - val_mae: 133.6678
Epoch 19/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 25671.1445 - mae: 114.1067 - val_loss: 26334.1367 - val_mae: 143.2326
Epoch 20/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 29ms/step - loss: 22478.6406 - mae: 108.0078 - val_loss: 21965.3730 - val_mae: 130.5272
Epoch 21/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 19053.5586 - mae: 98.8364 - val_loss: 25746.2441 - val_mae: 136.3833
Epoch 22/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 15880.9521 - mae: 91.8527 - val_loss: 24288.2891 - val_mae: 129.9008
Epoch 23/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 13922.7471 - mae: 86.6558 - val_loss: 33168.6016 - val_mae: 148.8380
Epoch 24/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 12638.6006 - mae: 83.6444 - val_loss: 32012.4121 - val_mae: 151.5186
Epoch 25/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 24ms/step - loss: 11294.9229 - mae: 79.4803 - val_loss: 37643.2422 - val_mae: 155.3250
Epoch 26/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 10655.3447 - mae: 77.9296 - val_loss: 38670.9297 - val_mae: 159.4311
Epoch 27/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 10798.2285 - mae: 77.3136 - val_loss: 46604.8125 - val_mae: 168.4884
Epoch 28/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 10129.1709 - mae: 74.1427 - val_loss: 46178.9766 - val_mae: 166.9620
Epoch 29/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 9019.6846 - mae: 71.1884 - val_loss: 51770.1836 - val_mae: 176.6419
Epoch 30/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 9189.5137 - mae: 70.5796 - val_loss: 43320.8047 - val_mae: 168.0582
Epoch 30: early stopping
Restoring model weights from the end of the best epoch: 20.

21/21 ━━━━━━━━━━━━━━━━━━━━ 1s 16ms/step 

--- Run Finished ---
Test Set R-squared (R²): 0.4220
Model saved to models/volatility_lstm_optimized/20250818_001758/best_volatility_model.h5

--- Running Experiment 3/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 12,
  "SEQUENCE_LENGTH": 72,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2664.22it/s]

Epoch 1/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 7s 49ms/step - loss: 450804.7188 - mae: 615.8929 - val_loss: 264138.0000 - val_mae: 475.7746
Epoch 2/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 390958.3750 - mae: 565.1512 - val_loss: 213493.9219 - val_mae: 419.1870
Epoch 3/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 321486.2812 - mae: 499.5483 - val_loss: 156473.0938 - val_mae: 344.5294
Epoch 4/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 246483.5156 - mae: 417.6288 - val_loss: 103664.6953 - val_mae: 263.3965
Epoch 5/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 179986.8125 - mae: 332.5792 - val_loss: 64990.6211 - val_mae: 195.3779
Epoch 6/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 38ms/step - loss: 129037.2109 - mae: 260.4389 - val_loss: 43965.0391 - val_mae: 162.9470
Epoch 7/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 97653.7891 - mae: 214.4545 - val_loss: 37828.3242 - val_mae: 164.0087
Epoch 8/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 81618.9688 - mae: 196.9895 - val_loss: 39770.5352 - val_mae: 175.3804
Epoch 9/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 75607.3516 - mae: 195.9724 - val_loss: 43814.5938 - val_mae: 185.3960
Epoch 10/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 73828.5703 - mae: 198.6508 - val_loss: 47041.8867 - val_mae: 191.9227
Epoch 11/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 73095.9062 - mae: 200.4785 - val_loss: 48933.8203 - val_mae: 195.3555
Epoch 12/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 36ms/step - loss: 73147.8828 - mae: 202.8400 - val_loss: 49760.9805 - val_mae: 196.7722
Epoch 13/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 36ms/step - loss: 73063.8516 - mae: 203.2506 - val_loss: 50001.0898 - val_mae: 197.1742
Epoch 14/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 36ms/step - loss: 73465.4141 - mae: 203.6255 - val_loss: 49844.4805 - val_mae: 196.9125
Epoch 15/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 35ms/step - loss: 72456.4219 - mae: 201.9024 - val_loss: 50379.3203 - val_mae: 197.8025
Epoch 16/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 39ms/step - loss: 72636.1562 - mae: 202.8098 - val_loss: 50550.1328 - val_mae: 198.0842
Epoch 17/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 72780.6250 - mae: 204.2925 - val_loss: 50132.9531 - val_mae: 197.3934
Epoch 17: early stopping
Restoring model weights from the end of the best epoch: 7.
 
21/21 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step 

--- Run Finished ---
Test Set R-squared (R²): -0.0257
Model saved to models/volatility_lstm_optimized/20250818_001932/best_volatility_model.h5

--- Running Experiment 4/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 24,
  "SEQUENCE_LENGTH": 24,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 3242.83it/s]

Epoch 1/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 5s 30ms/step - loss: 462671.0625 - mae: 626.4314 - val_loss: 283625.6875 - val_mae: 497.5529
Epoch 2/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 430170.1562 - mae: 599.9598 - val_loss: 255162.1250 - val_mae: 468.0765
Epoch 3/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 369945.1562 - mae: 546.7773 - val_loss: 184358.7344 - val_mae: 385.0899
Epoch 4/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 282106.0625 - mae: 458.9768 - val_loss: 122400.6719 - val_mae: 295.9308
Epoch 5/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 24ms/step - loss: 205580.0469 - mae: 368.1064 - val_loss: 75340.8203 - val_mae: 215.1082
Epoch 6/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 144460.5938 - mae: 284.5489 - val_loss: 47244.2812 - val_mae: 164.2370
Epoch 7/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 105139.6797 - mae: 225.0958 - val_loss: 36694.6172 - val_mae: 156.6322
Epoch 8/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 83937.1172 - mae: 197.1010 - val_loss: 37287.6133 - val_mae: 167.9660
Epoch 9/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 75938.3672 - mae: 194.5990 - val_loss: 41521.4609 - val_mae: 179.9501
Epoch 10/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 73414.4844 - mae: 196.1322 - val_loss: 45302.2500 - val_mae: 188.2010
Epoch 11/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 72488.1016 - mae: 198.9581 - val_loss: 47691.3203 - val_mae: 192.8688
Epoch 12/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 72122.9609 - mae: 200.1005 - val_loss: 48661.4219 - val_mae: 194.6397
Epoch 13/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 71996.7891 - mae: 200.6192 - val_loss: 49089.3828 - val_mae: 195.4036
Epoch 14/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 72576.1094 - mae: 202.2592 - val_loss: 49040.4727 - val_mae: 195.3168
Epoch 15/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 72691.3984 - mae: 202.2664 - val_loss: 49295.1406 - val_mae: 195.7685
Epoch 16/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 71724.1641 - mae: 200.6824 - val_loss: 49400.4688 - val_mae: 195.9548
Epoch 17/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 73024.5000 - mae: 201.3163 - val_loss: 46518.0156 - val_mae: 190.6082
Epoch 17: early stopping
Restoring model weights from the end of the best epoch: 7.
 
22/22 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step 

--- Run Finished ---
Test Set R-squared (R²): -0.0758
Model saved to models/volatility_lstm_optimized/20250818_002043/best_volatility_model.h5

--- Running Experiment 5/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 24,
  "SEQUENCE_LENGTH": 48,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2886.70it/s]

Epoch 1/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 5s 31ms/step - loss: 456403.2500 - mae: 620.9487 - val_loss: 268347.6562 - val_mae: 480.8440
Epoch 2/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 30ms/step - loss: 398563.8438 - mae: 572.2963 - val_loss: 215495.9688 - val_mae: 422.3254
Epoch 3/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 324077.5312 - mae: 502.9875 - val_loss: 154402.7031 - val_mae: 342.4432
Epoch 4/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 34ms/step - loss: 243979.4062 - mae: 415.8057 - val_loss: 98873.8594 - val_mae: 255.8068
Epoch 5/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 173877.0312 - mae: 325.4546 - val_loss: 60048.0977 - val_mae: 185.6477
Epoch 6/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 29ms/step - loss: 123142.8906 - mae: 251.6203 - val_loss: 40926.8945 - val_mae: 158.5563
Epoch 7/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 36ms/step - loss: 92864.5469 - mae: 209.2410 - val_loss: 37243.9297 - val_mae: 165.4322
Epoch 8/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 79212.7891 - mae: 194.9052 - val_loss: 40725.8984 - val_mae: 178.6902
Epoch 9/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 74790.4453 - mae: 196.4377 - val_loss: 45042.0156 - val_mae: 188.5110
Epoch 10/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 29ms/step - loss: 72739.1172 - mae: 198.5399 - val_loss: 47934.4844 - val_mae: 194.1416
Epoch 11/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 29ms/step - loss: 72804.8125 - mae: 200.9911 - val_loss: 49429.1562 - val_mae: 196.8075
Epoch 12/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 72387.3281 - mae: 200.6680 - val_loss: 50166.1602 - val_mae: 198.0631
Epoch 13/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 72617.7969 - mae: 201.8198 - val_loss: 50549.8281 - val_mae: 198.7075
Epoch 14/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 72375.5469 - mae: 201.9396 - val_loss: 50753.2930 - val_mae: 199.0455
Epoch 15/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 73934.8906 - mae: 204.6136 - val_loss: 50322.4609 - val_mae: 198.3268
Epoch 16/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 30ms/step - loss: 72898.9766 - mae: 202.4405 - val_loss: 50452.4805 - val_mae: 198.5450
Epoch 17/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 72846.4141 - mae: 202.3293 - val_loss: 50593.5391 - val_mae: 198.7804
Epoch 17: early stopping
Restoring model weights from the end of the best epoch: 7.
 
21/21 ━━━━━━━━━━━━━━━━━━━━ 0s 15ms/step 

--- Run Finished ---
Test Set R-squared (R²): -0.0046
Model saved to models/volatility_lstm_optimized/20250818_002131/best_volatility_model.h5

--- Running Experiment 6/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 24,
  "SEQUENCE_LENGTH": 72,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2824.74it/s]

Epoch 1/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 9s 57ms/step - loss: 452757.4688 - mae: 617.5165 - val_loss: 262923.5625 - val_mae: 474.3123
Epoch 2/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 381344.7188 - mae: 556.3085 - val_loss: 199964.5469 - val_mae: 402.5093
Epoch 3/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 296813.5938 - mae: 473.9109 - val_loss: 133871.1562 - val_mae: 311.0168
Epoch 4/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 212397.6094 - mae: 375.7645 - val_loss: 79820.2891 - val_mae: 221.9513
Epoch 5/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 145184.1406 - mae: 284.4415 - val_loss: 48390.5391 - val_mae: 168.1686
Epoch 6/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 102819.2812 - mae: 221.7970 - val_loss: 38209.6602 - val_mae: 163.1281
Epoch 7/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 83202.9141 - mae: 198.3888 - val_loss: 39935.2344 - val_mae: 175.9458
Epoch 8/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 75408.3047 - mae: 196.5322 - val_loss: 44415.7656 - val_mae: 186.9813
Epoch 9/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 39ms/step - loss: 73750.7969 - mae: 199.4164 - val_loss: 47668.2148 - val_mae: 193.4696
Epoch 10/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 73563.9219 - mae: 202.3542 - val_loss: 49323.5430 - val_mae: 196.4408
Epoch 11/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 72840.6641 - mae: 202.0443 - val_loss: 49998.4844 - val_mae: 197.5934
Epoch 12/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 72973.4766 - mae: 202.6041 - val_loss: 50321.5391 - val_mae: 198.1337
Epoch 13/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 72932.3594 - mae: 202.6571 - val_loss: 50394.4414 - val_mae: 198.2552
Epoch 14/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 73756.9766 - mae: 204.3296 - val_loss: 50573.1719 - val_mae: 198.5527
Epoch 15/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 30ms/step - loss: 72923.2109 - mae: 202.5228 - val_loss: 50531.6367 - val_mae: 198.4839
Epoch 16/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 35ms/step - loss: 73428.4062 - mae: 203.6048 - val_loss: 50441.6875 - val_mae: 198.3343
Epoch 16: early stopping
Restoring model weights from the end of the best epoch: 6.
 
21/21 ━━━━━━━━━━━━━━━━━━━━ 1s 18ms/step 

--- Run Finished ---
Test Set R-squared (R²): -0.0478
Model saved to models/volatility_lstm_optimized/20250818_002232/best_volatility_model.h5

--- Running Experiment 7/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "4h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 12,
  "SEQUENCE_LENGTH": 24,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 4h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2944.79it/s]

Epoch 1/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 24ms/step - loss: 818294.5625 - mae: 777.8378 - val_loss: 2345157.5000 - val_mae: 1455.0946
Epoch 2/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 745468.1250 - mae: 728.8136 - val_loss: 2180332.0000 - val_mae: 1397.3098
Epoch 3/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 650595.8125 - mae: 660.4081 - val_loss: 1965208.0000 - val_mae: 1318.0863
Epoch 4/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 24ms/step - loss: 542086.5625 - mae: 578.0972 - val_loss: 1718125.5000 - val_mae: 1220.7656
Epoch 5/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 436651.5625 - mae: 501.3410 - val_loss: 1471729.6250 - val_mae: 1115.2906
Epoch 6/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 348907.8125 - mae: 441.9867 - val_loss: 1247450.8750 - val_mae: 1009.7498
Epoch 7/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 284048.0625 - mae: 400.2262 - val_loss: 1063948.1250 - val_mae: 914.3804
Epoch 8/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 246656.1406 - mae: 377.2307 - val_loss: 929299.4375 - val_mae: 837.5171
Epoch 9/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 187447.3594 - mae: 289.1812 - val_loss: 772730.0625 - val_mae: 738.5571
Epoch 10/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 135725.0156 - mae: 223.6522 - val_loss: 636427.1875 - val_mae: 643.8585
Epoch 11/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 112224.3594 - mae: 203.1876 - val_loss: 540168.7500 - val_mae: 574.9919
Epoch 12/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 97791.8906 - mae: 190.7554 - val_loss: 472021.9062 - val_mae: 526.1010
Epoch 13/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 79401.5078 - mae: 170.4304 - val_loss: 401248.5000 - val_mae: 474.9456
Epoch 14/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 63915.6836 - mae: 149.1308 - val_loss: 341967.5625 - val_mae: 432.8445
Epoch 15/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 22ms/step - loss: 55277.9727 - mae: 141.9501 - val_loss: 297492.2812 - val_mae: 397.0865
Epoch 16/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 49002.6055 - mae: 136.2868 - val_loss: 266424.6562 - val_mae: 381.4418
Epoch 17/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 40607.4961 - mae: 123.1835 - val_loss: 243972.8125 - val_mae: 377.1228
Epoch 18/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 32978.9492 - mae: 113.3975 - val_loss: 229005.1719 - val_mae: 370.0397
Epoch 19/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 30970.5508 - mae: 111.2811 - val_loss: 224170.6719 - val_mae: 374.8478
Epoch 20/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 26263.9609 - mae: 104.1422 - val_loss: 220645.4844 - val_mae: 375.7552
Epoch 21/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 24320.7656 - mae: 100.0446 - val_loss: 214489.0156 - val_mae: 371.6392
Epoch 22/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 22682.6562 - mae: 97.4878 - val_loss: 187263.4688 - val_mae: 340.6639
Epoch 23/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 21052.0488 - mae: 92.9971 - val_loss: 186807.3594 - val_mae: 337.6525
Epoch 24/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 19254.1621 - mae: 91.1690 - val_loss: 210499.6719 - val_mae: 362.7882
Epoch 25/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 17537.4980 - mae: 87.4186 - val_loss: 181107.6719 - val_mae: 332.3528
Epoch 26/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 19ms/step - loss: 16551.4395 - mae: 86.7695 - val_loss: 181180.7188 - val_mae: 325.0400
Epoch 27/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 15433.3428 - mae: 82.0145 - val_loss: 188004.4375 - val_mae: 337.1121
Epoch 28/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 15006.7412 - mae: 82.5061 - val_loss: 189333.3438 - val_mae: 343.7002
Epoch 29/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 15423.8291 - mae: 83.7850 - val_loss: 211557.9688 - val_mae: 353.7144
Epoch 30/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 16247.6104 - mae: 85.0441 - val_loss: 202244.5469 - val_mae: 360.4088
Epoch 31/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 14786.2520 - mae: 83.8181 - val_loss: 209416.2031 - val_mae: 360.6192
Epoch 32/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 24ms/step - loss: 13883.0771 - mae: 80.6941 - val_loss: 198243.3438 - val_mae: 343.9480
Epoch 33/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 13590.6240 - mae: 80.2761 - val_loss: 213018.3906 - val_mae: 367.4756
Epoch 34/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 12326.6270 - mae: 76.3983 - val_loss: 209916.0312 - val_mae: 364.9568
Epoch 35/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 12403.4287 - mae: 76.5583 - val_loss: 188654.2500 - val_mae: 332.9455
Epoch 35: early stopping
Restoring model weights from the end of the best epoch: 25.
 
22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 13ms/step 

--- Run Finished ---
Test Set R-squared (R²): -3.7071
Model saved to models/volatility_lstm_optimized/20250818_002340/best_volatility_model.h5

--- Running Experiment 8/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "4h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 12,
  "SEQUENCE_LENGTH": 48,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 4h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2857.04it/s]
/opt/homebrew/Caskroom/miniconda/base/envs/crypto-trading-ai/lib/python3.10/site-packages/keras/src/layers/rnn/rnn.py:199: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.

104/104 ━━━━━━━━━━━━━━━━━━━━ 6s 36ms/step - loss: 826878.4375 - mae: 782.9024 - val_loss: 2358418.0000 - val_mae: 1457.2544
Epoch 2/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 759139.9375 - mae: 737.5541 - val_loss: 2201952.7500 - val_mae: 1402.5430
Epoch 3/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 665705.6250 - mae: 670.8966 - val_loss: 1988090.2500 - val_mae: 1324.1093
Epoch 4/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 30ms/step - loss: 556236.3750 - mae: 588.6654 - val_loss: 1743314.1250 - val_mae: 1228.2053
Epoch 5/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 448728.9062 - mae: 510.5245 - val_loss: 1493945.3750 - val_mae: 1122.1052
Epoch 6/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 358122.0625 - mae: 448.1113 - val_loss: 1268304.0000 - val_mae: 1016.6014
Epoch 7/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 35ms/step - loss: 292618.0938 - mae: 406.4330 - val_loss: 1082302.7500 - val_mae: 920.5854
Epoch 8/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 29ms/step - loss: 251838.6875 - mae: 381.1120 - val_loss: 944055.0000 - val_mae: 842.1577
Epoch 9/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 230339.6719 - mae: 367.8085 - val_loss: 849374.0625 - val_mae: 784.0113
Epoch 10/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 29ms/step - loss: 220151.0938 - mae: 361.5626 - val_loss: 789496.6250 - val_mae: 745.0765
Epoch 11/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 30ms/step - loss: 145225.6406 - mae: 239.6828 - val_loss: 647337.6250 - val_mae: 646.5899
Epoch 12/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 114571.9609 - mae: 206.9105 - val_loss: 545800.1250 - val_mae: 574.2965
Epoch 13/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 99600.0156 - mae: 196.4605 - val_loss: 496367.1875 - val_mae: 542.4133
Epoch 14/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 84096.1328 - mae: 178.6690 - val_loss: 410678.6875 - val_mae: 479.6858
Epoch 15/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 72051.2891 - mae: 166.1766 - val_loss: 356791.2812 - val_mae: 439.7908
Epoch 16/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 29ms/step - loss: 60398.9570 - mae: 152.9757 - val_loss: 315533.7188 - val_mae: 417.7473
Epoch 17/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 51809.7461 - mae: 143.5255 - val_loss: 276888.9688 - val_mae: 379.5923
Epoch 18/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 45647.0664 - mae: 136.6078 - val_loss: 255989.2031 - val_mae: 377.5113
Epoch 19/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 40212.7969 - mae: 128.0049 - val_loss: 239284.3906 - val_mae: 371.3811
Epoch 20/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 39ms/step - loss: 37657.8203 - mae: 124.7845 - val_loss: 230601.6406 - val_mae: 372.6114
Epoch 21/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 34818.6328 - mae: 121.8255 - val_loss: 223134.0000 - val_mae: 368.3866
Epoch 22/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 29ms/step - loss: 30456.7676 - mae: 114.6466 - val_loss: 219455.9531 - val_mae: 372.3651
Epoch 23/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 29ms/step - loss: 27645.9570 - mae: 109.2574 - val_loss: 222583.3281 - val_mae: 378.4262
Epoch 24/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 25468.6309 - mae: 104.8903 - val_loss: 227707.2031 - val_mae: 393.1223
Epoch 25/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 25174.5332 - mae: 104.8428 - val_loss: 231945.3906 - val_mae: 394.0411
Epoch 26/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 22077.0820 - mae: 97.8116 - val_loss: 244111.5156 - val_mae: 418.2968
Epoch 27/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 43ms/step - loss: 21778.2266 - mae: 95.6775 - val_loss: 219460.7812 - val_mae: 380.8124
Epoch 28/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 30ms/step - loss: 23191.8477 - mae: 99.6488 - val_loss: 214022.4219 - val_mae: 383.0074
Epoch 29/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 20028.7227 - mae: 93.5624 - val_loss: 234698.1250 - val_mae: 401.5536
Epoch 30/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 18502.4883 - mae: 90.0927 - val_loss: 223728.5469 - val_mae: 383.4409
Epoch 31/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 30ms/step - loss: 17109.6523 - mae: 87.3713 - val_loss: 216845.7812 - val_mae: 375.3553
Epoch 32/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 16966.3945 - mae: 86.9250 - val_loss: 214095.3125 - val_mae: 371.5786
Epoch 33/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 5s 50ms/step - loss: 15176.1074 - mae: 82.5981 - val_loss: 231174.8594 - val_mae: 388.6433
Epoch 34/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 38ms/step - loss: 15808.0244 - mae: 84.4583 - val_loss: 261824.8594 - val_mae: 419.6756
Epoch 35/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 15773.4355 - mae: 84.4313 - val_loss: 254185.7031 - val_mae: 411.8737
Epoch 36/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 5s 51ms/step - loss: 14452.9277 - mae: 81.2603 - val_loss: 256225.4531 - val_mae: 407.8062
Epoch 37/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 4s 41ms/step - loss: 13608.8037 - mae: 79.0993 - val_loss: 224269.5625 - val_mae: 375.9350
Epoch 38/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 13005.0459 - mae: 77.9837 - val_loss: 255203.9219 - val_mae: 405.9571
Epoch 38: early stopping
Restoring model weights from the end of the best epoch: 28.
 
21/21 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step 

--- Run Finished ---
Test Set R-squared (R²): -5.0170
Model saved to models/volatility_lstm_optimized/20250818_002509/best_volatility_model.h5

--- Running Experiment 9/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "4h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 12,
  "SEQUENCE_LENGTH": 72,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 4h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2971.60it/s]

Epoch 1/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 6s 36ms/step - loss: 821076.5000 - mae: 779.4528 - val_loss: 2351284.7500 - val_mae: 1452.6295
Epoch 2/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 42ms/step - loss: 736609.3125 - mae: 722.4739 - val_loss: 2164182.0000 - val_mae: 1386.7339
Epoch 3/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 631488.0000 - mae: 646.0351 - val_loss: 1926049.1250 - val_mae: 1298.0361
Epoch 4/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 515175.0312 - mae: 558.8844 - val_loss: 1663481.8750 - val_mae: 1192.6150
Epoch 5/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 406810.3125 - mae: 482.4789 - val_loss: 1406825.7500 - val_mae: 1079.6644
Epoch 6/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 41ms/step - loss: 321413.5938 - mae: 424.8579 - val_loss: 1183909.7500 - val_mae: 970.9577
Epoch 7/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 38ms/step - loss: 265889.7188 - mae: 389.4876 - val_loss: 1011986.5000 - val_mae: 877.9724
Epoch 8/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 36ms/step - loss: 237329.1875 - mae: 372.0399 - val_loss: 891778.1875 - val_mae: 806.6523
Epoch 9/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 41ms/step - loss: 209870.2500 - mae: 339.4201 - val_loss: 783051.6875 - val_mae: 736.4993
Epoch 10/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 146073.6094 - mae: 239.7265 - val_loss: 634392.4375 - val_mae: 634.3215
Epoch 11/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 38ms/step - loss: 113672.6797 - mae: 210.6508 - val_loss: 576600.5625 - val_mae: 593.8478
Epoch 12/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 104018.5469 - mae: 203.8820 - val_loss: 496844.6875 - val_mae: 538.2786
Epoch 13/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 95289.1641 - mae: 199.8678 - val_loss: 445577.5625 - val_mae: 504.7437
Epoch 14/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 78971.3906 - mae: 176.4683 - val_loss: 386661.1562 - val_mae: 466.5117
Epoch 15/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 65928.3906 - mae: 162.7424 - val_loss: 337854.4688 - val_mae: 435.4397
Epoch 16/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 55371.0742 - mae: 150.3296 - val_loss: 293383.8125 - val_mae: 411.5573
Epoch 17/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 40ms/step - loss: 47488.6250 - mae: 140.2345 - val_loss: 267744.1875 - val_mae: 398.3481
Epoch 18/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 43318.4336 - mae: 135.2329 - val_loss: 255186.0625 - val_mae: 398.7028
Epoch 19/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 39ms/step - loss: 41565.5117 - mae: 134.3890 - val_loss: 243832.6875 - val_mae: 393.6904
Epoch 20/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 37627.3516 - mae: 126.5953 - val_loss: 248427.5000 - val_mae: 393.5623
Epoch 21/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 37935.1133 - mae: 126.5215 - val_loss: 224646.6875 - val_mae: 377.2742
Epoch 22/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 30919.0703 - mae: 116.0051 - val_loss: 239353.7812 - val_mae: 400.9120
Epoch 23/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 30536.5156 - mae: 115.7071 - val_loss: 219337.1875 - val_mae: 381.2439
Epoch 24/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 26540.3652 - mae: 107.3328 - val_loss: 236190.6094 - val_mae: 403.9040
Epoch 25/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 36ms/step - loss: 25594.9277 - mae: 105.8618 - val_loss: 229207.8281 - val_mae: 397.6573
Epoch 26/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 25286.4688 - mae: 103.2725 - val_loss: 240744.7656 - val_mae: 412.0970
Epoch 27/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 24263.3965 - mae: 102.0019 - val_loss: 248848.5469 - val_mae: 421.9312
Epoch 28/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 22949.3418 - mae: 98.4086 - val_loss: 249762.2344 - val_mae: 422.2749
Epoch 29/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 22747.4492 - mae: 96.3465 - val_loss: 253916.7344 - val_mae: 426.9569
Epoch 30/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 21334.1113 - mae: 94.7435 - val_loss: 255642.3281 - val_mae: 429.6266
Epoch 31/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 36ms/step - loss: 21857.1934 - mae: 95.4456 - val_loss: 253122.9219 - val_mae: 426.2192
Epoch 32/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 20470.7852 - mae: 91.4329 - val_loss: 256814.3125 - val_mae: 430.1452
Epoch 33/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 20135.4277 - mae: 91.2640 - val_loss: 247448.8594 - val_mae: 418.0344
Epoch 33: early stopping
Restoring model weights from the end of the best epoch: 23.
 
21/21 ━━━━━━━━━━━━━━━━━━━━ 1s 16ms/step 

--- Run Finished ---
Test Set R-squared (R²): -3.5182
Model saved to models/volatility_lstm_optimized/20250818_002725/best_volatility_model.h5

--- Running Experiment 10/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "4h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 24,
  "SEQUENCE_LENGTH": 24,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 4h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2710.64it/s]

Epoch 1/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 5s 27ms/step - loss: 819078.9375 - mae: 776.6910 - val_loss: 2314662.2500 - val_mae: 1443.7841
Epoch 2/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 738680.0625 - mae: 722.2827 - val_loss: 2142866.7500 - val_mae: 1383.0103
Epoch 3/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 640864.1250 - mae: 651.3887 - val_loss: 1920670.1250 - val_mae: 1300.2002
Epoch 4/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 529750.7500 - mae: 568.2018 - val_loss: 1673376.8750 - val_mae: 1201.3442
Epoch 5/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 425641.7500 - mae: 493.7654 - val_loss: 1427383.3750 - val_mae: 1094.1818
Epoch 6/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 339482.5000 - mae: 436.3743 - val_loss: 1207674.8750 - val_mae: 988.6989
Epoch 7/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 281964.8750 - mae: 398.8016 - val_loss: 1033029.7500 - val_mae: 896.0543
Epoch 8/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 221883.4531 - mae: 329.8293 - val_loss: 864711.5000 - val_mae: 796.7079
Epoch 9/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 161109.6406 - mae: 248.2351 - val_loss: 705747.8125 - val_mae: 691.5381
Epoch 10/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 126677.7422 - mae: 213.5894 - val_loss: 591503.3750 - val_mae: 611.1097
Epoch 11/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 105769.0391 - mae: 195.4074 - val_loss: 507618.0000 - val_mae: 550.6636
Epoch 12/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 93665.3672 - mae: 186.5490 - val_loss: 443453.8125 - val_mae: 505.4552
Epoch 13/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 75926.4688 - mae: 163.5920 - val_loss: 381638.4688 - val_mae: 463.1096
Epoch 14/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 64447.4414 - mae: 151.5249 - val_loss: 332989.0312 - val_mae: 429.7735
Epoch 15/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 52012.0352 - mae: 135.5784 - val_loss: 296068.9375 - val_mae: 407.5558
Epoch 16/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 44469.4414 - mae: 126.8722 - val_loss: 268262.5938 - val_mae: 393.2865
Epoch 17/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 39416.0938 - mae: 119.0496 - val_loss: 250870.0156 - val_mae: 387.6068
Epoch 18/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 34379.2188 - mae: 113.7639 - val_loss: 240509.8281 - val_mae: 386.7516
Epoch 19/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 32124.3770 - mae: 110.3143 - val_loss: 231169.9375 - val_mae: 381.2945
Epoch 20/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 29213.9355 - mae: 107.1058 - val_loss: 231177.2969 - val_mae: 386.7569
Epoch 21/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 25913.1328 - mae: 101.4440 - val_loss: 230114.8594 - val_mae: 389.2335
Epoch 22/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 23743.6445 - mae: 96.1095 - val_loss: 231745.2969 - val_mae: 393.3694
Epoch 23/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 22458.1387 - mae: 93.6900 - val_loss: 234683.0312 - val_mae: 397.1284
Epoch 24/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 24ms/step - loss: 20191.8320 - mae: 91.5394 - val_loss: 239246.4219 - val_mae: 404.2242
Epoch 25/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 3s 24ms/step - loss: 21183.7617 - mae: 91.4238 - val_loss: 238783.2812 - val_mae: 406.7046
Epoch 26/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 19872.7988 - mae: 87.7692 - val_loss: 238959.7031 - val_mae: 403.6711
Epoch 27/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 20ms/step - loss: 19171.5000 - mae: 88.6229 - val_loss: 248396.7812 - val_mae: 419.1476
Epoch 28/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 18757.3027 - mae: 86.3886 - val_loss: 256508.5781 - val_mae: 427.0660
Epoch 29/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 23ms/step - loss: 18380.2227 - mae: 86.1975 - val_loss: 258434.2812 - val_mae: 426.6418
Epoch 30/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 21ms/step - loss: 17568.7695 - mae: 84.1664 - val_loss: 260709.2188 - val_mae: 432.8488
Epoch 31/100
104/104 ━━━━━━━━━━━━━━━━━━━━ 2s 22ms/step - loss: 17013.1660 - mae: 82.5002 - val_loss: 263998.0625 - val_mae: 435.1793
Epoch 31: early stopping
Restoring model weights from the end of the best epoch: 21.
 
22/22 ━━━━━━━━━━━━━━━━━━━━ 1s 15ms/step 

--- Run Finished ---
Test Set R-squared (R²): -3.4043
Model saved to models/volatility_lstm_optimized/20250818_002932/best_volatility_model.h5

--- Running Experiment 11/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "4h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 24,
  "SEQUENCE_LENGTH": 48,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 4h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2705.18it/s]

Epoch 1/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 6s 35ms/step - loss: 814666.9375 - mae: 773.6174 - val_loss: 2281488.0000 - val_mae: 1429.9557
Epoch 2/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 702880.1250 - mae: 696.8571 - val_loss: 2033195.5000 - val_mae: 1340.3289
Epoch 3/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 570088.4375 - mae: 597.4719 - val_loss: 1732978.3750 - val_mae: 1223.2186
Epoch 4/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 437202.5625 - mae: 502.5740 - val_loss: 1426608.6250 - val_mae: 1090.8228
Epoch 5/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 41ms/step - loss: 329154.1875 - mae: 429.5572 - val_loss: 1160499.5000 - val_mae: 961.1377
Epoch 6/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 264194.6562 - mae: 387.2382 - val_loss: 964719.8750 - val_mae: 853.2327
Epoch 7/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 232845.6562 - mae: 369.4084 - val_loss: 842044.0625 - val_mae: 778.3348
Epoch 8/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 222444.9688 - mae: 364.7508 - val_loss: 774492.0625 - val_mae: 734.2579
Epoch 9/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 24ms/step - loss: 212687.4062 - mae: 354.9291 - val_loss: 732620.6250 - val_mae: 705.8335
Epoch 10/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 30ms/step - loss: 812990.5625 - mae: 655.7209 - val_loss: 2472537.5000 - val_mae: 1495.1777
Epoch 11/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 177788.0312 - mae: 252.2493 - val_loss: 601990.4375 - val_mae: 614.4946
Epoch 12/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 105121.3281 - mae: 199.1334 - val_loss: 487088.3438 - val_mae: 532.8571
Epoch 13/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 87427.9922 - mae: 183.7455 - val_loss: 404698.5000 - val_mae: 477.6129
Epoch 14/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 68103.7422 - mae: 159.9704 - val_loss: 335550.2812 - val_mae: 431.3762
Epoch 15/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 53505.6328 - mae: 142.2873 - val_loss: 289974.1250 - val_mae: 404.5323
Epoch 16/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 44000.9375 - mae: 131.3572 - val_loss: 261853.7188 - val_mae: 394.1786
Epoch 17/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 37226.7891 - mae: 120.3004 - val_loss: 244878.0781 - val_mae: 390.2800
Epoch 18/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 32916.9570 - mae: 117.5585 - val_loss: 234120.6875 - val_mae: 387.0257
Epoch 19/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 27047.9023 - mae: 106.9646 - val_loss: 228054.9688 - val_mae: 385.5532
Epoch 20/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 24592.5215 - mae: 103.7085 - val_loss: 214249.0469 - val_mae: 374.3644
Epoch 21/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 22229.2832 - mae: 98.9912 - val_loss: 232942.7500 - val_mae: 397.8615
Epoch 22/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 21421.5566 - mae: 95.8377 - val_loss: 240502.7969 - val_mae: 407.4523
Epoch 23/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 18749.3105 - mae: 90.9898 - val_loss: 239961.0312 - val_mae: 410.3103
Epoch 24/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 19673.0566 - mae: 91.6284 - val_loss: 242690.6875 - val_mae: 415.0201
Epoch 25/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 20519.0508 - mae: 93.3143 - val_loss: 239365.0781 - val_mae: 410.2542
Epoch 26/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 18988.0918 - mae: 90.2459 - val_loss: 228247.8594 - val_mae: 397.4828
Epoch 27/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 25ms/step - loss: 18331.3926 - mae: 86.4812 - val_loss: 247254.9219 - val_mae: 421.2183
Epoch 28/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 26ms/step - loss: 18515.5820 - mae: 88.4145 - val_loss: 243384.0781 - val_mae: 415.2989
Epoch 29/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 27ms/step - loss: 17475.5430 - mae: 86.7186 - val_loss: 226768.9531 - val_mae: 391.1425
Epoch 30/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 28ms/step - loss: 15869.6279 - mae: 84.7115 - val_loss: 257412.2344 - val_mae: 427.5643
Epoch 30: early stopping
Restoring model weights from the end of the best epoch: 20.
 
21/21 ━━━━━━━━━━━━━━━━━━━━ 1s 17ms/step 

--- Run Finished ---
Test Set R-squared (R²): -3.8117
Model saved to models/volatility_lstm_optimized/20250818_003054/best_volatility_model.h5

--- Running Experiment 12/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "4h",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 24,
  "SEQUENCE_LENGTH": 72,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 4h: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2568.08it/s]
Epoch 1/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 6s 36ms/step - loss: 819224.0625 - mae: 775.9702 - val_loss: 2319440.2500 - val_mae: 1440.7792
Epoch 2/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 718505.3125 - mae: 707.4607 - val_loss: 2094127.5000 - val_mae: 1360.3425
Epoch 3/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 593966.6875 - mae: 615.6444 - val_loss: 1810301.0000 - val_mae: 1251.6812
Epoch 4/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 463270.6875 - mae: 521.3384 - val_loss: 1509876.1250 - val_mae: 1125.2914
Epoch 5/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 353549.4062 - mae: 446.2276 - val_loss: 1240808.5000 - val_mae: 998.6056
Epoch 6/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 280476.1875 - mae: 398.3203 - val_loss: 1032695.9375 - val_mae: 888.3134
Epoch 7/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 38ms/step - loss: 243628.7500 - mae: 375.3412 - val_loss: 893022.9375 - val_mae: 805.9937
Epoch 8/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 223300.4688 - mae: 362.2475 - val_loss: 809071.8750 - val_mae: 752.7317
Epoch 9/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 144291.6250 - mae: 236.0376 - val_loss: 640789.1875 - val_mae: 638.1443
Epoch 10/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 110636.4922 - mae: 203.0641 - val_loss: 528832.4375 - val_mae: 560.1681
Epoch 11/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 34ms/step - loss: 91355.4062 - mae: 183.3296 - val_loss: 444785.1562 - val_mae: 504.7620
Epoch 12/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 71928.0859 - mae: 162.6515 - val_loss: 374204.6562 - val_mae: 459.4536
Epoch 13/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 59122.6914 - mae: 146.8366 - val_loss: 325557.5000 - val_mae: 430.0909
Epoch 14/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 47558.8867 - mae: 130.4541 - val_loss: 289102.9375 - val_mae: 411.8076
Epoch 15/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 39797.0117 - mae: 122.3489 - val_loss: 267303.0312 - val_mae: 404.3921
Epoch 16/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 33ms/step - loss: 33375.6953 - mae: 113.8294 - val_loss: 256203.5312 - val_mae: 405.0970
Epoch 17/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 40ms/step - loss: 27868.3301 - mae: 105.0062 - val_loss: 259760.6406 - val_mae: 409.9113
Epoch 18/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 37ms/step - loss: 26080.4570 - mae: 103.3959 - val_loss: 267961.3125 - val_mae: 421.0120
Epoch 19/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 23875.8633 - mae: 98.3405 - val_loss: 260335.6250 - val_mae: 412.5262
Epoch 20/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 35ms/step - loss: 24412.3105 - mae: 99.3963 - val_loss: 267706.5000 - val_mae: 419.7604
Epoch 21/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 42ms/step - loss: 22260.8828 - mae: 95.7982 - val_loss: 268198.7500 - val_mae: 428.4057
Epoch 22/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 31ms/step - loss: 21766.9297 - mae: 93.6416 - val_loss: 272419.8125 - val_mae: 430.4836
Epoch 23/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 34ms/step - loss: 20642.2793 - mae: 91.5358 - val_loss: 269612.6562 - val_mae: 438.0225
Epoch 24/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 4s 34ms/step - loss: 20095.1660 - mae: 90.5713 - val_loss: 274356.3750 - val_mae: 434.3859
Epoch 25/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 19873.6191 - mae: 91.4904 - val_loss: 278157.1562 - val_mae: 445.5183
Epoch 26/100
103/103 ━━━━━━━━━━━━━━━━━━━━ 3s 32ms/step - loss: 19524.9785 - mae: 90.3272 - val_loss: 282951.5000 - val_mae: 447.3630
Epoch 26: early stopping
Restoring model weights from the end of the best epoch: 16.

21/21 ━━━━━━━━━━━━━━━━━━━━ 1s 18ms/step 

--- Run Finished ---
Test Set R-squared (R²): -1.3608
Model saved to models/volatility_lstm_optimized/20250818_003230/best_volatility_model.h5

--- Running Experiment 13/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1d",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 12,
  "SEQUENCE_LENGTH": 24,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1d:  58%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉                                                                                                 | 2925/5000 [00:00<00:00, 3108.98it/s]

Epoch 1/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 4s 33ms/step - loss: 2619115.5000 - mae: 1175.6663 - val_loss: 3776087.2500 - val_mae: 1685.7344
Epoch 2/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 2567672.2500 - mae: 1151.2815 - val_loss: 3698343.0000 - val_mae: 1662.0819
Epoch 3/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 2511369.2500 - mae: 1126.3318 - val_loss: 3610324.2500 - val_mae: 1635.3895
Epoch 4/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 2445162.2500 - mae: 1096.9277 - val_loss: 3504486.0000 - val_mae: 1602.7041
Epoch 5/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 2367789.2500 - mae: 1061.6622 - val_loss: 3380864.2500 - val_mae: 1563.6622
Epoch 6/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 2281861.0000 - mae: 1022.8142 - val_loss: 3244108.5000 - val_mae: 1519.3035
Epoch 7/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 2189224.0000 - mae: 982.0501 - val_loss: 3092340.0000 - val_mae: 1468.5085
Epoch 8/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 2084743.1250 - mae: 937.6323 - val_loss: 2925385.5000 - val_mae: 1410.5178
Epoch 9/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 1980085.2500 - mae: 896.3781 - val_loss: 2758151.7500 - val_mae: 1349.9358
Epoch 10/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 1877264.2500 - mae: 862.0915 - val_loss: 2591346.0000 - val_mae: 1286.6705
Epoch 11/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 1776323.3750 - mae: 839.3423 - val_loss: 2428412.7500 - val_mae: 1221.7150
Epoch 12/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 1688805.0000 - mae: 825.3426 - val_loss: 2270457.7500 - val_mae: 1155.3381
Epoch 13/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 1605993.5000 - mae: 819.5558 - val_loss: 2122364.7500 - val_mae: 1091.4945
Epoch 14/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 1529221.5000 - mae: 817.3788 - val_loss: 1985889.1250 - val_mae: 1036.0118
Epoch 15/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 1460214.2500 - mae: 811.4866 - val_loss: 1859819.2500 - val_mae: 991.2524
Epoch 16/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 1318837.3750 - mae: 671.2077 - val_loss: 1704930.8750 - val_mae: 944.7136
Epoch 17/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 1203420.5000 - mae: 620.6547 - val_loss: 1559574.2500 - val_mae: 903.2549
Epoch 18/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 1113400.7500 - mae: 583.5410 - val_loss: 1428593.2500 - val_mae: 867.0226
Epoch 19/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 1020384.5625 - mae: 555.8395 - val_loss: 1312578.1250 - val_mae: 835.8997
Epoch 20/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 933149.8750 - mae: 524.0124 - val_loss: 1209884.0000 - val_mae: 810.3120
Epoch 21/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 846987.8125 - mae: 495.5551 - val_loss: 1125370.3750 - val_mae: 796.4355
Epoch 22/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 781534.5625 - mae: 472.0189 - val_loss: 1048360.0000 - val_mae: 779.2001
Epoch 23/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 707451.5625 - mae: 448.7896 - val_loss: 1001192.1875 - val_mae: 778.5005
Epoch 24/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 644049.5000 - mae: 420.7548 - val_loss: 934488.2500 - val_mae: 756.8552
Epoch 25/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 583473.0625 - mae: 396.2048 - val_loss: 794225.1875 - val_mae: 659.9092
Epoch 26/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 522867.9375 - mae: 365.8783 - val_loss: 656527.5625 - val_mae: 571.8980
Epoch 27/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 472447.1875 - mae: 346.8144 - val_loss: 635013.0625 - val_mae: 585.0755
Epoch 28/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 425947.1562 - mae: 326.4990 - val_loss: 595543.8750 - val_mae: 594.5761
Epoch 29/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 385978.3750 - mae: 310.0412 - val_loss: 519326.0938 - val_mae: 545.8275
Epoch 30/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 344380.2812 - mae: 288.1896 - val_loss: 468264.0938 - val_mae: 513.8231
Epoch 31/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 313708.3438 - mae: 272.0364 - val_loss: 415408.0312 - val_mae: 471.9788
Epoch 32/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 290049.1875 - mae: 262.9702 - val_loss: 417575.0938 - val_mae: 501.5447
Epoch 33/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 260513.2188 - mae: 249.1518 - val_loss: 408334.0312 - val_mae: 506.4093
Epoch 34/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 250714.0625 - mae: 244.1562 - val_loss: 455944.5312 - val_mae: 555.9767
Epoch 35/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 224431.4375 - mae: 230.9782 - val_loss: 332754.1875 - val_mae: 456.6010
Epoch 36/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 200310.1250 - mae: 220.3405 - val_loss: 306034.4062 - val_mae: 439.0611
Epoch 37/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 181824.4688 - mae: 206.4326 - val_loss: 269421.9375 - val_mae: 415.2804
Epoch 38/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 168412.0156 - mae: 200.7517 - val_loss: 272921.5625 - val_mae: 420.8749
Epoch 39/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 156485.5938 - mae: 191.1359 - val_loss: 261344.9844 - val_mae: 416.1566
Epoch 40/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 142384.6875 - mae: 183.9791 - val_loss: 244981.5781 - val_mae: 403.4858
Epoch 41/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 131100.6562 - mae: 178.9056 - val_loss: 247353.9062 - val_mae: 405.2282
Epoch 42/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 116906.8281 - mae: 165.2404 - val_loss: 242446.5000 - val_mae: 399.4445
Epoch 43/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 111954.6328 - mae: 160.8813 - val_loss: 262193.8750 - val_mae: 427.0384
Epoch 44/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 101344.1719 - mae: 153.2398 - val_loss: 249636.3594 - val_mae: 407.5507
Epoch 45/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 93449.1250 - mae: 150.4148 - val_loss: 193391.8594 - val_mae: 361.8968
Epoch 46/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 90508.9297 - mae: 146.8082 - val_loss: 256232.8281 - val_mae: 418.0237
Epoch 47/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 84262.7500 - mae: 140.6422 - val_loss: 193019.6562 - val_mae: 347.5430
Epoch 48/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 78515.0312 - mae: 136.5597 - val_loss: 232464.0781 - val_mae: 392.7684
Epoch 49/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 74043.1797 - mae: 137.2965 - val_loss: 206442.8125 - val_mae: 364.2827
Epoch 50/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 24ms/step - loss: 65043.8789 - mae: 127.9158 - val_loss: 185381.3438 - val_mae: 345.2436
Epoch 51/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 68912.7969 - mae: 130.0240 - val_loss: 172378.0000 - val_mae: 333.9486
Epoch 52/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 63756.3711 - mae: 125.5455 - val_loss: 138739.0781 - val_mae: 300.5213
Epoch 53/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 62502.8906 - mae: 126.2769 - val_loss: 171499.0938 - val_mae: 343.0322
Epoch 54/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 55253.8281 - mae: 121.1554 - val_loss: 159573.2812 - val_mae: 324.3695
Epoch 55/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 57370.6797 - mae: 121.6819 - val_loss: 192399.7344 - val_mae: 372.4655
Epoch 56/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 52577.8438 - mae: 115.6097 - val_loss: 159280.7656 - val_mae: 315.2738
Epoch 57/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 57523.9609 - mae: 123.4544 - val_loss: 166485.6406 - val_mae: 334.2807
Epoch 58/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 48658.9727 - mae: 114.3075 - val_loss: 159740.5938 - val_mae: 321.9263
Epoch 59/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 50337.2266 - mae: 116.3776 - val_loss: 173200.1562 - val_mae: 332.7056
Epoch 60/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 45814.8789 - mae: 107.8979 - val_loss: 171575.7344 - val_mae: 325.6344
Epoch 61/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 43941.2578 - mae: 110.0380 - val_loss: 194040.2031 - val_mae: 357.3596
Epoch 62/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 45690.1641 - mae: 112.4095 - val_loss: 191996.0781 - val_mae: 359.7484
Epoch 62: early stopping
Restoring model weights from the end of the best epoch: 52.
 
12/12 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step 

--- Run Finished ---
Test Set R-squared (R²): 0.1026
Model saved to models/volatility_lstm_optimized/20250818_003411/best_volatility_model.h5

--- Running Experiment 14/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1d",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 12,
  "SEQUENCE_LENGTH": 48,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1d:  58%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉                                                                                                 | 2925/5000 [00:01<00:00, 2885.24it/s]

Epoch 1/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 4s 40ms/step - loss: 2641458.2500 - mae: 1180.0615 - val_loss: 3943114.5000 - val_mae: 1727.7089
Epoch 2/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 2576063.2500 - mae: 1150.4727 - val_loss: 3852491.5000 - val_mae: 1702.1014
Epoch 3/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 2507577.7500 - mae: 1120.3301 - val_loss: 3738318.7500 - val_mae: 1668.8220
Epoch 4/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 2423994.0000 - mae: 1082.3567 - val_loss: 3601065.7500 - val_mae: 1627.8900
Epoch 5/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 29ms/step - loss: 2325299.5000 - mae: 1038.4570 - val_loss: 3442238.0000 - val_mae: 1579.1761
Epoch 6/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 2218283.7500 - mae: 991.4371 - val_loss: 3268535.2500 - val_mae: 1524.0906
Epoch 7/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 29ms/step - loss: 2105761.2500 - mae: 943.7870 - val_loss: 3083398.7500 - val_mae: 1463.0609
Epoch 8/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 1983584.1250 - mae: 897.8066 - val_loss: 2891413.0000 - val_mae: 1396.9149
Epoch 9/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 1871321.0000 - mae: 863.2026 - val_loss: 2699088.7500 - val_mae: 1327.2958
Epoch 10/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 1762813.0000 - mae: 841.5840 - val_loss: 2510709.7500 - val_mae: 1255.3016
Epoch 11/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 1660043.5000 - mae: 829.7453 - val_loss: 2331885.0000 - val_mae: 1183.8845
Epoch 12/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 1575198.8750 - mae: 828.2158 - val_loss: 2166954.2500 - val_mae: 1119.1547
Epoch 13/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 1500022.5000 - mae: 827.0732 - val_loss: 2016887.2500 - val_mae: 1069.0991
Epoch 14/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 1426503.1250 - mae: 823.1784 - val_loss: 1867501.5000 - val_mae: 1011.8815
Epoch 15/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 1299683.6250 - mae: 722.3347 - val_loss: 1713333.1250 - val_mae: 972.3826
Epoch 16/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 30ms/step - loss: 1154994.0000 - mae: 618.7450 - val_loss: 1543037.0000 - val_mae: 926.2453
Epoch 17/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 1038605.5000 - mae: 573.8633 - val_loss: 1393292.8750 - val_mae: 878.9207
Epoch 18/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 941995.3750 - mae: 541.0815 - val_loss: 1279178.3750 - val_mae: 859.0885
Epoch 19/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 847668.3125 - mae: 512.0916 - val_loss: 1166832.5000 - val_mae: 822.6744
Epoch 20/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 30ms/step - loss: 765523.4375 - mae: 478.0064 - val_loss: 1067430.0000 - val_mae: 789.5954
Epoch 21/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 679547.5625 - mae: 445.2599 - val_loss: 957619.5000 - val_mae: 744.0721
Epoch 22/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 602944.9375 - mae: 413.0269 - val_loss: 818323.9375 - val_mae: 668.1685
Epoch 23/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 531529.7500 - mae: 380.7014 - val_loss: 726592.3125 - val_mae: 629.9191
Epoch 24/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 470810.7812 - mae: 353.6149 - val_loss: 646548.1250 - val_mae: 597.1335
Epoch 25/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 422396.9688 - mae: 330.9814 - val_loss: 593654.4375 - val_mae: 580.5662
Epoch 26/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 383167.6562 - mae: 312.1741 - val_loss: 815057.8125 - val_mae: 777.9205
Epoch 27/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 339482.5312 - mae: 294.6912 - val_loss: 497505.8125 - val_mae: 542.1161
Epoch 28/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 294637.9375 - mae: 272.3738 - val_loss: 447383.1250 - val_mae: 519.5825
Epoch 29/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 259094.3281 - mae: 254.9653 - val_loss: 416463.9688 - val_mae: 509.2733
Epoch 30/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 247260.4375 - mae: 248.1459 - val_loss: 391434.3438 - val_mae: 501.6839
Epoch 31/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 222823.9375 - mae: 238.5999 - val_loss: 377306.8750 - val_mae: 500.6497
Epoch 32/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 208759.0625 - mae: 231.2130 - val_loss: 329739.3125 - val_mae: 469.4560
Epoch 33/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 192123.2500 - mae: 220.6700 - val_loss: 276651.2188 - val_mae: 423.9404
Epoch 34/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 160960.7969 - mae: 201.1895 - val_loss: 354985.7500 - val_mae: 492.3128
Epoch 35/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 154782.1250 - mae: 197.4256 - val_loss: 255843.9219 - val_mae: 413.8545
Epoch 36/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 137311.6250 - mae: 188.8423 - val_loss: 245857.9844 - val_mae: 411.0133
Epoch 37/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 128557.5469 - mae: 180.1665 - val_loss: 256822.3438 - val_mae: 422.8546
Epoch 38/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 117782.3828 - mae: 174.0751 - val_loss: 304245.0312 - val_mae: 451.5536
Epoch 39/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 110999.7500 - mae: 170.7352 - val_loss: 368016.8438 - val_mae: 496.5690
Epoch 40/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 102928.3047 - mae: 161.0279 - val_loss: 265141.2812 - val_mae: 415.6199
Epoch 41/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 93549.9844 - mae: 157.0971 - val_loss: 380925.7188 - val_mae: 499.5740
Epoch 42/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 29ms/step - loss: 89523.9141 - mae: 151.6565 - val_loss: 290546.8438 - val_mae: 431.7890
Epoch 43/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 29ms/step - loss: 84576.1719 - mae: 146.5363 - val_loss: 234452.5312 - val_mae: 392.7813
Epoch 44/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 29ms/step - loss: 79062.6719 - mae: 144.6763 - val_loss: 318773.0938 - val_mae: 473.9839
Epoch 45/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 37ms/step - loss: 74195.3359 - mae: 137.4414 - val_loss: 189716.8281 - val_mae: 353.3694
Epoch 46/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 70665.1094 - mae: 131.4561 - val_loss: 226760.7188 - val_mae: 398.2126
Epoch 47/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 68571.4297 - mae: 131.6020 - val_loss: 306523.2500 - val_mae: 456.8497
Epoch 48/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 67399.9766 - mae: 135.5819 - val_loss: 277588.0625 - val_mae: 445.4522
Epoch 49/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 64768.8164 - mae: 130.9539 - val_loss: 228909.5469 - val_mae: 396.2787
Epoch 50/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 58053.9648 - mae: 125.8228 - val_loss: 197784.5781 - val_mae: 372.3556
Epoch 51/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 57021.4570 - mae: 124.4864 - val_loss: 229473.3750 - val_mae: 395.5915
Epoch 52/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 54635.4062 - mae: 125.6660 - val_loss: 177188.8906 - val_mae: 346.7983
Epoch 53/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 51880.2305 - mae: 119.0238 - val_loss: 237444.3750 - val_mae: 396.7950
Epoch 54/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 54054.0312 - mae: 121.9408 - val_loss: 208256.1562 - val_mae: 376.9667
Epoch 55/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 49565.2344 - mae: 120.0810 - val_loss: 242257.8438 - val_mae: 403.4996
Epoch 56/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 51047.7656 - mae: 122.1260 - val_loss: 273725.8750 - val_mae: 435.7174
Epoch 57/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 56010.3398 - mae: 126.8080 - val_loss: 256030.0156 - val_mae: 417.1405
Epoch 58/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 51146.1250 - mae: 123.4080 - val_loss: 223709.4219 - val_mae: 378.7395
Epoch 59/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 47266.3516 - mae: 115.8123 - val_loss: 241724.2188 - val_mae: 402.8148
Epoch 60/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 49234.5781 - mae: 117.4823 - val_loss: 246675.7500 - val_mae: 406.1888
Epoch 61/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 49374.4102 - mae: 119.7964 - val_loss: 232489.8281 - val_mae: 380.9472
Epoch 62/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 48606.0039 - mae: 118.5889 - val_loss: 236354.6719 - val_mae: 386.7654
Epoch 62: early stopping
Restoring model weights from the end of the best epoch: 52.
 
12/12 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step 

--- Run Finished ---
Test Set R-squared (R²): -0.0285
Model saved to models/volatility_lstm_optimized/20250818_003539/best_volatility_model.h5

--- Running Experiment 15/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1d",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 12,
  "SEQUENCE_LENGTH": 72,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1d:  58%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉                                                                                                 | 2925/5000 [00:01<00:00, 2771.33it/s]

Epoch 1/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 5s 66ms/step - loss: 2678840.2500 - mae: 1191.5608 - val_loss: 4211665.0000 - val_mae: 1806.3435
Epoch 2/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 2623879.5000 - mae: 1166.9694 - val_loss: 4113915.5000 - val_mae: 1779.0631
Epoch 3/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 2553296.0000 - mae: 1136.0842 - val_loss: 3992941.7500 - val_mae: 1744.7319
Epoch 4/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 37ms/step - loss: 2465390.0000 - mae: 1097.4791 - val_loss: 3839740.5000 - val_mae: 1700.2614
Epoch 5/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 2358605.5000 - mae: 1049.8116 - val_loss: 3655327.2500 - val_mae: 1645.1370
Epoch 6/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 2240046.0000 - mae: 999.0739 - val_loss: 3456263.0000 - val_mae: 1583.4810
Epoch 7/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 2115866.7500 - mae: 946.8563 - val_loss: 3244555.5000 - val_mae: 1515.1583
Epoch 8/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 1987462.1250 - mae: 900.2205 - val_loss: 3024830.0000 - val_mae: 1440.8257
Epoch 9/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 39ms/step - loss: 1864069.6250 - mae: 866.4954 - val_loss: 2806611.5000 - val_mae: 1362.9967
Epoch 10/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 1752294.1250 - mae: 847.6505 - val_loss: 2596085.7500 - val_mae: 1283.4470
Epoch 11/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 3s 46ms/step - loss: 1642517.1250 - mae: 837.7740 - val_loss: 2398310.5000 - val_mae: 1206.9355
Epoch 12/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 1552866.5000 - mae: 834.1406 - val_loss: 2215314.2500 - val_mae: 1141.7277
Epoch 13/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 1476169.1250 - mae: 834.1546 - val_loss: 2052943.1250 - val_mae: 1092.5900
Epoch 14/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 1415544.7500 - mae: 841.2455 - val_loss: 1911615.0000 - val_mae: 1053.3677
Epoch 15/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 36ms/step - loss: 1365552.6250 - mae: 848.0567 - val_loss: 1790875.3750 - val_mae: 1019.0120
Epoch 16/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 1336047.6250 - mae: 858.8204 - val_loss: 1690073.6250 - val_mae: 988.3900
Epoch 17/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 30ms/step - loss: 1312111.1250 - mae: 867.2775 - val_loss: 1607644.2500 - val_mae: 961.7626
Epoch 18/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 1252761.7500 - mae: 827.1125 - val_loss: 1536136.7500 - val_mae: 939.9282
Epoch 19/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 983083.6875 - mae: 573.9089 - val_loss: 1342275.6250 - val_mae: 859.2330
Epoch 20/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 867680.7500 - mae: 517.1834 - val_loss: 1160706.2500 - val_mae: 777.4060
Epoch 21/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 759100.0000 - mae: 476.3356 - val_loss: 1008992.7500 - val_mae: 709.8650
Epoch 22/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 659890.1250 - mae: 439.3938 - val_loss: 876851.6875 - val_mae: 663.6415
Epoch 23/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 571755.6875 - mae: 399.9221 - val_loss: 764515.8750 - val_mae: 618.4544
Epoch 24/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 36ms/step - loss: 492928.0938 - mae: 363.9368 - val_loss: 654094.8750 - val_mae: 565.3116
Epoch 25/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 438466.2500 - mae: 340.9391 - val_loss: 576074.8750 - val_mae: 537.0375
Epoch 26/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 37ms/step - loss: 383582.6562 - mae: 313.6447 - val_loss: 508004.6250 - val_mae: 510.1109
Epoch 27/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 333779.9062 - mae: 293.1273 - val_loss: 457350.3438 - val_mae: 488.0334
Epoch 28/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 298493.0938 - mae: 273.4871 - val_loss: 435181.5625 - val_mae: 510.2791
Epoch 29/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 266246.0938 - mae: 258.6087 - val_loss: 420289.1562 - val_mae: 523.2189
Epoch 30/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 248687.3906 - mae: 250.7036 - val_loss: 396042.2812 - val_mae: 510.5950
Epoch 31/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 225328.3750 - mae: 240.6063 - val_loss: 376244.0938 - val_mae: 507.9464
Epoch 32/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 189893.7656 - mae: 218.3231 - val_loss: 359437.9688 - val_mae: 507.9661
Epoch 33/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 174604.8750 - mae: 210.4835 - val_loss: 486627.8125 - val_mae: 619.1766
Epoch 34/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 160509.1719 - mae: 200.8999 - val_loss: 411828.4062 - val_mae: 562.9194
Epoch 35/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 145942.5000 - mae: 194.5408 - val_loss: 393007.1875 - val_mae: 551.7208
Epoch 36/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 135561.6250 - mae: 188.2449 - val_loss: 537152.2500 - val_mae: 639.3340
Epoch 37/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 120503.8672 - mae: 182.2668 - val_loss: 348809.2188 - val_mae: 487.2672
Epoch 38/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 112840.2578 - mae: 171.3548 - val_loss: 330355.5938 - val_mae: 509.1982
Epoch 39/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 100811.7500 - mae: 162.5067 - val_loss: 378466.0625 - val_mae: 534.2117
Epoch 40/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 94710.1953 - mae: 160.8022 - val_loss: 385564.5938 - val_mae: 562.7800
Epoch 41/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 89734.1719 - mae: 153.3681 - val_loss: 381040.0000 - val_mae: 549.0837
Epoch 42/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 40ms/step - loss: 84547.4297 - mae: 154.1293 - val_loss: 428259.0000 - val_mae: 592.7944
Epoch 43/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 77924.0469 - mae: 146.6713 - val_loss: 328517.8125 - val_mae: 506.2554
Epoch 44/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 74219.3750 - mae: 143.8915 - val_loss: 352013.6250 - val_mae: 506.8292
Epoch 45/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 72695.9062 - mae: 139.9916 - val_loss: 323900.1250 - val_mae: 505.1817
Epoch 46/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 66059.6484 - mae: 135.7229 - val_loss: 294544.4062 - val_mae: 463.3164
Epoch 47/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 65430.3086 - mae: 134.4940 - val_loss: 376396.1250 - val_mae: 536.5316
Epoch 48/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 36ms/step - loss: 63771.4492 - mae: 134.6401 - val_loss: 415567.1250 - val_mae: 566.1904
Epoch 49/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 59619.3672 - mae: 130.9996 - val_loss: 452135.0625 - val_mae: 609.9268
Epoch 50/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 58986.5352 - mae: 131.9950 - val_loss: 427836.0938 - val_mae: 589.5005
Epoch 51/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 56107.5352 - mae: 128.8531 - val_loss: 465574.7188 - val_mae: 613.7459
Epoch 52/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 53076.6797 - mae: 124.5634 - val_loss: 426852.5312 - val_mae: 573.0768
Epoch 53/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 53298.5586 - mae: 128.6865 - val_loss: 399217.5000 - val_mae: 553.4986
Epoch 54/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 29ms/step - loss: 52651.9492 - mae: 126.3178 - val_loss: 402564.7812 - val_mae: 544.4910
Epoch 55/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 50066.1562 - mae: 121.7484 - val_loss: 439238.2500 - val_mae: 579.3749
Epoch 56/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 49482.5586 - mae: 121.7800 - val_loss: 390048.6562 - val_mae: 529.9948
Epoch 56: early stopping
Restoring model weights from the end of the best epoch: 46.
 
11/11 ━━━━━━━━━━━━━━━━━━━━ 1s 34ms/step 

--- Run Finished ---
Test Set R-squared (R²): 0.1621
Model saved to models/volatility_lstm_optimized/20250818_003730/best_volatility_model.h5

--- Running Experiment 16/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1d",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 24,
  "SEQUENCE_LENGTH": 24,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1d:  58%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉                                                                                                 | 2925/5000 [00:01<00:00, 2905.18it/s]

Epoch 1/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 4s 40ms/step - loss: 2625894.2500 - mae: 1176.3634 - val_loss: 3799818.7500 - val_mae: 1691.7677
Epoch 2/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 2569810.5000 - mae: 1151.0391 - val_loss: 3722969.2500 - val_mae: 1668.8422
Epoch 3/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 2512057.2500 - mae: 1125.5145 - val_loss: 3625689.7500 - val_mae: 1639.4359
Epoch 4/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 2438895.5000 - mae: 1092.4598 - val_loss: 3505377.7500 - val_mae: 1602.3221
Epoch 5/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 2351005.5000 - mae: 1052.9541 - val_loss: 3365733.0000 - val_mae: 1558.1370
Epoch 6/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 2254589.2500 - mae: 1009.8347 - val_loss: 3210077.7500 - val_mae: 1507.3606
Epoch 7/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 2148905.2500 - mae: 964.9232 - val_loss: 3042667.2500 - val_mae: 1450.7671
Epoch 8/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 2041580.5000 - mae: 920.1107 - val_loss: 2868724.0000 - val_mae: 1389.5258
Epoch 9/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1932746.8750 - mae: 879.3639 - val_loss: 2690284.2500 - val_mae: 1323.7604
Epoch 10/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 1827178.6250 - mae: 850.9872 - val_loss: 2512919.7500 - val_mae: 1254.9811
Epoch 11/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 1724709.7500 - mae: 833.0503 - val_loss: 2342165.5000 - val_mae: 1184.9991
Epoch 12/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 1634041.2500 - mae: 824.8256 - val_loss: 2180571.5000 - val_mae: 1116.0648
Epoch 13/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 1550433.3750 - mae: 821.4293 - val_loss: 2029627.1250 - val_mae: 1054.0698
Epoch 14/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 1479713.3750 - mae: 820.7926 - val_loss: 1893155.0000 - val_mae: 1005.4031
Epoch 15/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 1425734.1250 - mae: 826.1232 - val_loss: 1772958.7500 - val_mae: 969.2801
Epoch 16/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 30ms/step - loss: 1372102.5000 - mae: 831.3702 - val_loss: 1667297.2500 - val_mae: 939.0295
Epoch 17/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 24ms/step - loss: 1269080.3750 - mae: 745.3947 - val_loss: 1552957.1250 - val_mae: 906.8242
Epoch 18/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 1101585.5000 - mae: 602.3861 - val_loss: 1405132.3750 - val_mae: 866.9516
Epoch 19/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 994878.0000 - mae: 563.5541 - val_loss: 1271468.8750 - val_mae: 828.3017
Epoch 20/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 895634.9375 - mae: 526.6592 - val_loss: 1158804.8750 - val_mae: 798.9015
Epoch 21/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 803749.1250 - mae: 491.8647 - val_loss: 1078191.0000 - val_mae: 792.0316
Epoch 22/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 722297.4375 - mae: 460.6129 - val_loss: 932971.6875 - val_mae: 703.9887
Epoch 23/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 650188.3750 - mae: 429.4406 - val_loss: 807905.8750 - val_mae: 639.4525
Epoch 24/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 573415.8125 - mae: 398.9100 - val_loss: 726362.1875 - val_mae: 605.3377
Epoch 25/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 519146.2188 - mae: 377.0699 - val_loss: 755473.3125 - val_mae: 680.2693
Epoch 26/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 451921.5000 - mae: 351.2746 - val_loss: 602415.7500 - val_mae: 566.4319
Epoch 27/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 414929.2500 - mae: 327.2047 - val_loss: 578312.7500 - val_mae: 563.8828
Epoch 28/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 362308.9062 - mae: 302.1591 - val_loss: 453925.2812 - val_mae: 477.6106
Epoch 29/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 324704.2188 - mae: 286.8070 - val_loss: 428482.2188 - val_mae: 474.7400
Epoch 30/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 293439.6562 - mae: 269.3289 - val_loss: 400938.4688 - val_mae: 466.9250
Epoch 31/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 263675.9062 - mae: 259.2578 - val_loss: 390610.5938 - val_mae: 474.3417
Epoch 32/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 244394.2188 - mae: 248.2792 - val_loss: 438196.2500 - val_mae: 535.3287
Epoch 33/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 226054.4375 - mae: 239.2472 - val_loss: 355505.0938 - val_mae: 469.7645
Epoch 34/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 203015.6094 - mae: 223.1379 - val_loss: 344332.1875 - val_mae: 455.2846
Epoch 35/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 183278.8750 - mae: 214.8425 - val_loss: 328400.2188 - val_mae: 439.0390
Epoch 36/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 167715.9062 - mae: 204.1099 - val_loss: 397935.8438 - val_mae: 500.5459
Epoch 37/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 22ms/step - loss: 154897.2188 - mae: 200.4168 - val_loss: 366668.3125 - val_mae: 461.3867
Epoch 38/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 136949.5469 - mae: 186.6149 - val_loss: 357404.4688 - val_mae: 464.7728
Epoch 39/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 126672.1250 - mae: 180.8543 - val_loss: 384983.4688 - val_mae: 507.0201
Epoch 40/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 117919.7969 - mae: 175.2688 - val_loss: 366343.1250 - val_mae: 479.5378
Epoch 41/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 21ms/step - loss: 108263.4531 - mae: 163.4972 - val_loss: 371674.2188 - val_mae: 456.6079
Epoch 42/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 2s 28ms/step - loss: 101696.8906 - mae: 159.4646 - val_loss: 392088.7500 - val_mae: 494.6490
Epoch 43/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 92147.9453 - mae: 155.5266 - val_loss: 325524.4688 - val_mae: 449.0772
Epoch 44/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 91446.9453 - mae: 154.4183 - val_loss: 324156.2500 - val_mae: 431.2489
Epoch 45/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 77884.4531 - mae: 142.0464 - val_loss: 252707.0312 - val_mae: 397.0396
Epoch 46/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - loss: 72375.7734 - mae: 139.6701 - val_loss: 299013.1875 - val_mae: 435.3680
Epoch 47/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 20ms/step - loss: 70158.4297 - mae: 134.9734 - val_loss: 292701.0312 - val_mae: 433.3430
Epoch 48/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 64574.0469 - mae: 131.2597 - val_loss: 267796.6250 - val_mae: 402.2420
Epoch 49/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 68093.7891 - mae: 135.8151 - val_loss: 343126.1875 - val_mae: 479.7086
Epoch 50/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 65120.0586 - mae: 135.4951 - val_loss: 319856.2812 - val_mae: 448.1242
Epoch 51/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 61641.4648 - mae: 126.0279 - val_loss: 275729.5625 - val_mae: 411.9265
Epoch 52/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 59423.5938 - mae: 132.0629 - val_loss: 271023.5938 - val_mae: 400.7611
Epoch 53/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 75865.1328 - mae: 132.6061 - val_loss: 255579.0469 - val_mae: 380.2785
Epoch 54/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 51817.4609 - mae: 121.9766 - val_loss: 282655.9062 - val_mae: 436.1527
Epoch 55/100
59/59 ━━━━━━━━━━━━━━━━━━━━ 1s 19ms/step - loss: 51883.6094 - mae: 122.9513 - val_loss: 281978.1562 - val_mae: 413.7908
Epoch 55: early stopping
Restoring model weights from the end of the best epoch: 45.
 
12/12 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step 

--- Run Finished ---
Test Set R-squared (R²): -0.8624
Model saved to models/volatility_lstm_optimized/20250818_003928/best_volatility_model.h5

--- Running Experiment 17/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1d",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 24,
  "SEQUENCE_LENGTH": 48,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1d:  58%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉                                                                                                 | 2925/5000 [00:01<00:00, 2554.28it/s]
/opt/homebrew/Caskroom/miniconda/base/envs/crypto-trading-ai/lib/python3.10/site-packages/keras/src/layers/rnn/rnn.py:199: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.

58/58 ━━━━━━━━━━━━━━━━━━━━ 4s 42ms/step - loss: 2660041.5000 - mae: 1185.6606 - val_loss: 4007261.5000 - val_mae: 1746.3445
Epoch 2/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 2600866.2500 - mae: 1159.8131 - val_loss: 3915279.5000 - val_mae: 1719.7987
Epoch 3/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 2537836.5000 - mae: 1132.1791 - val_loss: 3812931.5000 - val_mae: 1689.7811
Epoch 4/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 2464680.0000 - mae: 1099.1755 - val_loss: 3690858.7500 - val_mae: 1653.2654
Epoch 5/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 2377731.2500 - mae: 1060.3379 - val_loss: 3549851.0000 - val_mae: 1610.0557
Epoch 6/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 2281293.0000 - mae: 1017.8871 - val_loss: 3392680.2500 - val_mae: 1560.4838
Epoch 7/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 2177419.0000 - mae: 973.7872 - val_loss: 3221591.5000 - val_mae: 1504.6663
Epoch 8/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 2070808.5000 - mae: 929.9227 - val_loss: 3045632.2500 - val_mae: 1445.0128
Epoch 9/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1963476.7500 - mae: 890.8862 - val_loss: 2866697.0000 - val_mae: 1381.7113
Epoch 10/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 1857963.2500 - mae: 861.9801 - val_loss: 2689087.7500 - val_mae: 1315.8713
Epoch 11/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 1760631.1250 - mae: 843.6831 - val_loss: 2516395.7500 - val_mae: 1248.5293
Epoch 12/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1668201.2500 - mae: 834.6251 - val_loss: 2349836.2500 - val_mae: 1180.9395
Epoch 13/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1586144.0000 - mae: 831.2204 - val_loss: 2195138.5000 - val_mae: 1119.4348
Epoch 14/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1517768.5000 - mae: 829.6437 - val_loss: 2054433.7500 - val_mae: 1070.9779
Epoch 15/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1455546.7500 - mae: 830.8763 - val_loss: 1926350.5000 - val_mae: 1034.4871
Epoch 16/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1404943.6250 - mae: 835.7659 - val_loss: 1813828.0000 - val_mae: 1005.5899
Epoch 17/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1363463.1250 - mae: 842.3748 - val_loss: 1718149.5000 - val_mae: 981.2576
Epoch 18/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1243432.6250 - mae: 729.0487 - val_loss: 1601350.2500 - val_mae: 949.4233
Epoch 19/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 1080019.8750 - mae: 595.2517 - val_loss: 1450456.2500 - val_mae: 903.8492
Epoch 20/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 976819.6250 - mae: 556.3069 - val_loss: 1320522.6250 - val_mae: 865.3764
Epoch 21/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 887010.8750 - mae: 523.6312 - val_loss: 1211528.3750 - val_mae: 836.6395
Epoch 22/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 802366.6875 - mae: 490.8642 - val_loss: 1110638.8750 - val_mae: 804.2946
Epoch 23/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 26ms/step - loss: 713450.8750 - mae: 454.1706 - val_loss: 1052349.6250 - val_mae: 800.6100
Epoch 24/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 643102.5000 - mae: 428.5804 - val_loss: 954245.4375 - val_mae: 762.9968
Epoch 25/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 568330.3125 - mae: 394.4337 - val_loss: 891276.0000 - val_mae: 750.3688
Epoch 26/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 508940.8438 - mae: 366.9277 - val_loss: 910662.6250 - val_mae: 789.8262
Epoch 27/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 451875.2812 - mae: 342.0363 - val_loss: 917726.7500 - val_mae: 809.6459
Epoch 28/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 412279.9062 - mae: 324.1351 - val_loss: 837026.3125 - val_mae: 770.0099
Epoch 29/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 377351.0938 - mae: 308.4594 - val_loss: 977753.7500 - val_mae: 854.8463
Epoch 30/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 336653.4062 - mae: 290.3951 - val_loss: 1014871.1875 - val_mae: 879.4827
Epoch 31/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 304712.5000 - mae: 274.6235 - val_loss: 822222.8125 - val_mae: 782.7476
Epoch 32/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 277740.6250 - mae: 262.8826 - val_loss: 804525.4375 - val_mae: 773.1720
Epoch 33/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 251723.7812 - mae: 249.9232 - val_loss: 506747.1250 - val_mae: 598.5163
Epoch 34/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 30ms/step - loss: 234196.1250 - mae: 240.7297 - val_loss: 627938.1250 - val_mae: 693.1765
Epoch 35/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 205770.2344 - mae: 224.3102 - val_loss: 664020.5625 - val_mae: 722.5929
Epoch 36/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 193681.1562 - mae: 217.8573 - val_loss: 555521.4375 - val_mae: 655.1886
Epoch 37/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 174413.2344 - mae: 206.3555 - val_loss: 604986.8750 - val_mae: 702.1377
Epoch 38/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 162835.9219 - mae: 196.5206 - val_loss: 516309.9688 - val_mae: 640.6057
Epoch 39/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 144080.6875 - mae: 183.3821 - val_loss: 541807.0000 - val_mae: 657.1384
Epoch 40/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 136908.7188 - mae: 177.3122 - val_loss: 619495.3750 - val_mae: 699.2835
Epoch 41/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 27ms/step - loss: 125766.1875 - mae: 173.2366 - val_loss: 634107.0000 - val_mae: 700.0056
Epoch 42/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 121588.6406 - mae: 175.4539 - val_loss: 619064.6250 - val_mae: 677.4178
Epoch 43/100
58/58 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 111957.7812 - mae: 164.3083 - val_loss: 640687.3125 - val_mae: 688.6854
Epoch 43: early stopping
Restoring model weights from the end of the best epoch: 33.
 
12/12 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step 

--- Run Finished ---
Test Set R-squared (R²): -1.7021
Model saved to models/volatility_lstm_optimized/20250818_004049/best_volatility_model.h5

--- Running Experiment 18/18 ---
--- Starting Training Run with Config ---
{
  "SYMBOL": "BTC/USDT",
  "TIMEFRAME": "1d",
  "LIMIT": 5000,
  "REGRESSION_HORIZON": 24,
  "SEQUENCE_LENGTH": 72,
  "TEST_FRAC": 0.15,
  "VAL_FRAC": 0.15,
  "RANDOM_SEED": 42,
  "SAVE_DIR_BASE": "models/volatility_lstm_optimized"
}
Fetching BTC/USDT 1d:  58%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉                                                                                                 | 2925/5000 [00:01<00:00, 2710.52it/s]

Epoch 1/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 4s 40ms/step - loss: 2688683.0000 - mae: 1195.1692 - val_loss: 4251837.0000 - val_mae: 1820.2214
Epoch 2/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 2624327.0000 - mae: 1166.2472 - val_loss: 4146210.2500 - val_mae: 1790.9568
Epoch 3/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 30ms/step - loss: 2550512.7500 - mae: 1133.8539 - val_loss: 4019260.2500 - val_mae: 1755.1575
Epoch 4/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 2461694.0000 - mae: 1094.2306 - val_loss: 3865288.0000 - val_mae: 1710.7350
Epoch 5/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 2359546.2500 - mae: 1049.2433 - val_loss: 3689775.2500 - val_mae: 1658.6438
Epoch 6/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 2244923.7500 - mae: 1000.2809 - val_loss: 3495843.7500 - val_mae: 1599.1158
Epoch 7/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 2122319.5000 - mae: 949.7827 - val_loss: 3288182.5000 - val_mae: 1532.8116
Epoch 8/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 2002518.7500 - mae: 905.9847 - val_loss: 3076165.5000 - val_mae: 1462.0184
Epoch 9/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 1884471.7500 - mae: 874.2087 - val_loss: 2865216.7500 - val_mae: 1388.0028
Epoch 10/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 1769277.5000 - mae: 853.5970 - val_loss: 2659127.0000 - val_mae: 1311.6720
Epoch 11/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 1669760.1250 - mae: 842.9065 - val_loss: 2463697.0000 - val_mae: 1236.9333
Epoch 12/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 1580087.8750 - mae: 839.2401 - val_loss: 2282281.5000 - val_mae: 1170.4060
Epoch 13/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 1502010.6250 - mae: 838.7649 - val_loss: 2119766.5000 - val_mae: 1118.1891
Epoch 14/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 1433413.8750 - mae: 839.8871 - val_loss: 1973689.6250 - val_mae: 1076.7179
Epoch 15/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 30ms/step - loss: 1384354.8750 - mae: 836.7298 - val_loss: 1848020.1250 - val_mae: 1040.7615
Epoch 16/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 30ms/step - loss: 1197516.3750 - mae: 660.7816 - val_loss: 1669357.1250 - val_mae: 985.3144
Epoch 17/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 1056216.3750 - mae: 587.8587 - val_loss: 1491010.7500 - val_mae: 925.2371
Epoch 18/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 946602.0625 - mae: 549.9367 - val_loss: 1341889.1250 - val_mae: 876.7217
Epoch 19/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 849860.6250 - mae: 514.0319 - val_loss: 1216776.1250 - val_mae: 839.7142
Epoch 20/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 759878.1875 - mae: 480.5696 - val_loss: 1112340.8750 - val_mae: 806.5922
Epoch 21/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 674933.9375 - mae: 444.8617 - val_loss: 1034843.0000 - val_mae: 792.8467
Epoch 22/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 600376.1875 - mae: 410.5064 - val_loss: 964892.8125 - val_mae: 770.4539
Epoch 23/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 528413.0000 - mae: 383.8600 - val_loss: 779586.0000 - val_mae: 660.0502
Epoch 24/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 464616.9375 - mae: 356.4153 - val_loss: 740166.1875 - val_mae: 671.4449
Epoch 25/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 408110.3125 - mae: 328.4873 - val_loss: 706506.2500 - val_mae: 664.1744
Epoch 26/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 366665.6875 - mae: 310.8093 - val_loss: 780075.7500 - val_mae: 746.5964
Epoch 27/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 3s 56ms/step - loss: 326781.0312 - mae: 290.5926 - val_loss: 691313.3750 - val_mae: 694.3243
Epoch 28/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 37ms/step - loss: 298871.1562 - mae: 280.1389 - val_loss: 540124.7500 - val_mae: 606.8676
Epoch 29/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 266874.3438 - mae: 263.2767 - val_loss: 598414.4375 - val_mae: 664.3613
Epoch 30/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 245579.7969 - mae: 253.1970 - val_loss: 596805.6875 - val_mae: 658.4991
Epoch 31/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 219887.9688 - mae: 237.8381 - val_loss: 526817.3125 - val_mae: 623.5918
Epoch 32/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 36ms/step - loss: 200050.3594 - mae: 226.3463 - val_loss: 466296.2500 - val_mae: 573.5569
Epoch 33/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 186628.3906 - mae: 217.8957 - val_loss: 671046.8125 - val_mae: 723.6655
Epoch 34/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 158092.7500 - mae: 200.8939 - val_loss: 512803.5625 - val_mae: 628.8237
Epoch 35/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 145384.2500 - mae: 194.5370 - val_loss: 662639.5625 - val_mae: 706.8418
Epoch 36/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 129109.7266 - mae: 179.8628 - val_loss: 568444.3125 - val_mae: 650.7610
Epoch 37/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 122801.0938 - mae: 178.4005 - val_loss: 511395.1562 - val_mae: 614.6744
Epoch 38/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 113816.9141 - mae: 173.2799 - val_loss: 672074.0625 - val_mae: 700.0553
Epoch 39/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 39ms/step - loss: 104976.1250 - mae: 163.4793 - val_loss: 553746.1250 - val_mae: 632.3406
Epoch 40/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 35ms/step - loss: 96824.7344 - mae: 158.6167 - val_loss: 586471.5000 - val_mae: 646.1990
Epoch 41/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 89839.8906 - mae: 152.1833 - val_loss: 457908.1875 - val_mae: 566.3108
Epoch 42/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 33ms/step - loss: 84494.5938 - mae: 155.4455 - val_loss: 770663.9375 - val_mae: 760.7481
Epoch 43/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 83779.5781 - mae: 151.5023 - val_loss: 770517.6250 - val_mae: 745.2032
Epoch 44/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 81684.5625 - mae: 148.3633 - val_loss: 636635.5625 - val_mae: 671.3459
Epoch 45/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 34ms/step - loss: 70811.7266 - mae: 137.3588 - val_loss: 753369.4375 - val_mae: 718.0681
Epoch 46/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 71294.7500 - mae: 138.8867 - val_loss: 520327.5938 - val_mae: 611.7220
Epoch 47/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 38ms/step - loss: 64116.6523 - mae: 133.9113 - val_loss: 659169.1250 - val_mae: 690.1655
Epoch 48/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 67050.5156 - mae: 140.2124 - val_loss: 1123589.0000 - val_mae: 900.0807
Epoch 49/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 63560.4922 - mae: 134.2619 - val_loss: 918653.8750 - val_mae: 806.3436
Epoch 50/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 32ms/step - loss: 62878.0039 - mae: 131.8994 - val_loss: 680088.8125 - val_mae: 677.1176
Epoch 51/100
57/57 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 59128.1875 - mae: 129.4784 - val_loss: 817533.8125 - val_mae: 721.7878
Epoch 51: early stopping
Restoring model weights from the end of the best epoch: 41.
 
11/11 ━━━━━━━━━━━━━━━━━━━━ 1s 29ms/step 

--- Run Finished ---
Test Set R-squared (R²): -0.2588
Model saved to models/volatility_lstm_optimized/20250818_004201/best_volatility_model.h5


--- Optimization Finished ---
All Experiment Results:
      SYMBOL TIMEFRAME  LIMIT  REGRESSION_HORIZON  SEQUENCE_LENGTH  TEST_FRAC  VAL_FRAC  RANDOM_SEED                     SAVE_DIR_BASE  r2_score
1   BTC/USDT        1h   5000                  12               48       0.15      0.15           42  models/volatility_lstm_optimized  0.421963
14  BTC/USDT        1d   5000                  12               72       0.15      0.15           42  models/volatility_lstm_optimized  0.162133
12  BTC/USDT        1d   5000                  12               24       0.15      0.15           42  models/volatility_lstm_optimized  0.102593
4   BTC/USDT        1h   5000                  24               48       0.15      0.15           42  models/volatility_lstm_optimized -0.004642
2   BTC/USDT        1h   5000                  12               72       0.15      0.15           42  models/volatility_lstm_optimized -0.025723
0   BTC/USDT        1h   5000                  12               24       0.15      0.15           42  models/volatility_lstm_optimized -0.026941
13  BTC/USDT        1d   5000                  12               48       0.15      0.15           42  models/volatility_lstm_optimized -0.028510
5   BTC/USDT        1h   5000                  24               72       0.15      0.15           42  models/volatility_lstm_optimized -0.047822
3   BTC/USDT        1h   5000                  24               24       0.15      0.15           42  models/volatility_lstm_optimized -0.075849
17  BTC/USDT        1d   5000                  24               72       0.15      0.15           42  models/volatility_lstm_optimized -0.258831
15  BTC/USDT        1d   5000                  24               24       0.15      0.15           42  models/volatility_lstm_optimized -0.862416
11  BTC/USDT        4h   5000                  24               72       0.15      0.15           42  models/volatility_lstm_optimized -1.360770
16  BTC/USDT        1d   5000                  24               48       0.15      0.15           42  models/volatility_lstm_optimized -1.702089
9   BTC/USDT        4h   5000                  24               24       0.15      0.15           42  models/volatility_lstm_optimized -3.404261
8   BTC/USDT        4h   5000                  12               72       0.15      0.15           42  models/volatility_lstm_optimized -3.518187
6   BTC/USDT        4h   5000                  12               24       0.15      0.15           42  models/volatility_lstm_optimized -3.707107
10  BTC/USDT        4h   5000                  24               48       0.15      0.15           42  models/volatility_lstm_optimized -3.811710
7   BTC/USDT        4h   5000                  12               48       0.15      0.15           42  models/volatility_lstm_optimized -5.017023

Best Performing Configuration:
SYMBOL                                        BTC/USDT
TIMEFRAME                                           1h
LIMIT                                             5000
REGRESSION_HORIZON                                  12
SEQUENCE_LENGTH                                     48
TEST_FRAC                                         0.15
VAL_FRAC                                          0.15
RANDOM_SEED                                         42
SAVE_DIR_BASE         models/volatility_lstm_optimized
r2_score                                      0.421963
Name: 1, dtype: object