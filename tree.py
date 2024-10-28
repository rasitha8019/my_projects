# class Treenode:
#     def __init__(self,data,children=[]):
#         self.data=data
#         self.children=children
#     def __str__(self,level=0):
#         ret=" "*level+str(self.data)+"\n"
#         for child in self.children:
#             ret+=child.__str__(level+1)
#         return ret
#     def addchild(self,Treenode):
#         self.children.append(Treenode)
# tree=Treenode("a",[])
# cold=Treenode("b",[])
# hot=Treenode("c",[])
# tree.addchild(cold)
# tree.addchild(hot)
# print(tree)






# BINARY TREE
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
        
            
    def peek(self):
        if self.isempty():
            return "Queue is empty"
        else:
            return self.linkedlist.head.value
    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None






class Treenode:
    def __init__(self,data):
        self.leftchild=None
        self.data=data
        self.rightchild=None
newTree=Treenode("parent")
leftchild=Treenode("hot")
rightchild=Treenode("cold")
newTree.leftchild=leftchild
newTree.rightchild=rightchild
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
    preorder(rootNode.leftchild)
    preorder(rootNode.rightchild)
    print(rootNode.data)
def levelorder(rootNode):
    if not rootNode:
        return
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isempty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)
def serching(rootNode,value):
    if not rootNode:
        return "no tree"
    else:
        que=Queue()
        que.enqueue(rootNode)
        while not(que.isempty()):
            root=que.dequeue()
            if (root.value.data==value):
                return "found"
            if root.value.leftchild is not None:
                que.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                que.enqueue(root.value.rightchild)
        return  "not found"
def insert(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
    else:
        que=Queue()
        que.enqueue(rootNode)
        while not(que.isempty()):
            root=que.dequeue()
            if root.value.leftchild is not None:
                que.enqueue(root.value.leftchild)
            else:
                root.value.leftchild=newNode
                return "inserted l"
            if root.value.rightchild is not None:
                que.enqueue(root.value.rightchild)
            else:
                root.value.rightchild=newNode
                return "inserted r"
def getdeepestNode(rootNode):
    if not rootNode:
        return 
    else:
        que=Queue()
        que.enqueue(rootNode)
        while not(que.isempty()):
            root=que.dequeue()
            if root.value.leftchild is not None:
                que.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                que.enqueue(root.value.rightchild)
        deepestNode=root.value
        return deepestNode
def deletedeepest(rootNode,dNode):
    if not rootNode:
        return
    else:
        que=Queue()
        que.enqueue(rootNode)
        while not (que.isempty()):
            root=que.dequeue()
            if root.value is dNode:
                root.value=None
                return
            if root.value.rightchild is not None:
                if root.value.rightchild is dNode:
                    root.value.rightchild=None
                    return
                else:
                    que.enqueue(root.value.rightchild)
            if root.value.leftchild is not None:
                if root.value.leftchild is dNode:
                    root.value.leftchild=None
                    return
                else:
                    que.enqueue(root.value.leftchild)
def deleteNodeBT(rootNode,node):
    if not rootNode:
        return "no Tree"
    else:
        que=Queue()
        que.enqueue(rootNode)
        while not(que.isempty()):
            root=que.dequeue()
            if root.value.data==node:
                dNode=getdeepestNode(rootNode)
                root.value.data=dNode.data
                deletedeepest(rootNode,dNode)
                return "deleted"
            if root.value.leftchild is not None:
                que.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                que.enqueue(root.value.rightchild)
        return "failed"
def delete(rootNode):
    rootNode.data=None
    rootNode.leftchild=None
    rootNode.rightchild=None
    return "deleted"



# print(inorder(newTree))
# print(postorder(newTree))
# newNode=Treenode("coffee")
# print(insert(newTree,newNode))
# newNode=Treenode("boost")
# print(insert(newTree,newNode))
# print(levelorder(newTree))
# print(preorder(newTree))
# print(serching(newTree,"cold"))
# n=getdeepestNode(newTree)
# deletedeepest(newTree,n)
# print(getdeepestNode(newTree).data)
# print(deleteNodeBT(newTree,"cold"))
# print(delete(newTree))
# print(preorder(newTree))










#using python list
class BinaryTree:
    def __init__(self,size):
        self.list=size*[None]
        self.lastusedindex=0
        self.maxSize=size
    def insertNode(self,value):
        if self.lastusedindex+1==self.maxSize:
            return "tree is full"
        self.list[self.lastusedindex+1]=value
        self.lastusedindex+=1
        return "inserted"
    def search(self,value):
        for i in range(len(self.list)):
            if self.list[i]==value:
                return "found"
        return "not found"
    def preorder(self,index):
        if index>self.lastusedindex:
            return
        print(self.list[index])
        self.preorder(index*2)
        self.preorder(index*2+1)
    def inorder(self,index):
        if index>self.lastusedindex:
            return
        self.inorder(index*2)
        print(self.list[index])
        self.inorder(index*2+1)
    def postorder(self,index):
        if index>self.lastusedindex:
            return
        self.postorder(index*2)
        self.postorder(index*2+1)
        print(self.list[index])
    def levelorder(self,index):
        for i in range(index,len(self.list)):
            print(self.list[i])
    def delete(self,value):
        if self.lastusedindex==0:
            return "no tree"
        for i in range(1,self.lastusedindex+1):
            if self.list[i]==value:
                self.list[i]=self.list[self.lastusedindex]
                self.list[self.lastusedindex]=None
                self.lastusedindex-=1
                return "deleted"
    def deletetotal(self):
        self.list=None
        return "deleted"



    


newBT=BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("hot")
newBT.insertNode("cold")
newBT.insertNode("tea")
newBT.insertNode("coffee")
newBT.insertNode("sprite")
newBT.insertNode("limca")
print(newBT.search("tea"))
newBT.preorder(1)
newBT.inorder(1)
newBT.postorder(1)
newBT.levelorder(1)
print(newBT.delete("hot"))
# print(newBT.deletetotal())
newBT.levelorder(1)