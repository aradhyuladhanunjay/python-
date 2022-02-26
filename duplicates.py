string=input()
b=''
l=[]
for i in string:
    a=string.count(i)
    if a>1 and (i not in b):
        print(i+':'+str(a))
        b=b+i
        l.append(i)

    else:
        continue
if len(b)==0:
    print('Not Exists')

