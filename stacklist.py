# stack without limit
class stack:
    def __init__(self):
        self.list=[]
    def __str__(self):
        # values=self.list.reverse()
        values=[str(x) for x in reversed(self.list)]
        return "\n".join(values)
    # isempty
    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False
    # push
    def push(self,value):
        self.list.append(value)
        return "the element has been added to stack"
    def pop(self):
        if self.list==[]:
            return "stack is empty"
        else:
            self.list.pop()
            return "element popped"
    def peek(self):
        if self.list==[]:
            return "stack is empty"
        else:
            return self.list[len(self.list)-1]
    def delete(self):
        self.list=None



# newstack=stack()
# newstack.push(10)
# newstack.push(20)
# newstack.push(30)
# newstack.pop()
# print(newstack.peek())
# print(newstack)
# newstack.delete()
# print(newstack)





# stack with limit
class Stack:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.list=[]
    def __str__(self):
        values=[str(x) for x in reversed(self.list)]
        return "\n".join(values)
    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False
    def isfull(self):
        if len(self.list)==self.maxsize:
            return True
        else:
            return False
    def push(self,value):
        if self.isfull():
            return "stack is full"
        else:
            self.list.append(value)
    def pop(self):
        if self.list==[]:
            return "stack is empty"
        else:
            self.list.pop()
    def peek(self):
        if self.list==[]:
            return "stack is empty"
        else:
            return self.list[len(self.list)-1]
    def delete(self):
        self.list=None
new=Stack(5)
print(new.isempty())
new.push(10)
new.push(20)
new.push(30)
new.push(40)
new.push(50)
print(new.isfull())
new.pop()
print(new.peek())
print(new)
# 





















































































































































        
