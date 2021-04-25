import time

INF =int(1e9)

n,m,c = map(int,input().split())
# n: number of cities, m: number of path, c: starting city

graph= [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    x,y,z = map(int,input().split())   
    # form x to y cost z
    graph[x][y] = z


cnt=0
cost=1
for a in graph[c]:
    if a != 0 and a != INF:
        cnt +=1
        cost = max(cost,a)

print(cnt, cost)