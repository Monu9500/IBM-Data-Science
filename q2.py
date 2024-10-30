import requests
from bs4 import BeautifulSoup

# URL of Tesla's financials on Yahoo Finance
url = 'https://finance.yahoo.com/quote/TSLA/financials?p=TSLA'

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find revenue data (this may change based on the actual webpage structure)
revenue_data = soup.find_all('td', string='Total Revenue')
for revenue in revenue_data:
    print("Tesla Revenue Data:", revenue.find_next_sibling('td').text)
