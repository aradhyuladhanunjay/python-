s=input()
if (len(s))%2==0:
    print('NO PATTERN')
else:
    a=len(s)//2
    b=''
    for i in range(a,len(s)):
        b=b+s[i]
        print(b)
    for j in range(len(s[:a])):
        b=b+s[j]
        print(b)

