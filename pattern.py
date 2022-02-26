def solve(n):
    # write your code here
    num=1
    for i in range(0,n):
        for j in range(0,n-i):
            if num>9:num=1 
            print(num,end='')
            num+=1
        print()
print(solve(5))