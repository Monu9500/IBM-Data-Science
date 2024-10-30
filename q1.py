import yfinance as yf
import pandas as pd

# Fetch Tesla stock data
tesla_data = yf.download('TSLA', start='2020-01-01', end='2024-01-01')

# Display the first few rows of the data
print("Tesla Stock Data:")
print(tesla_data.head())