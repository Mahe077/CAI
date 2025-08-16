# Crypto Trading AI — Detailed Phase Plan & Execution Checklist

This document is the canonical, updatable plan for the project. Use the checkboxes to mark progress. Each line is an actionable step (smallest unit you can complete and check off). Add dates/notes after completion.

## Quick start (Mac)
- Create venv:
  - python3 -m venv .venv
  - source .venv/bin/activate
  - pip install -r requirements.txt
- Run tests: pytest -q
- Run data fetch (example): 
  - For CoinGecko:
      python scripts/fetch_data.py --source coingecko --symbol BTC-USD --start 2020-01-01 --end 2024-12-31
  - For Binance (once you've implemented the fetching logic):
      python scripts/fetch_data.py --source binance --symbol BTCUSDT --start 2020-01-01 --end 2024-12-31
- Launch notebooks: jupyter lab

---

## Phase 0 — Project Setup & Reproducibility (Goal: reproducible baseline)
- [ ] Initialize repository, add LICENSE, CODE_OF_CONDUCT, CONTRIBUTING.md
- [ ] Define branch strategy (main/dev/feature/*)
- [ ] Create environment files
  - [ ] requirements.txt
  - [ ] environment.yml
- [ ] Add pre-commit hooks (black, isort, flake8)
- [ ] Add CI pipeline skeleton (GitHub Actions: tests, lint)
- [ ] Add reproducibility.md with exact commands and seed settings

Estimated time: 1–2 days

---

## Phase 1 — Data Collection & Storage (Goal: reliable raw dataset)
- [x] Identify and list primary data sources (exchange APIs, CCXT, CoinGecko, Kaggle)
- [x] Implement scripts/fetch_data.py
  - [ ] CLI args: symbols, timeframe, start, end, out-path
  - [ ] Retry/backoff and rate-limit handling
  - [ ] Save raw CSV/Parquet to data/raw/{exchange}/{symbol}/{YYYY-MM-DD}.parquet
- [ ] Add metadata files (data/raw/_README.md, data/schema.json)
- [ ] Add automated daily fetch cron/script (scripts/sync_data.sh)
- [ ] Validate raw files (schema and checksum)

Estimated time: 2–4 days

---

## Phase 2 — EDA & Data Quality (Goal: understand data & quality issues)
- [ ] Create notebook: notebooks/01-data-exploration.ipynb
  - [ ] Load sample symbols
  - [ ] Check missing data, duplicates, time alignment, timezone issues
  - [ ] Visualize price, volume, volatility, gaps
  - [ ] Save EDA notebook notes and plots to docs/eda/
- [ ] Implement basic validators in src/data/validator.py
  - [ ] ensure time continuity, no negative volumes, expected column types
- [ ] Generate a one-page data quality report (docs/data_quality.md)

Estimated time: 2–3 days

---

## Phase 3 — Preprocessing & Feature Engineering (Goal: stable feature pipeline)
- [ ] Design processing contract: inputs, outputs, expected scalers, imputation strategy
- [ ] Implement src/data/preprocessing.py
  - [ ] timezone normalization, resampling (1m/5m/1h), forward-fill/backfill policies
  - [ ] outlier handling (winsorize or clip)
- [ ] Implement technical indicators in src/features/engineering.py
  - [ ] basic: SMA, EMA, RSI, MACD, Bollinger Bands, ATR, OBV
  - [ ] derived: returns, rolling-volatility, momentum, liquidity features
- [ ] Create feature store layout: data/processed/features/{symbol}/{timeframe}.parquet
- [ ] Notebook: notebooks/02-feature-engineering.ipynb — visualize feature distributions and correlation matrix
- [ ] Add feature selection checklist: correlation threshold, importance-based pruning

Estimated time: 4–7 days

---

## Phase 4 — Modeling & Validation (Goal: baseline models + robust validation)
- [ ] Define prediction task(s)
  - [ ] classification: up/down in horizon H
  - [ ] regression: future log-return
  - [ ] multi-horizon experiments
- [ ] Implement model interfaces in src/models/model.py
  - [ ] sklearn-compatible wrapper for tree-based models
  - [ ] PyTorch/TensorFlow/TorchForecasting wrappers for sequence models
- [ ] Implement training script src/models/train.py
  - [ ] config-driven (configs/*.yaml)
  - [ ] deterministic seed, checkpointing, logging
- [ ] Validation strategy
  - [ ] Time-series cross-validation (expanding / rolling windows)
  - [ ] Walk-forward evaluation
- [ ] Baseline models to run
  - [ ] Logistic regression, RandomForest, XGBoost
  - [ ] LSTM / GRU baseline
  - [ ] Transformer small prototype
- [ ] Notebook: notebooks/03-model-prototyping.ipynb — reproducible runs & visualizations
- [ ] Record hyperparameters & run metadata in experiments tracker

Estimated time: 1–2 weeks

---

## Phase 5 — Backtesting & Strategy Design (Goal: translate predictions to trades + realistic P&L)
- [ ] Implement backtester: src/backtest/backtester.py
  - [ ] support slippage, fees, position sizing, order types, leverage
  - [ ] support event-driven simulation (signal -> order -> execution)
- [ ] Define strategy rules (entry, exit, stop-loss, take-profit)
- [ ] Evaluate risk metrics: Sharpe, Sortino, max drawdown, MAR ratio, CAGR
- [ ] Run backtests vs buy-and-hold and benchmark (BTC, ETH)
- [ ] Add walk-forward backtesting to avoid lookahead
- [ ] Save backtest reports to experiments/experiment_YYYY-MM-DD_id/backtest_report.md

Estimated time: 1–2 weeks

---

## Phase 6 — Experiment Tracking & Hyperparameter Tuning (Goal: reproducible experiments)
- [ ] Implement lightweight tracker src/experiments/tracker.py (or integrate MLflow)
  - [ ] log config, metrics, artifacts (models, plots)
- [ ] Create experiments folder template and naming convention
- [ ] Run hyperparameter sweeps (Optuna/Hyperopt)
- [ ] Store best checkpoints in models/checkpoints/

Estimated time: 3–7 days

---

## Phase 7 — Evaluation, Robustness & Risk Analysis (Goal: ensure real-world viability)
- [ ] Evaluate on multiple time periods & unseen market regimes
- [ ] Sensitivity analysis: feature ablation, parameter variation
- [ ] Adversarial checks: simulate extreme events, regime shifts
- [ ] Stress-test capital usage and margin calls
- [ ] Document failure modes and risk controls (docs/risk.md)

Estimated time: 1–2 weeks

---

## Phase 8 — Deployment & API (Goal: serve model for live/inference use)
- [ ] Build minimal serve API: src/api/serve.py (FastAPI)
  - [ ] endpoints: /health, /predict, /metrics
  - [ ] authentication and rate limits
- [ ] Add dockerfile and docker-compose for local deployment
- [ ] Add monitoring endpoints and logs for inference latency and errors
- [ ] Implement live data fetcher & scheduler (cron/k8s)

Estimated time: 1 week

---

## Phase 9 — Tests, Documentation & Finalization (Goal: publishable codebase)
- [ ] Unit tests for data, features, models (tests/)
- [ ] Integration tests for training -> backtest -> report
- [ ] Update README with instructions, architecture diagram
- [ ] Prepare reproducibility binder / environment snapshot
- [ ] Prepare presentation / paper draft with methodology and results

Estimated time: 3–7 days

---

## Ongoing / Maintenance
- [ ] Daily/weekly data sync
- [ ] Retrain schedule and model drift monitoring
- [ ] Add new features and check performance delta per experiment

---

## Status Board (copy this section into a lightweight kanban or keep here)
- Use the checkboxes above. Example quick snapshot:
  - Phase 0: [x] environment [ ] CI [ ] pre-commit
  - Phase 1: [ ] raw fetch implemented
  - Phase 2: [ ] EDA notebook created
  - Phase 3: [ ] indicators implemented
  - Phase 4: [ ] baselines trained
  - Phase 5: [ ] backtester implemented

---

## Experiment Template (use for each experiment file saved under experiments/)
- experiment_id: YYYYMMDD_{short-name}
- owner:
- date:
- objective:
- dataset:
- config_file: configs/xxx.yaml
- model:
- metrics:
- backtest_summary:
- notes:

---

If you want, I can:
- Update docs/project_plan.md file now with this content.
- Create skeleton files (scripts/fetch_data.py, src/data/preprocessing.py, src/models/train.py) next.

Which action should I take now? (reply: "update plan" or "scaffold files")