def happy(n:int):
    a=0
    if(n!=1):
        while(n!=0):
            r=n%10
            a=a+r**2
            n=n//10
    else:
        return True
    if len(str(a))>1:
        return happy(a)
    if a==7:
        return happy(a)
    if a==1:
        return True
    else:
        return False
print(happy(2))