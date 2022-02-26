def solve(n):
    # write your code here
    a=0
    b=1
    l=[0,1]
    if n==0:
        return 0
    elif n==1:
        return l
    else:
        for j in range(1,n):
            c=a+b
            l.append(c)
            a=b
            b=c
        return l

print(solve(13))