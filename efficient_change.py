import time

n,m = map(int,input().split())
cashs=[]
for i in range(n):
    cashs.append(int(input()))

st = time.time()

d=[10001]*(m+1)
d[0]=0
for i in range(n):
    for j in range(cashs[i], m+1):
        if d[j-cashs[i]] != 10001:
            d[j] = min(d[j], d[j-cashs[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
et=time.time()
print('time:',et-st)