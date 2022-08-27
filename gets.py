import requests


header={
    'cookie': 'tz=Europe%2FMoscow; _ga=GA1.1.2063520179.1661428584; sid=ll3nij337r731c0840ha0a078m; tz=Europe%2FMoscow; _ga_1LTT3CXFKZ=GS1.1.1661583432.8.1.1661588334.0.0.0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

for i in range(1, 15):

    req=requests.get('https://betsapi.com/cs/soccer/p.'+str(i)+'?skipE=1', headers=header)
    print('https://betsapi.com/cs/soccer/p.'+str(i)+'?skipE=1')
    with open('html\\'+str(i)+'.html', 'w', encoding='utf-8') as file:
        file.write(req.text)