import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quoutes = soup.find_all('small', class_='author')
for value in quoutes:
    print(value.text)