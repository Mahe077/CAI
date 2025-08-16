import unittest
import pandas as pd
from pathlib import Path

from src.data.loader import load_raw_data

class TestDataLoading(unittest.TestCase):

    def setUp(self):
        # Create a dummy data file for testing
        self.data_dir = Path("data/raw")
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.test_file = self.data_dir / "test_data.csv"
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        pd.DataFrame(data).to_csv(self.test_file, index=False)

    def test_load_data(self):
        """Tests that data is loaded correctly."""
        df = load_raw_data(self.test_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def tearDown(self):
        # Clean up the dummy data file
        self.test_file.unlink()

if __name__ == '__main__':
    unittest.main()