n,m = map(int,input().split())
# n: number of houses, m: number of roads

def find_parent(parent,  x):
    if parent[x] != x:
        parent[x]= find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

cost_list=[]

for _ in range(m):
    a,b,cost = map(int,input().split())
    cost_list.append(cost)
    graph[a][b] = cost
    graph[b][a] = cost
