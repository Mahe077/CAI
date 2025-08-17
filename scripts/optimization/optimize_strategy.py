# scripts/optimization/optimize_strategy.py
import itertools
import pandas as pd
from scripts.training.train_volatility_forecaster import run_training_pipeline

def main():
    # --- Define the grid of parameters to search ---
    param_grid = {
        "SYMBOL": ["BTC/USDT"],
        "TIMEFRAME": ['1h', '4h', '1d'],
        "LIMIT": [5000],
        "REGRESSION_HORIZON": [12, 24],
        "SEQUENCE_LENGTH": [24, 48, 72],
        "TEST_FRAC": [0.15],
        "VAL_FRAC": [0.15],
        "RANDOM_SEED": [42],
        "SAVE_DIR_BASE": ["models/volatility_lstm_optimized"]
    }

    # Create a list of all parameter combinations
    keys, values = zip(*param_grid.items())
    experiments = [dict(zip(keys, v)) for v in itertools.product(*values)]

    print(f"Starting optimization process for {len(experiments)} experiments...")

    results = []

    for i, config in enumerate(experiments):
        print(f"\n--- Running Experiment {i+1}/{len(experiments)} ---")
        try:
            r2_score = run_training_pipeline(config)
            results.append({
                **config,
                "r2_score": r2_score
            })
        except Exception as e:
            print(f"!!! Experiment {i+1} failed with error: {e} !!!")
            results.append({
                **config,
                "r2_score": "ERROR"
            })

    # --- Report Results ---
    print("\n\n--- Optimization Finished ---")
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values(by="r2_score", ascending=False)

    print("All Experiment Results:")
    print(results_df.to_string())

    print("\nBest Performing Configuration:")
    print(results_df.iloc[0])

if __name__ == "__main__":
    main()
