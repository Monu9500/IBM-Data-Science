import matplotlib.pyplot as plt

# Sample revenue data (for demonstration purposes)
tesla_revenue = [24.57, 31.53, 42.49]  # Example revenue in billions for recent years
years = ['2020', '2021', '2022']

# Plot Tesla stock price
plt.figure(figsize=(10, 5))

# Subplot for stock data
plt.subplot(1, 2, 1)
plt.plot(tesla_data.index, tesla_data['Close'], label='Tesla Stock Price')
plt.title('Tesla Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()

# Subplot for revenue data
plt.subplot(1, 2, 2)
plt.bar(years, tesla_revenue, color='orange')
plt.title('Tesla Revenue')
plt.xlabel('Year')
plt.ylabel('Revenue (Billions USD)')

plt.tight_layout()
plt.show()
