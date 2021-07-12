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

n,m = map(int,input().split())
# n: number of houses, m: number of roads
parent = [0]*(n+1) # parent table

roads = []
costs =[]
result =0

for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    a, b, c = map(int,input().split())
    roads.append((c,a,b))

roads.sort()

for road in roads:
    cost, a, b =road
    # no cyccle
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        costs.append(cost)

costs.pop()

for i in costs:
    result += i

print(result)