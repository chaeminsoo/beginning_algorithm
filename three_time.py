'''
Make a program that counts every number of cases of the time contain the number "3", from 00:00:00 to N:59:59.

input condition:
	N (0<=N<=23)
output condition:
	number of cases
'''

import time

N = int(input())
start_time = time.time()
cnt =0
for h in range(N+1):
    if '3' in str(h):
        cnt += 3600
        continue
    for m in range(60):
        if '3' in str(m):
            cnt += 60
            continue
        for s in range(60):
            if '3' in str(s): cnt +=1
    
print(cnt)
end_time = time.time()
print('time:',end_time - start_time)