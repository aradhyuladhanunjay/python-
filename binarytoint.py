n=bin(int(input()))
s=str(n[2:])
a=0
j=0
for i in range((len(s))-1,-1,-1):
    a=a+int(s[i])*(2**(j))
    j=j+1
print(a)

