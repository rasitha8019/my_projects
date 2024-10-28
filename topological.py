from collections import defaultdict
class Graph:
    def __init__(self,numberofvertices):
        self.graph=defaultdict(list)
        self.numberofvertices=numberofvertices
    def addedge(self,vertex,edge):
        self.graph[vertex].append(edge)
    def topologicalutil(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalutil(i,visited,stack)
        stack.insert(0,v)
    def topologicalsort(self):
        visited=[]
        stack=[]
        for k in list(self.graph):
            if k not in visited:
                self.topologicalutil(k,visited,stack)
        print(stack)

my_graph=Graph(8)
my_graph.addedge("A","C")
my_graph.addedge("C","E")
my_graph.addedge("B","C")
my_graph.addedge("B","D")
my_graph.addedge("D","F")
my_graph.addedge("E","H")
my_graph.addedge("E","F")
my_graph.addedge("F","G")
my_graph.topologicalsort()