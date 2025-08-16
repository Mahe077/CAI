#!/bin/bash

# Activate the Python virtual environment
source ../venv/bin/activate

# Fetch the latest data
python fetch_data.py

# Run data preprocessing
python ../src/data/preprocessing.py

# Execute feature engineering
python ../src/features/engineering.py

# Train the model
python ../src/models/train.py

# Run backtesting
python ../src/backtest/backtester.py

# Log the experiment results
python ../src/experiments/tracker.py

# Deactivate the virtual environment
deactivate