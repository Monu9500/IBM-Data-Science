# Sample revenue data for GameStop (for demonstration purposes)
gamestop_revenue = [5.09, 6.92, 8.64]  # Example revenue in billions for recent years
years_gme = ['2020', '2021', '2022']

# Plot GameStop stock price
plt.figure(figsize=(10, 5))

# Subplot for stock data
plt.subplot(1, 2, 1)
plt.plot(gamestop_data.index, gamestop_data['Close'], label='GameStop Stock Price', color='green')
plt.title('GameStop Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()

# Subplot for revenue data
plt.subplot(1, 2, 2)
plt.bar(years_gme, gamestop_revenue, color='blue')
plt.title('GameStop Revenue')
plt.xlabel('Year')
plt.ylabel('Revenue (Billions USD)')

plt.tight_layout()
plt.show()
