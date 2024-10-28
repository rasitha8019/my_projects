class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class DCLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0 
    def append(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            self.tail.next=new_node
            self.head.prev=new_node
            new_node.prev=self.tail
            new_node.next=self.head
            self.tail=new_node
        self.length+=1
    def __str__(self):
        temp=self.head
        result=''
        while temp is not None:
            result=result+str(temp.value)
            temp=temp.next
            if(temp==self.head):
                break
            result=result+'->'
        return result
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            new_node.next=self.head
            new_node.prev=self.tail
            self.tail.next=new_node
            self.head=new_node
        self.length+=1
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
            if(temp==self.head):
                break
    def traverse_reverse(self):
        temp=self.tail
        while temp is not None:
            print(temp.value)
            temp=temp.prev
            if(temp==self.tail):
                break
    def search(self,number):
        temp=self.head
        while temp:
            if(temp.value==number):
                return 'number found'
            temp=temp.next
            if(temp==self.head):
                break
        return 'number not found'
        



new=DCLinkedList()
new.append(10)
new.append(20)
new.append(30)
new.prepend(0)
new.traverse()
new.traverse_reverse()
print(new.search(200))
print(new)


    
