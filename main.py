from bs4 import BeautifulSoup
import re



def main(pages_football):
    a = {}




    for k in range(1, pages_football):
        with open('html\\' + str(k) + '.html', 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            lst=re.findall(r"\d\d:\d\d", soup.get_text())
            for i in lst:
                if i in a:
                    a[i]+=1
                else:
                    a[i]=1


    with open('final.txt', 'w') as file:
        for i in a:
            file.write(str(i) + ',' + str(a[i]) + '\n')

