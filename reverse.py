import math
def sumsquares(num:int):
    if(num==1):
        return True
    a=math.sqrt(num)
    a=str(a)    
    if a[-1]=="0":
        return True
    else:
        l=range(1,int(math.sqrt(num)))
        left=0
        right=len(l)-1
        while(left<=right):
            if l[left]**2+l[right]**2==num:
                return True
            elif(l[left]**2+l[right]**2)>num:
                right-=1
            else:
                left+=1
        else:
            return False
print(sumsquares(5))
                



