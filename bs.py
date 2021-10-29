#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = []  # a list to store quotes

table = soup.find('div', attrs={'id': 'js-site-main'})

for row in table.findAll('div',
                         attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)


df = pd.DataFrame(quotes, columns=['theme', 'url', 'img', 'lines', 'author'])
print(df.describe().transpose())
