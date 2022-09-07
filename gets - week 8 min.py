import tkinter, tkinter.messagebox
import requests
import main
import main_tennis




header = {
    'cookie': '_ga=GA1.1.2063520179.1661428584; sid=r0o4uidr8e6jnla146gvr1ac42; tz=Europe%2FMoscow; _ga_1LTT3CXFKZ=GS1.1.1662543053.31.1.1662544326.0.0.0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'upgrade-insecure-requests': '1'
}



for i in range(6, 120):
    req=requests.get('https://betsapi.com/le/22614/Esoccer-Battle--8-mins-play/p.'+str(i), headers=header)
    print('https://betsapi.com/le/22614/Esoccer-Battle--8-mins-play/p.'+str(i))
    with open('html\\'+str(i)+'8.html', 'w', encoding='utf-8') as file:
        file.write(req.text)


