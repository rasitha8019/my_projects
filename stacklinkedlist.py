class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.length=0
    def __iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp=temp.next
    
class Stack:
    def __init__(self):
        self.Linkedlist=Linkedlist()
    def __str__(self):
        values=[str(x.value) for x in self.Linkedlist]
        return "\n".join(values)
    def push(self,value):
        new_node=Node(value)
        if self.Linkedlist.length==0:
            self.Linkedlist.head=new_node
        else:
            new_node.next=self.Linkedlist.head
            self.Linkedlist.head=new_node
        self.Linkedlist.length+=1
    def pop(self):
        if self.Linkedlist.length==0:
            return "stack is empty"
        elif self.Linkedlist.length==1:
            self.head=None
            self.Linkedlist.length-=1
        else:
            temp=self.Linkedlist.head
            self.Linkedlist.head=self.Linkedlist.head.next
            temp.next=None
    def peek(self):
        if self.Linkedlist.length==0:
            return "stack is empty"
        else:
            return self.Linkedlist.head.value
    def isempty(self):
        if self.Linkedlist.length==0 or self.Linkedlist.head==None:
            return True
        else:
            return False
    def delete(self):
        self.Linkedlist.head=None



new=Stack()
new.push(5)
new.push(4)
new.push(6)
new.push(7)
new.pop()
print(new.isempty())
print(new)
print(new.peek())
