import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

price = soup.find('bg-quote', class_ = 'value').text
price

closing_price = soup.find('td', class_ = 'table__cell u-semi').text
closing_price

nested = soup.find('mw-rangebar', class_ = 'element element--range range--yearly')
nested

lower = nested.find_all('span', class_ = 'primary')[0].text
lower

upper = nested.find_all('span', class_ = 'primary')[1].text
upper