import requests
import pandas as pd
import os

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
    return pd.DataFrame(data)

def save_data(df, filename):
    """
    Save the DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        filename (str): The filename for the saved CSV.
    """
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    # Define API URL and parameters
    api_url = "https://api.example.com/crypto-data"  # Replace with actual API URL
    params = {
        'symbol': 'BTC',  # Example parameter
        'interval': '1d',  # Example parameter
        'limit': 100  # Example parameter
    }

    # Fetch data
    data = fetch_data(api_url, params)

    # Create directories if they don't exist
    os.makedirs('data/raw', exist_ok=True)

    # Save raw data
    save_data(data, 'data/raw/crypto_data.csv')

if __name__ == "__main__":
    main()