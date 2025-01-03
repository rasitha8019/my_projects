class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp=temp.next

class Queue:
    def __init__(self):
        self.linkedlist=LinkedList()
    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return " ".join(values)
    def enqueue(self,value):
        new_node=Node(value)
        if self.linkedlist.head==None:
            self.linkedlist.head=new_node
            self.linkedlist.tail=new_node
        else:
            self.linkedlist.tail.next=new_node
            self.linkedlist.tail=new_node
    def isempty(self):
        if self.linkedlist.head==None:
            return True
        else:
            return False
    def dequeue(self):
        if self.isempty():
            return "Queue is empty"
        elif self.linkedlist.head==self.linkedlist.tail:
            self.linkedlist.head=None
            self.linkedlist.tail=None
        else:
            temp=self.linkedlist.head
            self.linkedlist.head=self.linkedlist.head.next
            temp.next=None
    def peek(self):
        if self.isempty():
            return "Queue is empty"
        else:
            return self.linkedlist.head.value
    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None



new=Queue()
print(new.isempty())
new.enqueue(4)
new.enqueue(3)
new.enqueue(4)
new.dequeue()
print(new.isempty())
print(new.peek())
print(new)
