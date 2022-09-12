import os

try:
    path_f = os.path.abspath('final.txt')
    os.remove(path_f)
except:
    print('File is deleted')

try:
    path_t = os.path.abspath('final_tennis.txt')
    os.remove(path_t)
except:
    print('File is deleted')


for root, dirs, files in os.walk("html"):
    for filename in files:
        try:
            os.remove(os.path.abspath(root)+'\\'+filename)
        except:
            print('File is deleted')



