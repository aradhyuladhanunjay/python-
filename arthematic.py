def solve(A):
    # write your code here
    a=A[1]-A[0]
    c=0
    b=0
    for i in range(len(A)):
        if i==len(A)-1:
            b+=1
            break
        if a==A[i+1]-A[i]:
            c+=1
        else:
            return "Normal Series"
    if c==(len(A))-1:
        return True
    if b==1:
        return 'Normal Series'
print(solve([2,4,6,8,10]))