# Fetch GameStop stock data
gamestop_data = yf.download('GME', start='2020-01-01', end='2024-01-01')

# Display the first few rows of the data
print("GameStop Stock Data:")
print(gamestop_data.head())