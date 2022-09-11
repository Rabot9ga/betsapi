from bs4 import BeautifulSoup
import re

def main(pages_ten):

    a = {}





    for k in range(1, pages_ten):
        with open('html\\' + str(k) + 'tennis.html', 'r', encoding='utf-8') as f:
            print(f)
            soup = BeautifulSoup(f.read(), 'html.parser')
            lst = re.findall(r"\d\d:\d\d", soup.get_text())
            for i in lst:
                if i in a:
                    a[i]+=1
                else:
                    a[i]=1

    with open('final_tennis.txt', 'w') as file:
        for i in a:
            file.write(str(i) + ',' + str(a[i]) + '\n')
