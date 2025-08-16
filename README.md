# Crypto Trading AI Research Project Plan

## Project Overview
This project aims to implement AI techniques for crypto trading, focusing on data analysis, feature engineering, model training, and backtesting strategies.

## Steps to Follow

### 1. Define Research Objectives
- Clearly outline the goals of the research.
- Identify key questions to be answered.

### 2. Data Collection
- [ ] Identify data sources (e.g., exchanges, APIs).
- [ ] Fetch data using `scripts/fetch_data.py`.
- [ ] Store raw data in `data/raw`.

### 3. Data Exploration
- [ ] Open `notebooks/01-data-exploration.ipynb`.
- [ ] Analyze and visualize the data.
- [ ] Document findings in the notebook.

### 4. Data Preprocessing
- [ ] Implement data preprocessing in `src/data/preprocessing.py`.
- [ ] Clean and transform data.
- [ ] Store processed data in `data/processed`.

### 5. Feature Engineering
- [ ] Open `notebooks/02-feature-engineering.ipynb`.
- [ ] Create and select features.
- [ ] Document feature selection process.

### 6. Model Prototyping
- [ ] Open `notebooks/03-model-prototyping.ipynb`.
- [ ] Prototype different AI models in `src/models/model.py`.
- [ ] Train models using `src/models/train.py`.

### 7. Backtesting
- [ ] Implement backtesting in `src/backtest/backtester.py`.
- [ ] Evaluate trading strategies using historical data.

### 8. Experiment Tracking
- [ ] Use `src/experiments/tracker.py` to log experiments.
- [ ] Store results in `experiments/experiment_YYYY-MM-DD_id/results.csv`.

### 9. Evaluation
- [ ] Evaluate model performance using metrics in `src/utils/metrics.py`.
- [ ] Document evaluation results in `docs/experiments.md`.

### 10. API Development
- [ ] Implement API for serving models in `src/api/serve.py`.
- [ ] Test API functionality.

### 11. Documentation
- [ ] Update `README.md` with project details.
- [ ] Document reproducibility guidelines in `docs/reproducibility.md`.

### 12. Testing
- [ ] Write unit tests in `tests/test_data.py` and `tests/test_models.py`.
- [ ] Run tests and ensure code quality.

### 13. Final Review
- [ ] Review all components of the project.
- [ ] Prepare for presentation or publication.

## Status Update
- [ ] Define Research Objectives
- [ ] Data Collection
- [ ] Data Exploration
- [ ] Data Preprocessing
- [ ] Feature Engineering
- [ ] Model Prototyping
- [ ] Backtesting
- [ ] Experiment Tracking
- [ ] Evaluation
- [ ] API Development
- [ ] Documentation
- [ ] Testing
- [ ] Final Review

This plan can be updated as tasks are completed, and additional steps can be added as needed.