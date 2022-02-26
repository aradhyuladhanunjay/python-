strs=["dhanunjayarao","dhanunjay","dhanu",'syam']
s=[]
for j in strs:
    s.append(len(j))
a=''
for k in range(len(strs)):
    for i in range(min(s)):
        if strs[0][i]==strs[1][i]==strs[2][i]:
            a=a+strs[0][i]
        else:
            break
if len(a)!=0:
    print(a)
else:
    print('')