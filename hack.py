n=int(input())
l=[]
for i in range(n):
    name=input()
    score=float(input())
    l.append([name,score])
b=[]
for i in range(len(l)):
    b.append(l[i][1])
b=sorted(b)
a=b[-2]
c=b[-3]
A=[]
for i in range(len(l)):
    if a==l[i][1]:
        A.append(l[i][0])
    if c==l[i][1]:
        A.append(l[i][0])
A=sorted(A)
for i in A:
    print(i)

   