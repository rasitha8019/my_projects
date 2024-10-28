INF=9999
def print_solution(nV,distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j]==INF:
                print("INF",end=" ")
            else:
                print(distance[i][j],end=" ")
        print(" ")
def floydWarshall(nV,G):
    distance=G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
    print_solution(nV,distance)

g=[[0,8,INF,1],
   [INF,0,1,INF],
    [4,INF,0,INF],
    [INF,2,9,1]]
floydWarshall(4,g)

