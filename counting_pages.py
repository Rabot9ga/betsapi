import requests
from bs4 import BeautifulSoup
import re

def searching_pages_count_football(cookies):
    header = {
            'cookie': cookies,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'upgrade-insecure-requests': '1'
        }
    req = requests.get('https://betsapi.com/cs/soccer/p.1?skipE=1', headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')
    lst=re.findall(r"\/cs\/soccer\/p.\d+", soup.prettify())
    new_lst=[]
    for i in lst:
        new_lst.append(re.search(r"\d+", i)[0])
    return max(list(map(int, new_lst)))


def searching_pages_count_tennis(cookies='_ga=GA1.1.2063520179.1661428584; sid=jbg466it10pegeeh7oih1li57a; tz=Europe%2FMoscow; _ga_1LTT3CXFKZ=GS1.1.1664602099.63.1.1664602173.0.0.0'):
    header = {
            'cookie': cookies,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'upgrade-insecure-requests': '1'
        }
    req = requests.get('https://betsapi.com/cs/tennis/p.1?skipE=1', headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')
    lst=re.findall(r"\/cs\/tennis\/p.\d+", soup.prettify())
    new_lst=[]
    for i in lst:
        new_lst.append(re.search(r"\d+", i)[0])
    return max(list(map(int, new_lst)))

