import requests
import pandas as pd
import os
import sys
import argparse
from pathlib import Path

# ensure project src/ is importable so 'from utils...' works when running script directly
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from utils.config import load_config

def fetch_coingecko_data(api_url, api_key, params=None):
    """
    Fetch data from the CoinGecko API.
    """
    headers = {'x-cg-demo-api-key': api_key}
    response = requests.get(api_url, params=params, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def fetch_binance_data(symbol, start, end, api_key, api_secret):
    """
    Fetch data from the Binance API.
    """
    from binance.client import Client
    client = Client(api_key, api_secret)
    klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1DAY, start, end)
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume', 
        'close_time', 'quote_asset_volume', 'number_of_trades', 
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def save_data(df, filename):
    """
    Save the DataFrame to a CSV file.
    """
    parent_dir = Path(filename).parent
    if not parent_dir.exists():
        parent_dir.mkdir(parents=True)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch cryptocurrency data.")
    parser.add_argument("--source", type=str, default="coingecko", help="Data source to use (coingecko or binance)")
    parser.add_argument("--symbol", type=str, default="BTC-USD", help="Symbol to fetch data for (e.g., BTC-USD)")
    parser.add_argument("--start", type=str, help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end", type=str, help="End date in YYYY-MM-DD format")
    args = parser.parse_args()

    config = load_config()
    data_sources = config.get("data", {}).get("data_sources", {})
    source_config = data_sources.get(args.source, {})

    if not source_config:
        print(f"Error: Data source '{args.source}' not found in config.")
        return

    raw_data_path = ROOT / config.get("data", {}).get("raw_data_path")
    coin = args.symbol.split('-')[0].lower()
    file_path = Path(raw_data_path) / f"{args.source}_{coin}_data_{args.start}_{args.end}.csv"

    if args.source == "coingecko":
        start_timestamp = int(pd.to_datetime(args.start).timestamp()) if args.start else None
        end_timestamp = int(pd.to_datetime(args.end).timestamp()) if args.end else None
        api_url = f"{source_config.get('api_url')}/coins/{coin}/market_chart/range"
        params = {
            'vs_currency': args.symbol.split('-')[1].lower(),
            'from': start_timestamp,
            'to': end_timestamp,
        }
        data = fetch_coingecko_data(api_url, source_config.get('api_key'), params)
    
    elif args.source == "binance":
        data = fetch_binance_data(
            args.symbol.replace('-',''), 
            args.start, 
            args.end, 
            source_config.get('api_key'), 
            source_config.get('api_secret')
        )

    else:
        print(f"Error: Data source '{args.source}' not supported.")
        return

    save_data(data, file_path)

if __name__ == "__main__":
    main()