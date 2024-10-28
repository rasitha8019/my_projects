class Queue:
    def __init__(self):
        self.items=[]
    def __str__(self):
        values=[str(x) for x in self.items]
        return " ".join(values)
    def isempty(self):
        if self.items==[]:
            return True
        else:
            return False
    def enqueue(self,value):
        self.items.append(value)
        return "element appended"
    def dequeue(self):
        if self.isempty():
            return "Queue is empty"
        else:
            self.items.pop(0)
    def peek(self):
        if self.isempty():
            return "Queue is empty"
        else:
            return self.items[0]
    def delete(self):
        self.items=None

# new=Queue()
# new.enqueue(10)
# new.enqueue(20)
# new.enqueue(30)
# new.enqueue(40)
# print(new.peek())
# print(new.isempty())
# print(new)
# new.dequeue()
# print(new)





# Queue with limit
class queue:
    def __init__(self,maxsize):
        self.items=maxsize*None
        self.maxsize=maxsize
        self.start=-1
        self.top=-1
    def __str__(self):
        values=[str(x) for x in self.items]
        return " ".join(values)
    def isfull(self):
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top+1==self.maxsize:
            return True
        else:
            return False
    def isempty(self):
        if self.top==-1:
            return True
        else:
            return  False
    def enqueue(self,value):
        if self.isfull():
            return "the queue is full"
        else:
            if self.top+1==self.maxsize:
                self.top=0
            else:
                self.top+=1
                if self.start == -1:
                    self.start=0
            self.items[self.top]=value
            return "success"
    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        else:
            start_element=self.items[self.start]
            start=self.start
            if start==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxsize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return start_element
    def peek(self):
        if self.isempty():
            return "queue is empty"
        else:
            return self.items[self.start]
    def delete(self):
        self.items=self.maxsize=[None]
        self.top=-1
        self.start=-1

