s=input()
d=dict({})
for i in s:
    a=s.count(i)
    d[i]=a
b=max(d.values())
for j in d.keys():
    if d[j]==b:
        print(j)
        break
    else:
        continue
