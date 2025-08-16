import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class CryptoTradingModel:
    def __init__(self, data):
        self.data = data
        self.model = None

    def preprocess_data(self):
        # Example preprocessing steps
        df = self.data.copy()

        # create target: 1 if next close is greater than current close
        df['target'] = (df['close'].shift(-1) > df['close']).astype(float)

        # drop last row(s) where target is NaN (due to shift)
        df = df.dropna(subset=['target']).reset_index(drop=True)

        # forward-fill remaining missing values if any
        df.fillna(method='ffill', inplace=True)

        # select numeric features only (exclude target)
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if 'target' in numeric_cols:
            numeric_cols.remove('target')

        # ensure there is at least one feature column
        if not numeric_cols:
            raise ValueError("No numeric feature columns available after preprocessing.")

        self.features = df[numeric_cols]
        self.target = df['target'].astype(int)
        self.data = df

    def split_data(self, test_size=0.2):
        X_train, X_test, y_train, y_test = train_test_split(
            self.features, self.target, test_size=test_size, random_state=42
        )
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        if self.model is None:
            raise Exception("Model has not been trained yet.")
        return self.model.predict(X_test)

    def evaluate_model(self, X_test, y_test):
        predictions = self.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy