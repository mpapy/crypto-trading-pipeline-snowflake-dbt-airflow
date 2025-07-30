from snowflake.connector import DictCursor
from datetime import datetime
import pandas as pd
import requests
from utils.snowflake_conn import get_connection


pairs = ['PEPEUSDT', 'ORDIUSDT', '1000FLOKIUSDT', 'BIGTIMEUSDT', 'WIFUSDT', 'DOGEUSDT']
columns_full = [
    'open_time', 'open_price', 'high_price', 'low_price', 'close_price', 'volume',
    'close_time', 'quote_asset_volume', 'number_of_trades',
    'taker_buy_base', 'taker_buy_quote', 'ignore'
]
columns = ['open_time', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']

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
# Convert columns to appropriate data types
final_df["open_time"] = pd.to_numeric(final_df['open_time'])
final_df['open_price'] = pd.to_numeric(final_df['open_price'])
final_df['high_price'] = pd.to_numeric(final_df['high_price'])
final_df['low_price'] = pd.to_numeric(final_df['low_price'])
final_df['close_price'] = pd.to_numeric(final_df['close_price'])
final_df['volume'] = pd.to_numeric(final_df['volume'])

print(f"""dataset {final_df} must be withhout ) 0 values in open price, high price, low price, close price""")

query = f"""INSERT INTO TRADING_DB.RAW.CRYPTO_PRICES (symbol, open_time, open_price, high_price, low_price, close_price, volume) 
            VALUES (%s, %s, %s, %s, %s, %s, %s) """
list_of_values = list(final_df.itertuples(index=False, name=None))
conn = get_connection()
cursor = conn.cursor(DictCursor)
cursor.execute("USE DATABASE TRADING_DB")
cursor.execute("USE SCHEMA RAW")
cursor.execute("USE WAREHOUSE TRADING_WH")
cursor.execute("TRUNCATE TABLE CRYPTO_PRICES")
cursor.executemany(query, list_of_values)
conn.commit()
cursor.close()