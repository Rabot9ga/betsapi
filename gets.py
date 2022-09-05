import tkinter
import requests
import main
import main_tennis

header={
    'cookie': '_ga=GA1.1.2063520179.1661428584; sid=kr9bs082sb25ov9rana9d2nqmb; tz=Europe%2FMoscow; _ga_1LTT3CXFKZ=GS1.1.1662356892.27.1.1662357003.0.0.0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'upgrade-insecure-requests': '1'
}

pages_soc=3
pages_ten=3

for i in range(1, pages_soc):
    req=requests.get('https://betsapi.com/cs/soccer/p.'+str(i)+'?skipE=1', headers=header)
    print('https://betsapi.com/cs/soccer/p.'+str(i)+'?skipE=1')
    with open('html\\'+str(i)+'.html', 'w', encoding='utf-8') as file:
        file.write(req.text)

main.main(pages_soc)

# for i in range(1, 3):
#     req=requests.get('https://betsapi.com/ls/22614/Esoccer-Battle--8-mins-play/p.'+str(i), headers=header)
#     print('https://betsapi.com/ls/22614/Esoccer-Battle--8-mins-play/p.'+str(i))
#     with open('html\\'+str(i)+'8.html', 'w', encoding='utf-8') as file:
#         file.write(req.text)



# for i in range(1, 2):
#     req=requests.get('https://betsapi.com/ls/22821/Esoccer-Live-Arena--10-mins-play/p.'+str(i), headers=header)
#     print('https://betsapi.com/ls/22614/Esoccer-Battle--10-mins-play/p.'+str(i))
#     with open('html\\'+str(i)+'10.html', 'w', encoding='utf-8') as file:
#         file.write(req.text)



# for i in range(1, 7):
#     req=requests.get('https://betsapi.com/ls/23114/Esoccer-GT-Leagues-%E2%80%93-12-mins-play/p.'+str(i), headers=header)
#     print('https://betsapi.com/ls/22614/Esoccer-Battle--12-mins-play/p.'+str(i))
#     with open('html\\'+str(i)+'12.html', 'w', encoding='utf-8') as file:
#         file.write(req.text)


for i in range(1, pages_ten):
    req=requests.get('https://betsapi.com/cs/tennis/p.'+str(i), headers=header)
    print('https://betsapi.com/cs/tennis/p.'+str(i))
    with open('html\\'+str(i)+'tennis.html', 'w', encoding='utf-8') as file:
        file.write(req.text)

main_tennis.main(pages_ten)