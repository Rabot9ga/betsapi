import requests


header={
    'cookie': '_ga=GA1.1.2063520179.1661428584; sid=vakjq632je7ct83jkvt5co4us7; tz=Europe%2FMoscow; _ga_1LTT3CXFKZ=GS1.1.1661664176.12.1.1661664377.0.0.0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'upgrade-insecure-requests': '1'
}

for i in range(1, 11):
    req=requests.get('https://betsapi.com/cs/soccer/p.'+str(i)+'?skipE=1', headers=header)
    print('https://betsapi.com/cs/soccer/p.'+str(i)+'?skipE=1')
    with open('html\\'+str(i)+'.html', 'w', encoding='utf-8') as file:
        file.write(req.text)