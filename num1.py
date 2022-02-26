n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if l[i]>=0:
        c=c+1
    else:
        continue
print(c)

