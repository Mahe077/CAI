import requests
import pandas as pd
import os
import sys
from pathlib import Path

# ensure project src/ is importable so 'from utils...' works when running script directly
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from utils.config import load_config

def fetch_data(api_url, params=None):
    """
    Fetch data from the specified API URL.

    Args:
        api_url (str): The API endpoint to fetch data from.
        params (dict, optional): Additional parameters for the API request.

    Returns:
        pd.DataFrame: A DataFrame containing the fetched data.
    """
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    # The coingecko API returns prices in a nested list
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def save_data(df, filename):
    """
    Save the DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        filename (str): The filename for the saved CSV.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    config = load_config()
    data_source_config = config.get("data", {}).get("data_source", {})
    
    api_url = f"{data_source_config.get('api_url')}/coins/{data_source_config.get('coin')}/market_chart"
    params = {
        'vs_currency': data_source_config.get('currency'),
        'days': data_source_config.get('days'),
    }

    # Fetch data
    data = fetch_data(api_url, params)

    # Save raw data
    raw_data_path = config.get("data", {}).get("raw_data_path")
    file_path = os.path.join(raw_data_path, f"{data_source_config.get('coin')}_data.csv")
    save_data(data, file_path)

if __name__ == "__main__":
    main()