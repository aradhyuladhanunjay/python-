n=int(input())
s=0
fact=1
if n==1:
    print(0)
else:
    for i in range(1,n+1):
        fact=fact*i
fact=str(fact)
for i in range(len(fact)-1,0,-1):
    if fact[i]=="0":
        s=s+1
    elif fact[i]!='0':
        break
print(s)