
def fact(a:int):
    if (a==0):
        return 1
    else:
        return a*fact(a-1)
    f=str(fact)
    for i in range(len(f)-1,0,-1):
        if fact[i]=="0":
            s=s+1
        elif fact[i]!='0':
            break
    print(s)
print(fact(5))
