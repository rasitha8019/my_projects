class Heap:
    def __init__(self,size):
        self.list=(size+1)*[None]
        self.heapsize=0
        self.maxsize=size+1
def peek(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.list[1]
def size_of_heap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapsize
def levelorder(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapsize+1):
            print(rootNode.list[i])
def heapify_insert(rootNode,index,heaptype):
    parentindex=int(index/2)
    if index<=1:
        return
    if heaptype=="min":
        if rootNode.list[index]<rootNode.list[parentindex]:
            temp=rootNode.list[index]
            rootNode.list[index]=rootNode.list[parentindex]
            rootNode.list[parentindex]=temp
        heapify_insert(rootNode,parentindex,heaptype)
    elif heaptype=="max":
        if rootNode.list[index]>rootNode.list[parentindex]:
            temp=rootNode.list[index]
            rootNode.list[index]=rootNode.list[parentindex]
            rootNode.list[parentindex]=temp
        heapify_insert(rootNode,parentindex,heaptype)

def insert(rootNode,value,heaptype):
    if rootNode.heapsize+1==rootNode.maxsize:
        return "list is full"
    rootNode.list[rootNode.heapsize+1]=value
    rootNode.heapsize+=1
    heapify_insert(rootNode,rootNode.heapsize,heaptype)

def heapify_of_extract(rootNode,index,heaptype):
    leftindex=index*2
    rightindex=index*2+1
    swapchild=0
    if rootNode.heapsize<leftindex:
        return
    elif rootNode.heapsize==leftindex:
        if heaptype=="min":
            if rootNode.list[index]>rootNode.list[leftindex]:
                temp=rootNode.list[index]
                rootNode.list[index]=rootNode.list[leftindex]
                rootNode.list[leftindex]=temp
            return
        else:
            if rootNode.list[index]<rootNode.list[leftindex]:
                temp=rootNode.list[index]
                rootNode.list[index]=rootNode.list[leftindex]
                rootNode.list[leftindex]=temp
            return
    else:
        if heaptype=="min":
            if rootNode.list[leftindex]<rootNode.list[rightindex]:
                swapchild=leftindex
            else:
                swapchild=rightindex
            if rootNode.list[index]>rootNode.list[swapchild]:
                temp=rootNode.list[index]
                rootNode.list[index]=rootNode.list[swapchild]
                rootNode.list[swapchild]=temp
        else:
            if rootNode.list[leftindex]>rootNode.list[rightindex]:
                swapchild=leftindex
            else:
                swapchild=rightindex
            if rootNode.list[index]<rootNode.list[swapchild]:
                temp=rootNode.list[index]
                rootNode.list[index]=rootNode.list[swapchild]
                rootNode.list[swapchild]=temp
    heapify_of_extract(rootNode,swapchild,heaptype)




def extract(rootNode,heaptype):
    if rootNode.heapsize==0:
        return
    else:
        extractNode=rootNode.list[1]
        rootNode.list[1]=rootNode.list[rootNode.heapsize]
        rootNode.list[rootNode.heapsize]=None
        rootNode.heapsize-=1
        heapify_of_extract(rootNode,1,heaptype)
        return extractNode


def delete(rootNode):
    rootNode.list=None   

binaryheap=Heap(5)
insert(binaryheap,4,"max")
insert(binaryheap,5,"max")
insert(binaryheap,2,"max")
insert(binaryheap,1,"max")
print(extract(binaryheap,"max"))
delete(binaryheap)
# levelorder(binaryheap)
# print(size_of_heap(binaryheap))
