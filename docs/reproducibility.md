# Reproducibility

This document outlines the steps to reproduce the results of this project.

## Environment Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/crypto-trading-ai-research.git
    cd crypto-trading-ai-research
    ```

2.  **Create and activate the Conda environment:**
    ```bash
    conda env create -f environment.yml
    conda activate crypto-trading-ai
    ```

## Data Fetching

To fetch the data, run the `fetch_data.py` script with the desired data source and parameters. For example:

```bash
python scripts/fetch_data.py --source coingecko --symbol BTC-USD --start 2020-01-01 --end 2024-12-31
```

## Seed Settings

To ensure reproducibility of the modeling results, we use a fixed seed for all random number generators. The seed is set in the `configs/default.yaml` file.

```yaml
project:
  seed: 42
```
