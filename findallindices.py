l=list(map(int,input().split(" ")))
for i in range(len(l)):
    for j in range(len(l)-i-1):
         if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
         else:
                continue
a=[]
for i in range(len(l)):
    if l[i]==2:
        a.append(i)
print(sorted(a))


