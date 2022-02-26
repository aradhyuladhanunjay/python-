class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,val:int):
        self.stack.insert(0,val)
        return self.stack
       
    def pop(self):
        if(len(self.stack)!=0 or self.stack):
            self.stack.pop(0)
            return self.stack
        else:
            return "stack is under flow"
    def minval(self):
        return min(self.stack)
    def add(self,a=[]):
        for i in range(len(a)):
            self.stack.insert(0,a[i])
        return self.stack
    def maxval(self):
        return max(self.stack)

s=Stack()
print(s.add([1,2,3,4,5]))
print(s.push(6))
print(s.pop())
print(s.minval())
print(s.maxval())

