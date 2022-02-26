str=input()
sub_str=input()
lst=[]
for i in str:
    lst.append(i)

while len(str)!=0 and sub_str in str:
    for i in sub_str:
        lst.remove(i)
    str="".join(lst)
    
if len(str)==0:
    print("Yes")
else:    
    print("No")