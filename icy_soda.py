import time

n, m =map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int, input().split())))

start_time = time.time()

def dfs(x,y):
    if x <=-1 or x >=n or y<=-1 or y>=m:
        return False
    if board[x][y] ==0:
        board[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result =0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1

print(result)
end_time=time.time()
print('time:',end_time-start_time)