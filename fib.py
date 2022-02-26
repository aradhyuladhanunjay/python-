l=[]
def fib(n):
    a=0
    b=1
    if n==0:
        l.append(0)
    elif n==1:
        l.append(1)
    else:
        for i in range(0,n):
            c=a+b
            a=b
            b=c
        l.append(a)
    return l
n=input()
a={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
for i in range(len(n)):
    if n[i] in a.keys():
        fib(a[n[i]])
    else:
        continue
print(sum(l))


