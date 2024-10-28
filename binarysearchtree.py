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






class BSTnode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
def insert(rootNode,nodeValue):
    if rootNode.data==None:
        rootNode.data=nodeValue
    elif nodeValue<=rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild=BSTnode(nodeValue)
        else:
            insert(rootNode.leftchild,nodeValue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild=BSTnode(nodeValue)
        else:
            insert(rootNode.rightchild,nodeValue)
    return "inserted"
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
            if root.value.leftchild is not None:
                que.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                que.enqueue(root.value.rightchild)
def search(rootNode,nodeValue):
    if rootNode.data==nodeValue:
        print("found")
    elif nodeValue<rootNode.data:
        if rootNode.leftchild.data==nodeValue:
            print("found")
        else:
            search(rootNode.leftchild,nodeValue)
    else:
        if rootNode.rightchild.data==nodeValue:
            print("found")
        else:
            search(rootNode.rightchild,nodeValue)
def successor(bstNode):
    current=bstNode
    while (current.leftchild is not None):
        current=current.leftchild
    return current
def delete(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue<rootNode.data:
        rootNode.leftChild=delete(rootNode.leftchild,nodeValue)
    elif nodeValue>rootNode.data:
        rootNode.rightchild=delete(rootNode.rightchild,nodeValue)
    else:
        if rootNode.leftchild is None:
            temp=rootNode.rightchild
            rootNode=None
            return temp
        if rootNode.rightchild is None:
            temp=rootNode.leftchild
            rootNode=None
            return temp
        temp=successor(rootNode.rightchild)
        rootNode.data=temp.data
        rootNode.rightchild=delete(rootNode.rightchild,temp.data)
    return rootNode
def delete_total(rootNode):
    rootNode.data=None
    rootNode.leftchild=None
    rootNode.rightchild=None 


    

newBST=BSTnode(None)
print(insert(newBST,70))
print(insert(newBST,40))
print(insert(newBST,90))
print(newBST.data)
print(newBST.leftchild.data)
preorder(newBST)
inorder(newBST)
postorder(newBST)
levelorder(newBST)
search(newBST,40)
print(delete(newBST,70).data)
