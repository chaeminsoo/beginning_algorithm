from collections import deque

num_node, num_edge = map(int,input().split())

in_degree = [0]*(num_node+1)

graph = [[] for i in range(num_node+1)]

for _ in range(num_edge):
    a,b = map(int,input().split())
    graph[a].append(b)
    in_degree[b] +=1

def topo_sort():
    result =[]
    q = deque()

    for i in range(1, num_node+1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            in_degree[i] -=1

            if in_degree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topo_sort()