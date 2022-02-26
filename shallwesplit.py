def solve(A):
    # write your code here
    for i in range(1,len(A)-1):
        a=A[:i]
        b=A[i:]
        if sum(a)==sum(b):
            print(True)

print(solve([10,5,3,1,1,1,1,1,1,12]))