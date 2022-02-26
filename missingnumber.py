l=list(map(int,input().split()))
flag=True
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
            flag=False
    if flag:
        break
print(l)