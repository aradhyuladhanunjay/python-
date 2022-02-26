def solve(n):
    # write your code here
    previous =' 1 '
    present=''
    if n==1:
        print(previous)
    else:
        for i in range(2,n+1):
            present=previous+str(i)+previous
            previous=present
        print(present[1:-1])
print(solve(7),end="\t")