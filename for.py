N=int(input())
b=0
c=1
for i in range(1,N+1):
    b=b+i**2
    c=c*i
if b==c:
    print('Yes')
else:
    print('No')
