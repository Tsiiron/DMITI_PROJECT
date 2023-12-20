import requests
from bs4 import BeautifulSoup
import calendar
import re
import json
from parcing_functions import *
from headers import *
import sys
import threading

start_year= 2017
end_year =2022

start_month = 1
end_month = 12

urls = url_parser([start_year, end_year], [start_month, end_month])

date_errors = []
type_errors = []
errors = []

def bimbimbambam():
    global url
    parse_result = parse_text(get_temp_str(url))
    print(url[-10:], parse_result)

counter = 0

for url in urls:
    try:
        thread = threading.Thread(target=bimbimbambam, name=f'Tread{counter}')
        thread.start()
        counter+=1        

    except Exception: 
        type_errors.append(sys.exc_info()[1].__class__.__name__)
        errors.append(str(sys.exc_info()[1]))
        date_errors.append(url[-10:])
        print(url[-10:], 'ERROR')

print(f'Количество проблемных дат:  {len(date_errors)}\n', *date_errors, sep='\t')
print(f'Типы ошибок:\n', *type_errors, sep='\t')
print(f'Суть ошибок:\n', *errors, sep='\t')
