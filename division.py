strs=["flower","flow","flight"]
res=''
for a in zip(*strs):
    if len(set(a)) == 1: 
        res += a[0]
    else: 
        print(res)
print(res)