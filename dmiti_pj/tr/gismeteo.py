import requests
from bs4 import BeautifulSoup

url = 'https://www.gismeteo.ru/weather-sankt-peterburg-4079/10-days/'

headers = requests.utils.default_headers()

headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
date = soup.find_all('div', class_='date')
temperature = soup.find_all('span', class_='unit unit_temperature_c')
temperature = temperature[1:]


for i in range(len(date)):
    print(f"{date[i].text} : {temperature[i*2].text}")