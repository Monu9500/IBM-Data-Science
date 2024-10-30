# URL of GameStop's financials on Yahoo Finance
url_gme = 'https://finance.yahoo.com/quote/GME/financials?p=GME'

# Fetch the page
response_gme = requests.get(url_gme)
soup_gme = BeautifulSoup(response_gme.text, 'html.parser')

# Find revenue data
revenue_data_gme = soup_gme.find_all('td', string='Total Revenue')
for revenue in revenue_data_gme:
    print("GameStop Revenue Data:", revenue.find_next_sibling('td').text)
