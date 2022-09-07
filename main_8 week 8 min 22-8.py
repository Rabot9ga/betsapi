from bs4 import BeautifulSoup
import re

a = {}

b=['09/06', '09/05', '09/04', '09/03', '09/02', '09/01', '08/31']

def adding_a(time, c):
    if time in a:
        a[time] += c
    else:
        a[time] = c

for k in range(6, 120):
    with open('html\\' + str(k) + '8.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        result=re.findall(r'09/0[1-6] 0[0-7]:..|09/0[1-6] 2[2-3]:..|08/31 0[0-7]:..|08/31 2[2-3]:..', soup.get_text())
        for i in result:
            if i[:5] in a:
                a[i[:5]]+=1
            else:
                a[i[:5]]=1
            print(i[6:])
        # for j in b:
        #     adding_a(j, soup.get_text().count(j))



with open('week_8_night.txt', 'w') as file:
    for i in a:
        file.write(str(i) + ',' + str(a[i]) + '\n')
