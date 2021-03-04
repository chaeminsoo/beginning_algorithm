'''

'''

import time

N = int(input())
command = list(input().split())

start_time = time.time()

x,y = 1,1
move =['U','D','R','L']
for i in command:
    if i == 'U':
        if x >1: x -= 1
    elif i == 'D':
        if x < N: x += 1
    elif i == 'R':
        if y < N: y += 1
    elif i == 'L':
        if y >1: y -= 1

print(x,y)
end_time = time.time()
print('time:',end_time - start_time)