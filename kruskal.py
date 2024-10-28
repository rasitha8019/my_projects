import disjoint as ds
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
        self.nodes=[]
        self.MST=[]
    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])
    def add_node(self,value):
        self.nodes.append(value)
    def print_sol(self,s,d,w):
        for s,d,w in self.MST:
            print("%s - %s : %s" % (s,d,w))
    def kruskal(self):
        i,e=0,0
        dst=ds.DisjointSet(self.nodes)
        self.graph=sorted(self.graph,key=lambda item:item[2])
        while e<self.V-1:
            s,d,w=self.graph[i]
            i+=1
            x=dst.find(s)
            y=dst.find(d)
            if x!=y:
                e+=1
                self.MST.append([s,d,w])
                dst.union(x,y)
        self.print_sol(s,d,w)
g=Graph(5)
g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")
g.add_edge("a","b",5)
g.add_edge("a","c",13)
g.add_edge("a","e",15)
g.add_edge("b","a",5)
g.add_edge("b","c",10)
g.add_edge("b","d",8)
g.add_edge("c","a",13)
g.add_edge("c","b",10)
g.add_edge("c","d",6)
g.add_edge("c","e",20)
g.add_edge("d","b",8)
g.add_edge("d","c",6)
g.add_edge("e","a",15)
g.add_edge("e","c",20)
g.kruskal()
