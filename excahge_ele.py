import time

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

st=time.time()

a.sort()
b.sort()

for i in range(k):
    if a[i] < b[len(b)-1-i]:
        a[i] = b[len(b)-1-i]

print(sum(a))
et=time.time()
print('time:',et-st)