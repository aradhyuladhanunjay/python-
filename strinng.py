n=input()
n=list(n.split(' '))
s=''
for i in range(len(n)):
    if n.count(n[i])>1 and (n[i] not in s) :
        s=s+n[i]+' '
    else:
        continue
if len(s)!=0:
    print(s)
else:
    print('NA')