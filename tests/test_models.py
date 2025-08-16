import unittest
import pandas as pd
from pathlib import Path
import sys

# Add project root to path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.models.model import CryptoTradingModel

class TestCryptoTradingModel(unittest.TestCase):

    def setUp(self):
        # Create a sample dataframe for testing
        data = {
            'timestamp': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
            'open': [100, 102, 101, 103, 105],
            'high': [103, 104, 103, 106, 107],
            'low': [99, 101, 100, 102, 104],
            'close': [102, 101, 103, 105, 106],
            'volume': [1000, 1100, 1200, 1300, 1400]
        }
        self.df = pd.DataFrame(data)
        self.model = CryptoTradingModel(self.df)

    def test_preprocess_data(self):
        self.model.preprocess_data()
        self.assertIn('target', self.model.data.columns)
        self.assertFalse(self.model.features.isnull().sum().sum() > 0)

    def test_train_predict_evaluate(self):
        self.model.preprocess_data()
        X_train, X_test, y_train, y_test = self.model.split_data()
        self.model.train_model(X_train, y_train)
        
        # Test predict
        predictions = self.model.predict(X_test)
        self.assertEqual(len(predictions), len(X_test))

        # Test evaluate
        accuracy = self.model.evaluate_model(X_test, y_test)
        self.assertIsInstance(accuracy, float)
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

if __name__ == '__main__':
    unittest.main()
