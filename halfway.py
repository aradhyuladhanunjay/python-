n=int(input())
l=list(map(int,input().split()))
a=sorted(l[0:(len(l)//2)])
b=sorted(l[(len(l)//2):])
b=reversed(b)
for i in b:
    a.append(i)
for j in a:
    print(j,end=' ')