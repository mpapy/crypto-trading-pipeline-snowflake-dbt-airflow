from snowflake.connector import DictCursor
from datetime import datetime
import pandas as pd
import requests

pairs = ['PEPEUSDT', 'ORDIUSDT', '1000FLOKIUSDT', 'BIGTIMEUSDT', 'WIFUSDT', 'DOGEUSDT']
columns_full = [
    'open_time', 'open', 'high', 'low', 'close', 'volume',
    'close_time', 'quote_asset_volume', 'number_of_trades',
    'taker_buy_base', 'taker_buy_quote', 'ignore'
]
columns = ['open_time', 'open', 'high', 'low', 'close', 'volume']

results = []

# Fetch data from Binance API for the specified pairs
for pair in pairs:
    response = requests.get('https://api.binance.com/api/v3/klines', params={
        'symbol': pair,
        "interval": '1m',
        "limit": 10
    })
    raw_data = response.json()
    df = pd.DataFrame(raw_data, columns=columns_full)
    df = df[columns]  # Keep only the relevant columns
    df.insert(0, 'symbol', pair)  # Add the symbol column

    results.append(df)  # Append the DataFrame to results list

# Concatenate all DataFrames in the results list
final_df = pd.concat(results, ignore_index=True)
final_df['open_time'] = pd.to_datetime(final_df['open_time'], unit='ms')
# Convert columns to appropriate data types
final_df['open'] = pd.to_numeric(final_df['open'])
final_df['high'] = pd.to_numeric(final_df['high'])
final_df['low'] = pd.to_numeric(final_df['low'])
final_df['close'] = pd.to_numeric(final_df['close'])
final_df['volume'] = pd.to_numeric(final_df['volume'])

print(final_df)