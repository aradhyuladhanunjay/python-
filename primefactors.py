import math
def solve(n):
    # write your code here
    if n>1:
        p=[]
        while n%2==0:
            p.append(2)
            n=n/2
        for i in range(3,int(math.sqrt(n)+1),2):
            while n%i==0:
                  p.append(i)
                  n=n/i
        if n>2:
            p.append(n)
        p=sorted(p)
        for i in p:
            print(int(i),end=' ')
print(solve(30))