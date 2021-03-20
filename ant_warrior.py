import time

n = int(input())
Ks = list(map(int,input().split()))

st=time.time()

d=[0]*101
d[1]=Ks[0]
d[2]=max(d[1],Ks[1])
for i in range(3,n+1):
    d[i] = max(d[i-1],d[i-2]+Ks[i-1])

print(d[n])
et=time.time()
print('time:',et-st)