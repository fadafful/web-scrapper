import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/REG'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

#table = soup.find('table', {'summary': 'Standings - Detailed View'})
table = soup.find('table', class_ = 'd3-o-table')
table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)
    
df = pd.DataFrame(columns = headers)
df

for j in table.find_all('tr')[1:]:
    first_td = j.find_all('td')[0].find('div', class_ = 'd3-o-club-fullname').text.strip()
    row_data = j.find_all('td')[1:]
    row = [td.text.strip() for td in row_data]
    row.insert(0, first_td)
    length = len(df)
    df.loc[length] = row
