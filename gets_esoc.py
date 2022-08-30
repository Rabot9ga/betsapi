import requests


header={
    'cookie': '_ga=GA1.1.2063520179.1661428584; sid=hc7da330h5i78rh8q7r75obn2n; tz=Europe%2FMoscow; _ga_1LTT3CXFKZ=GS1.1.1661751802.13.1.1661751813.0.0.0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'upgrade-insecure-requests': '1'
}

for i in range(1, 2):
    req=requests.get('https://betsapi.com/ls/22614/Esoccer-Battle--8-mins-play/p.'+str(i), headers=header)
    print('https://betsapi.com/ls/22614/Esoccer-Battle--8-mins-play/p.'+str(i))
    with open('html\\'+str(i)+'e.html', 'w', encoding='utf-8') as file:
        file.write(req.text)