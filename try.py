import requests
from bs4 import BeautifulSoup
import re


header = {
        # 'cookie': cookies,
        'cookie': '_ga=GA1.1.2063520179.1661428584; sid=0ke58v0tngeb44k95d13g4mndl; tz=Europe%2FMoscow; _ga_1LTT3CXFKZ=GS1.1.1664564601.62.0.1664564601.0.0.0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'upgrade-insecure-requests': '1'
    }
req = requests.get('https://betsapi.com/cs/soccer/p.1?skipE=1', headers=header)
soup = BeautifulSoup(req.text, 'html.parser')
lst=re.findall(r"\/cs\/soccer\/p.\d+", soup.prettify())
print(lst)

