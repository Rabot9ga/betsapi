from bs4 import BeautifulSoup
import csv

for k in range(1, 15):
    a={}
    with open(str(k)+'.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        for i in range(0, 24):
            for j in range(0, 60):
                if i<10 and j<10:
                    c=soup.get_text().count('0'+str(i)+':'+'0'+str(j))
                    if c:
                        a['0'+str(i)+':'+'0'+str(j)]=c
                elif i<10 and j>9:
                    c = soup.get_text().count('0' + str(i) + ':' + str(j))
                    if c:
                        a['0' + str(i) + ':' + str(j)] = c
                elif i>9 and j<10:
                    c = soup.get_text().count(str(i) + ':' + '0'+str(j))
                    if c:
                        a[str(i) + ':' + '0'+str(j)] = c
                else:
                    c = soup.get_text().count(str(i) + ':' + str(j))
                    if c:
                        a[str(i) + ':' + str(j)] = c

    with open(str(k)+'.txt', 'w') as file:
        for i in a:
            file.write(str(i)+','+str(a[i])+'\n')








