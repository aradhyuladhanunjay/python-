a=input()
b=input()
a=a[::-1]
b=b[::-1]
c=0
d=0
for i in range(len(a)):
    c=c+2**(i)*(int(a[i]))

for j in range(len(b)):
    d=d+2**(j)*(int(b[j]))


print(c,d)



print(str(bin(c+d))[2:])
