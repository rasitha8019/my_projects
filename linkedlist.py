class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
# class LinkedList:
#     def __init__(self,value):
#         new_node=Node(value)#O(1)
#         self.head=new_node#O(1)
#         self.tail=new_node#O(1)
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):#OVERALL O(1)
        new_node=Node(value)#O(1)
        if self.head is None:#O(1)
            self.head=new_node#O(1)
            self.tail=new_node
        else:
            self.tail.next=new_node#O(1)
            self.tail=new_node#O(1)
        self.length+=1
    def __str__(self):
        temp=self.head
        result=''
        while temp is not None:
            result+=str(temp.value)
            if temp is not None:
                result+='->'
            temp=temp.next
        return result
    def insert_at_beg(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    def insert_at_end(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def insert_at_pos(self,value,index):
        new_node=Node(value)
        temp=self.head
        for _ in range(index-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
    def traversal(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def search(self,num):
        temp=self.head
        while temp is not None:
            if(num==temp.value):
                return 'element found'
            temp=temp.next
        return 'element not found'
    def get(self,index):
        temp=self.head
        i=0
        while temp is not None:
            if(i==index):
                return temp.value
            i=i+1
            temp=temp.next
        return False
    def set(self,index,value):
        temp=self.head
        i=0
        while temp is not None:
            if(i==index):
                temp.value=value
                return True
            i=i+1
            temp=temp.next
        return False
    def delete_at_beg(self):
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            x=self.head
            self.head=self.head.next
            x.next=None
        self.length-=1
    def delete_at_end(self):
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            x=self.tail
            temp=self.head
            while temp.next is not x:
                temp=temp.next
            temp.next=None
            self.tail=temp
        self.length-=1
    def remove(self,index):
        if index<0 or index>self.length:
            return None
        if index==0:
            temp=self.head
            self.head=temp.next
            temp.next=None
        else:
            temp=self.head
            for i in range(self.length):
                if(i<index-1):
                    temp=temp.next
            pop=temp.next
            temp.next=pop.next
            pop.next=None
            self.length-=1

    def reverse(self):
        # TODO
        temp=self.head
        x=self.head.next
        prevnode=self.head
        while temp is not None:
            temp=temp.next
            x.next=prevnode
            
           

            prevnode=x
        k=self.head
        self.head=self.tail
        self.tail=k

    def removeElements()
            
                
        
        



            
        
        
        

        

new=LinkedList()
new.append(10)
new.append(20)
new.append(30)
new.insert_at_beg(0)
new.insert_at_end(100)
new.insert_at_pos(150,3)
new.traversal()
print(new.search(150))
print(new.get(9))
new.set(3,189)
new.delete_at_beg()
new.delete_at_end()
new.remove(10)
new.reverse()
print(new)
