import requests
from bs4 import BeautifulSoup
import calendar
import re
import json
from headers import headers

'''
данная функия создает ссылки для парсинга. 
Все ссылки на сайте имеет подобную стрктуру
'''
def url_parser(years : list, months : list) -> list:
    urls = []                                   
    for year in range(years[0], years[1] + 1):
        for month in range(months[0], months[1] + 1):
            days = calendar.monthrange(year, month)[1]
            for day in range(1,days+1):
                url = f"https://www.meteoservice.ru/archive/sankt-peterburg/{year}/{month:02d}/{day:02d}"
                urls.append(url)
    return urls



#данная функция непосредственно отправляет реквест на сайт и получает нужные данные
def get_temp_str(url : str) -> str:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    value = soup.find_all('div', class_='callout')[0].text
    return value


#данная функия ищет в тексте температуру днем и ночью
def find_values(string):
    numbers = re.findall(r'\d+', string)
    for i in range(len(numbers)):
        if string[string.find(numbers[i]) - 1] == '-':
            numbers[i] = int(numbers[i]) * -1
        else:
            numbers[i] = int(numbers[i])
    return numbers
# в этой функции создается словарь значений температур днем и ночью. Ключ дата, значений список температур
def parse_text(text : str) -> dict:
    first_index = text.find("°")
    second_index = text.find("°", first_index + 1)
    dct = {}
    if(second_index != -1):
        night = find_values(text[first_index - 10 : first_index])
        if(len(night) == 1): night.append(night[0])
        day = find_values(text[second_index - 10 : second_index])
        if(len(day) == 1): day.append(day[0])
        dct["night"] = int(round(night[0] + night[1]) / 2)
        dct["day"] = int(round(day[0] + day[1]) / 2)
    else:
        night = find_values(text[first_index - 10 : first_index])
        if(len(night) == 1): night.append(night[0])
        day = night
        dct["night"] = int(round(night[0] + night[1]) / 2)
        dct["day"] = int(round(day[0] + day[1]) / 2)
    return dct