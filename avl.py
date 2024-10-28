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
        else:
            temp=self.linkedlist.head
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=self.linkedlist.head.next
            return temp








class AVLNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        self.height=1
def preorder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorder(rootNode.leftchild)
    preorder(rootNode.rightchild)
def inorder(rootNode):
    if not rootNode:
        return
    inorder(rootNode.leftchild)
    print(rootNode.data)
    inorder(rootNode.rightchild)
def postorder(rootNode):
    if not rootNode:
        return
    postorder(rootNode.leftchild)
    postorder(rootNode.rightchild)
    print(rootNode.data)
def levelorder(rootNode):
    if not rootNode:
        return
    else:
        que=Queue()
        que.enqueue(rootNode)
        while not(que.isempty()):
            root=que.dequeue()
            print(root.value.data)
            if(root.value.leftchild is not None):
                que.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                que.enqueue(root.value.rightchild)
def search(rootNode,value):
    if rootNode.data==value:
        print("found")
    elif(value<rootNode.data):
        if rootNode.leftchild.data==value:
            print('found')
        else:
            search(rootNode.leftchild,value)
    else:
        if rootNode.rightchild.data==value:
            print("found")
        else:
            search(rootNode.rightchild,value)
def getheight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height
def rightrotate(disbalancedNode):
    newRoot=disbalancedNode.leftchild
    disbalancedNode.leftchild=disbalancedNode.leftchild.rightchild
    newRoot.rightchild=disbalancedNode
    disbalancedNode.height=1+max(getheight(disbalancedNode.leftchild),getheight(disbalancedNode.rightchild))
    newRoot.height=1+max(getheight(newRoot.leftchild),getheight(newRoot.rightchild))
    return newRoot
def leftrotate(disbalancedNode):
    newRoot=disbalancedNode.rightchild
    disbalancedNode.rightchild=disbalancedNode.rightchild.leftchild
    newRoot.leftchild=disbalancedNode
    disbalancedNode.height=1+max(getheight(disbalancedNode.leftchild),getheight(disbalancedNode.rightchild))
    newRoot.height=1+max(getheight(newRoot.leftchild),getheight(newRoot.rightchild))
    return newRoot
def getBalance(rootNode):
    if not rootNode:
        return
    return getheight(rootNode.leftchild)-getheight(rootNode.rightchild)
def insertNode(rootNode,value):
    if not rootNode:
        return  AVLNode(value)
    elif value<rootNode.data:
        rootNode.leftchild=insertNode(rootNode.leftchild,value)
    else:
        rootNode.rightchild=insertNode(rootNode.rightchild,value)
    rootNode.height=1 + max(getheight(rootNode.leftchild),getheight(rootNode.rightchild))
    balance=getBalance(rootNode)
    if (balance>1 and value<rootNode.leftchild.data):
        return rightrotate(rootNode)
    if balance>1 and value>rootNode.leftchild.data:
        rootNode.leftchild=leftrotate(rootNode.leftchild)
        return rightrotate(rootNode)
    if balance<-1 and value>rootNode.rightchild.data:
        return leftrotate(rootNode)
    if balance<-1 and value<rootNode.rightchild.data:
        rootNode.rightchild=rightrotate(rootNode.rightchild)
        return leftrotate(rootNode)
    return rootNode
def successor(rootNode):
    if rootNode is None or rootNode.leftchild is None:
        return rootNode
    return successor(rootNode.leftchild)
def delete(rootNode,value):
    if not rootNode:
        return
    elif value<rootNode.data:
        rootNode.leftchild=delete(rootNode.leftchild,value)
    elif value>rootNode.data:
        rootNode.rightchild=delete(rootNode.rightchild,value)
    else:
        if rootNode.leftchild is None:
            temp=rootNode.rightchild
            rootNode=temp
            return temp
        elif rootNode.rightchild is None:
            temp=rootNode.leftchild
            rootNode=temp
            return temp
        temp=successor(rootNode.rightchild)
        rootNode.data=temp.data
        rootNode.rightchild=delete(rootNode.rightchild,temp.data)

    balance=getBalance(rootNode)
    if balance>1 and getBalance(rootNode.leftchild)>=0:
        return rightrotate(rootNode)
    if balance<-1 and getBalance(rootNode.rightchild)<=0:
        return leftrotate(rootNode)
    if balance>1 and getBalance(rootNode.leftchild)<0:
        rootNode.leftchild=leftrotate(rootNode.leftchild)
        return rightrotate(rootNode)
    if balance<-1 and getBalance(rootNode.rightchild)>0:
        rootNode.rightchild=rightrotate(rootNode.rightchild)
        return leftrotate(rootNode)
    return rootNode
        
def delete_full(rootNode):
    rootNode.data=None
    rootNode.leftchild=None
    rootNode.rightchild=None
    return "full tree delete" 
        

    
newAVL=AVLNode(5)
newAVL=insertNode(newAVL,10)
newAVL=insertNode(newAVL,15)
newAVL=insertNode(newAVL,20)
newAVL=delete(newAVL,15)
print(delete_full(newAVL))
levelorder(newAVL)
            
