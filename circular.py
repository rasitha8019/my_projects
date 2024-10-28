class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class CircularList:
    # empty node
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    # single node
    # def __init__(self,value):
    #     new_node=Node(value)
    #     self.head=new_node
    #     self.tail=new_node
    #     new_node.next=self.head
    #     self.length=1
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1
    def __str__(self):
        temp=self.head
        result=""
        while temp is not None:
            result+=str(temp.value)
            temp=temp.next
            if temp==self.head:
                break
            result+='->'
        return result

       
    def insert_at_beg(self,value):
         new_node=Node(value)
         new_node.next=self.head
         self.head=new_node
         self.tail.next=new_node
    def insert_at_pos(self,index,value):
        new_node=Node(value)
        temp=self.head
        if index>self.length:
            return None
        if self.length==0:
            new_node.next=new_node
            self.head=new_node
            self.tail=new_node
        if index==0:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        elif index==self.length:
            self.tail.next=new_node
            self.tail=new_node
            new_node.next=self.head
        else:
            for _ in range(index-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
        self.length+=1
    def traversal(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
            if(temp==self.head):
                return
    def search(self,num):
        temp=self.head
        while temp is not None:
            if temp.value==num:
                return "number found"
            temp=temp.next
            if(temp==self.head):
                return "number not found"
    def get(self,index):
        temp=self.head
        if index<-1 and index>self.length:
            return 
        elif index==-1:
            return self.tail.value
        for _ in range(index):
            temp=temp.next
            if temp==self.head:
                return
        return temp.value
    def set(self,index,number):
        temp=self.head
        if index<-1 and index>self.length:
            return 
        elif index==-1:
            self.tail.value=number
        for _ in range(index):
            temp=temp.next
            if temp==self.head:
                return
        temp.value=number
    def del_at_beg(self):
        if self.length==0:
            return
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head 
            self.head=temp.next
            self.tail.next=self.head
            temp.next=None
        self.length-=1
    def del_at_end(self):
        if self.length==0:
            return
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            x=self.tail
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            x.next=None
        self.length-=1
    def remove(self,index):
        temp=self.head
        for _ in range(index):
            temp=temp.next
            if temp==self.head:
                break
        d=temp.next
        temp.next=d.next
        d.next=None
        self.length-=1



        



        
new=CircularList()
new.append(20)
new.append(30)
new.append(40)
new.insert_at_beg(10)
new.insert_at_pos(3,100)
new.insert_at_pos(4,150)
new.traversal()
new.set(4,50)
print(new.search(40))
new.del_at_beg()
new.del_at_end()
new.remove(3)
print(new)
print(new.get(-1))