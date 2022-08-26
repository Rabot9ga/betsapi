from bs4 import BeautifulSoup
import csv

a={}
with open('6.html', 'r') as f:
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

with open('6.txt', 'w') as file:
    for i in a:
        file.write(str(i)+','+str(a[i])+'\n')







