import requests
from bs4 import BeautifulSoup
import calendar
import re
import json
from parcing_functions import *
from headers import *
import sys

start_year= 2017
end_year =2022

start_month = 1
end_month = 12

urls = url_parser([start_year, end_year], [start_month, end_month])

date_errors = []
type_errors = []
errors = []

for url in urls:
    try:
        parse_result = parse_text(get_temp_str(url))
        print(url[-10:], parse_result)
        key = url[-10:]
    except Exception: 
        type_errors.append(sys.exc_info()[1].__class__.__name__)
        errors.append(str(sys.exc_info()[1]))
        date_errors.append(key)
        print(key, 'ERROR')

print(f'Количество проблемных дат:  {len(date_errors)}\n', *date_errors, sep='\t')
print(f'Типы ошибок:\n', *type_errors, sep='\t')
print(f'Суть ошибок:\n', *errors, sep='\t')

'''
тестовый запуск необходимый для проверки всех дат
были проблемы с тем что парсер падал на некоторых страницах
'''