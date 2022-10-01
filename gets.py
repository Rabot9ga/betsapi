import tkinter, tkinter.messagebox
import requests
import main
import main_tennis
import counting_pages

root=tkinter.Tk()
root.geometry('500x200')


canvas=tkinter.Canvas(root, height=500, width=200)
canvas.pack()

frame=tkinter.Frame(root)
frame.place(relwidth=1, relheight=1)


title=tkinter.Label(frame, text='cookie: ', font=50)
title.place(x=10, y=10)


# title=tkinter.Label(frame, text='pages soccer: ', font=50)
# title.place(x=10, y=40)
# pagessoccerField=tkinter.Entry(frame, bg='white', width=60)
# pagessoccerField.place(x=120, y=42)
#
#
#
# title=tkinter.Label(frame, text='pages tennis: ', font=50)
# title.place(x=10, y=70)
# pagestenField=tkinter.Entry(frame, bg='white', width=60)
# pagestenField.place(x=120, y=72)



cookieField=tkinter.Entry(frame, bg='white', width=60)
cookieField.place(x=120, y=12)





def button_main():
    cookies = cookieField.get()
    pages_soc = counting_pages.searching_pages_count_football(cookies)
    pages_ten = counting_pages.searching_pages_count_tennis(cookies)
    print(pages_soc, pages_ten, cookies)

    header = {
        'cookie': cookies,
        # 'cookie': '_ga=GA1.1.2063520179.1661428584; sid=kr9bs082sb25ov9rana9d2nqmb; tz=Europe%2FMoscow; _ga_1LTT3CXFKZ=GS1.1.1662356892.27.1.1662357003.0.0.0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'upgrade-insecure-requests': '1'
    }


    for i in range(1, pages_soc+1):
        req = requests.get('https://betsapi.com/cs/soccer/p.' + str(i) + '?skipE=1', headers=header)
        print('https://betsapi.com/cs/soccer/p.' + str(i) + '?skipE=1')
        with open('html\\' + str(i) + '.html', 'w', encoding='utf-8') as file:
            file.write(req.text)

    main.main(pages_soc+1)

    for i in range(1, pages_ten+1):
        req = requests.get('https://betsapi.com/cs/tennis/p.' + str(i), headers=header)
        print('https://betsapi.com/cs/tennis/p.' + str(i))
        with open('html\\' + str(i) + 'tennis.html', 'w', encoding='utf-8') as file:
            file.write(req.text)

    main_tennis.main(pages_ten+1)
    tkinter.messagebox.showinfo(title='Success', message='Time for tennis and soccer is created')

btn=tkinter.Button(frame, text='Create results', width=30, command=button_main)
btn.place(x=150, y=150)


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






root.mainloop()