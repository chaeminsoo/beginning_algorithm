'''
Make a program that returns the least number of counts based on the given condition below. 

By using the number 'N', 'K', repeat the given process until 'N' becomes 1.
1.N -1
2.N/K (only when N%K=0)

input condition:
1st line: natural number N(2<=N<=100,000) and K(2<=K<=100,000) separated by ' '. (N>=K)
output condition:
number of count

'''

import time

N,K=map(int,input().split())
start_time = time.time()
cnt = 0
while True:
    if N % K == 0:
        N /= K
        cnt +=1
        if N==1: break
    else:
        N -= 1
        cnt +=1
        if N==1: break
print(cnt)
end_time= time.time()
print(end_time-start_time)