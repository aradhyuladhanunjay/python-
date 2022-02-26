num=int(input())
l=list(range(1,num))
left=0
right=len(l)-1
while(left<=right):
    mid=(left+right)//2
    if l[mid]**2==num:
        print(True)
        break
    elif (l[mid]**2)>num:
        right=mid-1
    else:
        left=mid+1
else:
    print(False)




