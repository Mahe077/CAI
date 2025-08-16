import pandas as pd
import numpy as np

def create_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Create features for the crypto trading model.

    Parameters:
    data (pd.DataFrame): The input data containing price and volume information.

    Returns:
    pd.DataFrame: The data with added features.
    """
    # Example feature: Calculate the moving average
    data['moving_average'] = data['close'].rolling(window=5).mean()

    # Example feature: Calculate the price change percentage
    data['price_change'] = data['close'].pct_change()

    # Example feature: Calculate the volume change percentage
    data['volume_change'] = data['volume'].pct_change()

    # Example feature: Create a binary feature for price increase
    data['price_increase'] = np.where(data['price_change'] > 0, 1, 0)

    return data

def select_features(data: pd.DataFrame, target: str) -> pd.DataFrame:
    """
    Select relevant features for the model.

    Parameters:
    data (pd.DataFrame): The input data with features.
    target (str): The target variable name.

    Returns:
    pd.DataFrame: The data with selected features.
    """
    # Example: Selecting features based on correlation with the target
    correlation_matrix = data.corr()
    relevant_features = correlation_matrix[target].abs().sort_values(ascending=False)
    
    # Select features with correlation above a certain threshold
    selected_features = relevant_features[relevant_features > 0.1].index.tolist()
    
    return data[selected_features]