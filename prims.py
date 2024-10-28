import sys
class Graph:
    def __init__(self,verticesnum,edges,nodes):
        self.nodes=nodes
        self.edges=edges
        self.verticesnum=verticesnum
        self.MST=[]
    def print_sol(self):
        print("EDGE : WEIGHT")
        for s,d,w in self.MST:
            print("%s -> %s : %s"%(s,d,w))
    def prims(self):
        visited=[0]*self.verticesnum
        edgenum=0
        visited[0]=True
        while edgenum<self.verticesnum-1:
            min=sys.maxsize
            for i in range(self.verticesnum):
                if visited[i]:
                    for j in range(self.verticesnum):
                        if((not visited[j]) and self.edges[i][j]):
                            if min>self.edges[i][j]:
                                pass

