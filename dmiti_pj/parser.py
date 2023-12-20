import requests
from bs4 import BeautifulSoup
import calendar
import re
import json
import sys
from parcing_functions import *
from headers import *


if __name__ == '__main__':
    json_data = {}

    start_year= 2013
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
            json_data[key] = parse_result
        except Exception: 
            type_errors.append(sys.exc_info()[1].__class__.__name__)
            errors.append(str(sys.exc_info()[1]))
            date_errors.append(key)
    
    print(f'Количество ошибок: {len(date_errors)}\n', *date_errors, sep='\t')
    print(f'Типы ошибок:\n', *type_errors, sep='\t')
    print(f'Суть ошибок:\n', *errors, sep='\t')

    with open('data.json', 'w') as file:
        json.dump(json_data, file, indent=2, sort_keys=True)

    file.close