n=int(input())
n=str(n)
odd=[]
even=[]
for i in range(1,len(n),2):
    odd.append(n[i])
for j in range(0,len(n),2):
    even.append(n[j])
count=0
c=0
for i in odd:
    c=c+int(i)


for j in even:
    count=count+int(j)

print(c-count)