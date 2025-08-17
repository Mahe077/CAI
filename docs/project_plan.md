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
- [x] Initialize repository, add LICENSE, CODE_OF_CONDUCT, CONTRIBUTING.md
- [x] Define branch strategy (main/dev/feature/*)
- [x] Create environment files
  - [x] requirements.txt
  - [x] environment.yml
- [x] Add pre-commit hooks (black, isort, flake8)
- [x] Add CI pipeline skeleton (GitHub Actions: tests, lint)
- [x] Add reproducibility.md with exact commands and seed settings

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
- [ ] Optional: Integrate secondary data sources
  - [ ] CoinGecko market data
  - [ ] Glassnode on-chain data (if free tier usable)
  - [ ] Sentiment proxy (Reddit, Twitter scraping, optional)
- [ ] Document data source rationale in docs/data_sources.md

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
- [ ] Add time granularity EDA (1m/5m/1h) and determine optimal resolution
- [ ] Save histogram snapshots of technical indicators
- [ ] Detect and document exchange outages or data inconsistencies

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
 - [ ] Document and visualize full list of features
  - [ ] Group by type (momentum, volatility, volume, price action)
  - [ ] Save in docs/features.md
- [ ] Feature taxonomy diagram in notebooks/02-feature-taxonomy.ipynb
- [ ] Create data/labels.md with target generation strategy
  - [ ] E.g. “future 3h return > 1%” = buy label

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
- [ ] Add docs/ai_fusion.md (describe fusion strategy)
  - [ ] Inputs: price signals, features, multi-model output
  - [ ] Fusion: ensemble, rule-weighted, voting
- [ ] Add support for:
  - [ ] Multi-task head (if multi-horizon prediction needed)
  - [ ] Label noise robustness (smoothing, relabeling)
- [ ] Implement feature importance analysis (SHAP, permutation)
  - [ ] Save in notebooks/03-interpretability.ipynb

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
- [ ] Add model → signal → trade conversion logic in src/strategy/entry_exit.py
- [ ] Backtest multiple AI fusion variants:
  - [ ] Rule-based vs ML-only vs Hybrid
- [ ] Store risk-metric snapshot in experiments/{exp_id}/risk_metrics.json

Estimated time: 1–2 weeks

---

## Phase 6 — Experiment Tracking & Hyperparameter Tuning (Goal: reproducible experiments)
- [ ] Implement lightweight tracker src/experiments/tracker.py (or integrate MLflow)
  - [ ] log config, metrics, artifacts (models, plots)
- [ ] Create experiments folder template and naming convention
- [ ] Run hyperparameter sweeps (Optuna/Hyperopt)
- [ ] Store best checkpoints in models/checkpoints/
- [ ] Add experiment summary cards in experiments/logs/
- [ ] Save paper figures during experiment runs in experiments/{id}/figures/


Estimated time: 3–7 days

---

## Phase 7 — Evaluation, Robustness & Risk Analysis (Goal: ensure real-world viability)
- [ ] Evaluate on multiple time periods & unseen market regimes
- [ ] Sensitivity analysis: feature ablation, parameter variation
- [ ] Adversarial checks: simulate extreme events, regime shifts
- [ ] Stress-test capital usage and margin calls
- [ ] Document failure modes and risk controls (docs/risk.md)
- [ ] Add feature ablation analysis script
- [ ] Add adversarial simulation (simulated pump/dump, regime change)
- [ ] Stress-test AI fusion decision logic
- [ ] Document failure scenarios (docs/risk.md)
Estimated time: 1–2 weeks

---

## Phase 8 — Deployment & API (Goal: serve model for live/inference use)
- [ ] Build minimal serve API: src/api/serve.py (FastAPI)
  - [ ] endpoints: /health, /predict, /metrics
  - [ ] authentication and rate limits
- [ ] Add dockerfile and docker-compose for local deployment
- [ ] Add monitoring endpoints and logs for inference latency and errors
- [ ] Implement live data fetcher & scheduler (cron/k8s)
- [ ] Implement model rollback option
- [ ] Add optional trigger-based trade alerts (for simulation use)

Estimated time: 1 week

---

## Phase 9 — Tests, Documentation & Finalization (Goal: publishable codebase)
- [ ] Unit tests for data, features, models (tests/)
- [ ] Integration tests for training -> backtest -> report
- [ ] Update README with instructions, architecture diagram
- [ ] Prepare reproducibility binder / environment snapshot
- [ ] Prepare presentation / paper draft with methodology and results
- [ ] Add docs/research_protocol.md
  - [ ] Define hypothesis, goals, evaluation protocol
- [ ] Add paper_figures notebook (notebooks/04-paper-figures.ipynb)

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

New Docs/Reference Files to Add

- [ ] docs/features.md — full list of engineered features
- [ ] docs/ai_fusion.md — what fusion means, design philosophy
- [ ] docs/research_protocol.md — hypothesis & experiment design
- [ ] docs/labels.md — how prediction targets are derived
- [ ] docs/data_sources.md — justification of each data source
- [ ] docs/risk.md — assumptions, limitations, and robustness tests