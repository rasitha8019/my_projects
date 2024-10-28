class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return f"{self.value}->{self.next}"
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    def __str__(self):
        temp=self.head
        result=""
        while temp is not None:
            result=result+str(temp.value)
            temp=temp.next
            if(temp==None):
                break
            result=result+"->"
        return result
    def prepend(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
    def traversal(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def reverse_traverse(self):
        temp=self.tail
        while temp is not None:
            print(temp.value)
            temp=temp.prev
    def search(self,number):
        temp=self.head
        while temp is not None:
            if (temp.value==number):
                return "number found"
            temp=temp.next
        return "number not found"
    def get(self,index):
        if index<0 and index>=self.length:
            return None
        temp=self.head
        if index<((self.length+1)//2):
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    def set(self,index,number):
        if index<0 and index>=self.length:
            return None
        temp=self.head
        if index<((self.length+1)//2):
            temp=self.head
            for _ in range(index):
                temp=temp.next
            temp.value=number
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
            temp.value=number
    def insert(self,index,number):
        new_node=Node(number)
        if(index<0 and index>=self.length):
            return
        elif index==0:
            self.prepend(number)
            return
        elif self.length==0:
            self.head=new_node
            self.tail=new_node
        elif index==self.length:
            self.append(number)
            return 

        else:
            temp=self.get(index-1)
            new_node.next=temp.next
            new_node.prev=temp
            temp.next.prev=new_node
            temp.next=new_node
            self.length+=1
    def del_at_beg(self):
        if(self.length==1):
            self.head=None
            self.tail=None
        else:
            pop=self.head
            temp=self.head.next
            temp.prev=None
            self.head=temp
            pop.next=None
            pop.prev=None
        self.length-=1
    def del_at_end(self):
        if(self.length==1):
            self.head=None
            self.tail=None
        else:
            pop=self.tail
            temp=self.tail.prev
            temp.next=None
            self.tail=temp
            pop.prev=None
        self.length-=1
    def remove(self,index):
        if(index==0):
            self.head=self.head.next
        elif(index==self.length):
            self.del_at_end()
            
        else:
            temp=self.get(index)
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
            temp.prev=None
            temp.next=None
        self.length-=1



        



            

        


new=DoublyLinkedList()
new.append(10)
new.append(20)
new.append(30)
new.append(40)
new.append(50)
new.prepend(0)
new.traversal()
new.reverse_traverse()
print(new.search(300))
print(new.get(30))
new.insert(6,900)
new.del_at_beg()
new.del_at_end()
new.remove(4)
print(new)
