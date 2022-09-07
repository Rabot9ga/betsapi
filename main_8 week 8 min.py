from bs4 import BeautifulSoup
import csv

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
        for j in b:
            adding_a(j, soup.get_text().count(j))



with open('week_8.txt', 'w') as file:
    for i in a:
        file.write(str(i) + ',' + str(a[i]) + '\n')
