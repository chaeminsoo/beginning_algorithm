'''
Tourist 'A' is standing at point (1,1) of n*n size spare. The far upper left point is (1,1) and the far lower right is (n,n) There is a tour plan written with U, D, R, L. Each code means move up, down, right, left for one.

Make a program that gives us a final destination of tourist 'A'. If 'A' moves out of the spare, that part of the plan will be ignored.

input condition:
	1st line: n (1<=n<=100)
	2nd line: tour plan (1<= length <=100)
output condition:
	final destinaton (m,n)
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