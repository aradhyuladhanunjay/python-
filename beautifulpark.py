def solve(n):
    # write your code here
    c=1
    b=1
    print('#.'*n+'#'+'.#'*n)
    for i in range(1,n+1):
        
        
        print('#.'*((n+1)-i)+'.'*(c)+'.#'*((n+1)-i))
    
        c=c+4
    a=c-8
        
    for j in range(1,n):

        
        print('#.'*(j+1)+'.'*(a)+'.#'*(j+1))
        a=a-4
     
    print('#.'*n+'#'+'.#'*n)
print(solve(10))