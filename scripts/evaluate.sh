#!/bin/bash

# Evaluate the results of the experiments

# Check if results directory exists
RESULTS_DIR="../experiments/experiment_YYYY-MM-DD_id"
if [ ! -d "$RESULTS_DIR" ]; then
  echo "Results directory does not exist. Please check the path."
  exit 1
fi

# Load configuration
CONFIG_FILE="$RESULTS_DIR/config.yaml"
if [ ! -f "$CONFIG_FILE" ]; then
  echo "Configuration file not found!"
  exit 1
fi

# Load results
RESULTS_FILE="$RESULTS_DIR/results.csv"
if [ ! -f "$RESULTS_FILE" ]; then
  echo "Results file not found!"
  exit 1
fi

# Evaluate the results using Python script
python3 -c "
import pandas as pd
import yaml

# Load configuration
with open('$CONFIG_FILE', 'r') as file:
    config = yaml.safe_load(file)

# Load results
results = pd.read_csv('$RESULTS_FILE')

# Perform evaluation (this is a placeholder for actual evaluation logic)
print('Evaluation Results:')
print(results.describe())  # Example: summary statistics of results
"

echo "Evaluation completed."