from collections import deque
import copy

n = int(input())
# number of classes

indegree =  [0]*(n+1)
# number of entries

curri = [[] for i in range(n+1)]

time = [0]*(n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))
    curri[i] = data

    time[i] = data[0]
    

print(curri)