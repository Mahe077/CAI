import pandas as pd
import os
from datetime import datetime

class ExperimentTracker:
    def __init__(self, experiment_id, results_dir='experiments'):
        self.experiment_id = experiment_id
        self.results_dir = results_dir
        self.results_file = os.path.join(results_dir, f'results_{experiment_id}.csv')
        self.results = []

        # Create results directory if it doesn't exist
        os.makedirs(results_dir, exist_ok=True)

        # Initialize results file with headers if it doesn't exist
        if not os.path.isfile(self.results_file):
            self._initialize_results_file()

    def _initialize_results_file(self):
        headers = ['timestamp', 'experiment_id', 'metric', 'value']
        df = pd.DataFrame(columns=headers)
        df.to_csv(self.results_file, index=False)

    def log_experiment(self, metric, value):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.results.append({'timestamp': timestamp, 'experiment_id': self.experiment_id, 'metric': metric, 'value': value})
        self._save_results()

    def _save_results(self):
        df = pd.DataFrame(self.results)
        df.to_csv(self.results_file, mode='a', header=False, index=False)

    def get_results(self):
        return pd.read_csv(self.results_file)

# Example usage:
# tracker = ExperimentTracker('experiment_001')
# tracker.log_experiment('accuracy', 0.95)
# tracker.log_experiment('loss', 0.05)