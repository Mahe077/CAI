import unittest
from src.data.loader import load_data
from src.data.preprocessing import preprocess_data

class TestDataFunctions(unittest.TestCase):

    def setUp(self):
        # Setup code to initialize test data
        self.raw_data = load_data('data/raw/sample_data.csv')
        self.processed_data = preprocess_data(self.raw_data)

    def test_load_data(self):
        # Test if data is loaded correctly
        self.assertIsNotNone(self.raw_data)
        self.assertGreater(len(self.raw_data), 0)

    def test_preprocess_data(self):
        # Test if data preprocessing works as expected
        self.assertIsNotNone(self.processed_data)
        self.assertGreater(len(self.processed_data), 0)
        # Add more assertions based on expected preprocessing outcomes

    def test_data_integrity(self):
        # Test for data integrity checks
        self.assertTrue(self.processed_data.isnull().sum().sum() == 0, "Data contains null values")

if __name__ == '__main__':
    unittest.main()