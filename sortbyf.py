import collections
n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if l.count(i)==1:
        a.append(i)
    else:
        b.append(i)
a=sorted(a)
occ=collections.Counter(b)

