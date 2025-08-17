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
  - [x] CLI args: symbols, timeframe, start, end, out-path
  - [x] Retry/backoff and rate-limit handling
  - [x] Save raw CSV/Parquet to data/raw/{exchange}/{symbol}/{YYYY-MM-DD}.parquet
- [ ] Add metadata files (data/raw/_README.md, data/schema.json)
- [ ] Add automated daily fetch cron/script (scripts/sync_data.sh)
- [ ] Validate raw files (schema and checksum)
- [ ] Optional: Integrate secondary data sources
  - [ ] CoinGecko market data
  - [ ] Glassnode on-chain data (if free tier usable)
  - [ ] Sentiment proxy (Reddit, Twitter scraping, optional)
- [x] Document data source rationale in docs/data_sources.md

Estimated time: 2–4 days

---

## Phase 2 — EDA & Data Quality (Goal: understand data & quality issues)
- [ ] Create notebook: notebooks/01-data-exploration.ipynb
  - [ ] Load sample symbols
  - [ ] Check missing data, duplicates, time alignment, timezone issues
  - [ ] Visualize price, volume, volatility, gaps
  - [ ] Save EDA notebook notes and plots to docs/eda/
- [ ] Implement basic validators in src/data/validator.py
- [ ] Generate a one-page data quality report (docs/data_quality.md)
- [x] Add time granularity EDA (1m/5m/1h) and determine optimal resolution (Done via optimizer script)
- [x] Save histogram snapshots of technical indicators (Done via model analysis plots)
- [ ] Detect and document exchange outages or data inconsistencies

Estimated time: 2–3 days

---

## Phase 3 — Preprocessing & Feature Engineering (Goal: stable feature pipeline)
- [ ] Design processing contract: inputs, outputs, expected scalers, imputation strategy
- [ ] Implement src/data/preprocessing.py
- [x] Implement technical indicators in src/features/engineering.py
  - [x] basic: SMA, EMA, RSI, MACD, Bollinger Bands, ATR, OBV
  - [x] derived: returns, rolling-volatility, momentum, liquidity features
- [ ] Create feature store layout: data/processed/features/{symbol}/{timeframe}.parquet
- [ ] Notebook: notebooks/02-feature-engineering.ipynb — visualize feature distributions and correlation matrix
- [ ] Add feature selection checklist: correlation threshold, importance-based pruning
 - [x] Document and visualize full list of features
  - [x] Group by type (momentum, volatility, volume, price action)
  - [x] Save in docs/features.md
- [ ] Feature taxonomy diagram in notebooks/02-feature-taxonomy.ipynb
- [x] Create data/labels.md with target generation strategy
  - [x] E.g. “future 3h return > 1%” = buy label

Estimated time: 4–7 days

---

## Phase 4 — Modeling & Validation (Goal: baseline models + robust validation)
- [x] Define prediction task(s)
  - [x] classification: up/down in horizon H
  - [x] regression: future log-return
  - [ ] multi-horizon experiments
- [ ] Implement model interfaces in src/models/model.py
- [x] Implement training script src/models/train.py
  - [x] config-driven (configs/*.yaml)
  - [x] deterministic seed, checkpointing, logging
- [x] Validation strategy
  - [ ] Time-series cross-validation (expanding / rolling windows)
  - [x] Walk-forward evaluation
- [x] Baseline models to run
  - [ ] Logistic regression, RandomForest, XGBoost
  - [x] LSTM / GRU baseline
  - [ ] Transformer small prototype
- [ ] Notebook: notebooks/03-model-prototyping.ipynb — reproducible runs & visualizations
- [x] Record hyperparameters & run metadata in experiments tracker (Done via optimizer script)
- [x] Add docs/ai_fusion.md (describe fusion strategy)
  - [x] Inputs: price signals, features, multi-model output
  - [x] Fusion: ensemble, rule-weighted, voting
- [x] Add support for:
  - [ ] Multi-task head (if multi-horizon prediction needed)
  - [x] Label noise robustness (smoothing, relabeling) (Done via Triple-Barrier)
- [x] Implement feature importance analysis (SHAP, permutation)
  - [ ] Save in notebooks/03-interpretability.ipynb

Estimated time: 1–2 weeks

---

## Phase 5 — Backtesting & Strategy Design (Goal: translate predictions to trades + realistic P&L)
- [x] Implement backtester: src/backtest/backtester.py
  - [x] support slippage, fees, position sizing, order types, leverage
  - [x] support event-driven simulation (signal -> order -> execution)
- [x] Define strategy rules (entry, exit, stop-loss, take-profit)
- [x] Evaluate risk metrics: Sharpe, Sortino, max drawdown, MAR ratio, CAGR (Done via PnL analysis)
- [ ] Run backtests vs buy-and-hold and benchmark (BTC, ETH)
- [x] Add walk-forward backtesting to avoid lookahead (Implicit in train/val/test split)
- [ ] Save backtest reports to experiments/experiment_YYYY-MM-DD_id/backtest_report.md
- [x] Add model → signal → trade conversion logic in src/strategy/entry_exit.py
- [x] Backtest multiple AI fusion variants:
  - [x] Rule-based vs ML-only vs Hybrid
- [ ] Store risk-metric snapshot in experiments/{exp_id}/risk_metrics.json

Estimated time: 1–2 weeks

---

## Phase 6 — Experiment Tracking & Hyperparameter Tuning (Goal: reproducible experiments)
- [ ] Implement lightweight tracker src/experiments/tracker.py (or integrate MLflow)
- [x] Create experiments folder template and naming convention (Done via optimizer script save structure)
- [x] Run hyperparameter sweeps (Optuna/Hyperopt) (Done via custom optimizer script)
- [x] Store best checkpoints in models/checkpoints/
- [ ] Add experiment summary cards in experiments/logs/
- [x] Save paper figures during experiment runs in experiments/{id}/figures/ (Plots saved in model dirs)


Estimated time: 3–7 days

---

## Phase 7 — Evaluation, Robustness & Risk Analysis (Goal: ensure real-world viability)
- [x] Evaluate on multiple time periods & unseen market regimes (Done via optimizer script)
- [ ] Sensitivity analysis: feature ablation, parameter variation
- [ ] Adversarial checks: simulate extreme events, regime shifts
- [ ] Stress-test capital usage and margin calls
- [x] Document failure modes and risk controls (docs/risk.md)
- [ ] Add feature ablation analysis script
- [ ] Add adversarial simulation (simulated pump/dump, regime change)
- [x] Stress-test AI fusion decision logic
- [x] Document failure scenarios (docs/risk.md)
Estimated time: 1–2 weeks

---

## Phase 8 — Deployment & API (Goal: serve model for live/inference use)
- [ ] Build minimal serve API: src/api/serve.py (FastAPI)
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
- [x] Update README with instructions, architecture diagram
- [x] Prepare reproducibility binder / environment snapshot
- [ ] Prepare presentation / paper draft with methodology and results
- [x] Add docs/research_protocol.md
  - [x] Define hypothesis, goals, evaluation protocol
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

- [x] docs/features.md — full list of engineered features
- [x] docs/ai_fusion.md — what fusion means, design philosophy
- [x] docs/research_protocol.md — hypothesis & experiment design
- [x] docs/labels.md — how prediction targets are derived
- [x] docs/data_sources.md — justification of each data source
- [x] docs/risk.md — assumptions, limitations, and robustness tests
