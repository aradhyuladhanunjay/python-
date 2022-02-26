def fact(N):
    if N==0:
        return 1
    else:
        return N*fact(N-1)
def sum_sqres(N):
    count=0
    for i in range(1,N+1):
        count=count+i**2
    return count
N=int(input())
a=fact(N)
b=sum_sqres(N)
print(a)
print(b)

if a==b:
    print('Yes')
else:
    print('No')