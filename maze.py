'''
incompleted
'''
from collections import deque
import time

n,m=map(int,input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int,input())))

start_time=time.time()

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] ==1:
                maze[nx][ny] == maze[x][y] +1
                queue.append((nx,ny))
    return maze[n-1][m-1]

print(bfs(1,1))
end_time=time.time()
print('time:',end_time-start_time)