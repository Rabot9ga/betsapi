a={}

with open('concat.txt', 'r') as f:
    for i in f.readlines():
        splited=i.rstrip().split(',')
        if splited[0] not in a:
            a[splited[0]]=int(splited[1])
        else:
            a[splited[0]]+=int(splited[1])

with open('fin.txt', 'w') as file:
    for i in a:
        file.writelines(i+','+str(a[i])+'\n')
