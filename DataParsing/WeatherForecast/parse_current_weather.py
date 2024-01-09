import requests
from bs4 import BeautifulSoup
from DMITI_PROJECT.DataParcing.WeatherForcast.headers import headers

def get_temp() -> list:
    response = requests.get("https://www.meteoservice.ru/weather/14days/sankt-peterburg", headers= headers)
    soup = BeautifulSoup(response.text, 'lxml')
    value = soup.find_all('span', class_='value colorize-server-side')
    return value

def get_dates() -> list:
    response = requests.get("https://www.meteoservice.ru/weather/14days/sankt-peterburg", headers= headers)
    soup = BeautifulSoup(response.text, 'lxml')
    value = soup.find_all('div', class_='text-nowrap grey hide-for-large')
    return value

def get_some_days_tmp(days : int) -> list:
    if days <= 0 : return []
    if days >= 14 : days = 14
    data = get_temp()
    dates = get_dates()
    tmp = {}

    for number in range(days):
        day = data[number * 2].text
        night = data[number * 2 + 1].text
        date1 = dates[number].text.split('.')
        date = f'{int(date1[0]):02d}'+'/'+f'{int(date1[1]):02d}'
        day_value = int(day[:len(day) - 1])
        night_value = int(night[:len(night) - 1])
        tmp[date] = {'day' : day_value, 'night' : night_value}
    
    return tmp