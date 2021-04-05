INF = int(1e9)

# n: number of nodes, m: number of edges

n,m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

#node itself
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] =0

for i in range(m):
    a,b,c = map(int,input().split())
    #form a to b cost c
    graph[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INF", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()