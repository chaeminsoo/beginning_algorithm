n,m = map(int,input().split())
# n: number of houses, m: number of roads

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

cost_list=[]

for _ in range(m):
    a,b,cost = map(int,input().split())
    cost_list.append(cost)
    graph[a][b] = cost
    graph[b][a] = cost
