def addDigit(nums:int):
    a=0
    while(nums!=0):
        r=nums%10
        a=a+r
        nums=nums//10
    if len(str(a))>1:
        return addDigit(a)
    else:
        return a    
print(addDigit(879))