n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
found=False
key=int(input())
for j in range(len(l)):
    if key==l[j]:
        found=True
        position=j
        break
if found:
    print(position)
else:
    print('No')
