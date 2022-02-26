def isValid(s: str) -> bool:
    match = {'[':']', '{':'}', '(':')'}
    parlist = []
    for i in s:
        if i in "[{(":
            parlist.insert(0, i)
            s = s.replace(i,'',1)
        try:
            if match[parlist[0]]==i:
                parlist.pop(0)
                s = s.replace(i,'', 1)
        except IndexError:
            return False

    if len(parlist)==0 and s=="":
        return True
    else:
        return False
a=isValid("(){}[]")
print(a)