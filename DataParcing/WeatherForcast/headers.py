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
)