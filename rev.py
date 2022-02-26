n=int(input())
a='{:032b}'.format(n)
a=str(a)
a=a[::-1]
b=int(a,2)
print(b)