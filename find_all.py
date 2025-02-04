import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

#find and find_all

product_name = soup.find_all('a', class_ = 'title')
product_name

description = soup.find_all('p', class_ = 'description')
description

import re
reviews = soup.find_all('p', class_ = re.compile('review-count'))
reviews

price = soup.find_all('h4', class_ = 'float-end price card-title pull-right')
price

#for loop and lists

product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)
    
product_name_list

price_list = []
for i in price:
    single_price = i.text
    price_list.append(single_price)
    
price_list

description_list = []
for i in description:
    desc = i.text
    description_list.append(desc)
    
description_list

reviews_list = []
for i in reviews:
    review = i.text
    reviews_list.append(review)
    
reviews_list

import pandas as pd

table = pd.DataFrame({'Product Name': product_name_list, 'Description': description_list,
                      'Price:':price_list, 'Reviews': reviews_list})

#data extract from nested HTML tags
boxes = soup.find_all('div', class_ = 'col-md-4 col-xl-4 col-lg-4')[0]
boxes

boxes.find('a').text
boxes.find('p', class_ = 'description').text

box2 = soup.find_all('ul', class_ = 'nav', id = 'side-menu')[0]
box2.find_all('li')[3].text









