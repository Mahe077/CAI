import pandas as pd
import os

def load_raw_data(file_path):
    """
    Load raw data from the specified file path.
    
    Parameters:
    file_path (str): The path to the raw data file.
    
    Returns:
    pd.DataFrame: A DataFrame containing the raw data.
    """
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

def load_external_data(file_path):
    """
    Load external data from the specified file path.
    
    Parameters:
    file_path (str): The path to the external data file.
    
    Returns:
    pd.DataFrame: A DataFrame containing the external data.
    """
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

def load_processed_data(file_path):
    """
    Load processed data from the specified file path.
    
    Parameters:
    file_path (str): The path to the processed data file.
    
    Returns:
    pd.DataFrame: A DataFrame containing the processed data.
    """
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")