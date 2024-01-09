import requests
from bs4 import BeautifulSoup
import calendar
import re
import json


headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)# данная конструкция нужна для того чтобы при отправки реквеста на сайт, сайт не думал что это бот