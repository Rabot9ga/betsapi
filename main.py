from bs4 import BeautifulSoup
import csv

a = {}


def adding_a(time, c):
    if time in a:
        a[time] += c
    else:
        a[time] = c


for k in range(1, 10):
    with open('html\\' + str(k) + '.html', 'r', encoding='utf-8') as f:
        print(f)
        soup = BeautifulSoup(f.read(), 'html.parser')
        for i in range(0, 24):
            for j in range(0, 60):
                if i < 10 and j < 10:
                    c = soup.get_text().count('0' + str(i) + ':' + '0' + str(j))
                    time = '0' + str(i) + ':' + '0' + str(j)
                    if c:
                        adding_a(time, c)
                elif i < 10 and j > 9:
                    c = soup.get_text().count('0' + str(i) + ':' + str(j))
                    time = '0' + str(i) + ':' + str(j)
                    if c:
                        adding_a(time, c)
                elif i > 9 and j < 10:
                    c = soup.get_text().count(str(i) + ':' + '0' + str(j))
                    time = str(i) + ':' + '0' + str(j)
                    if c:
                        adding_a(time, c)
                else:
                    c = soup.get_text().count(str(i) + ':' + str(j))
                    time = str(i) + ':' + str(j)
                    if c:
                        adding_a(time, c)

with open('final.txt', 'w') as file:
    for i in a:
        file.write(str(i) + ',' + str(a[i]) + '\n')
