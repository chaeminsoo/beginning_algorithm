import time

n,m = map(int,input().split())
cashs=[]
for i in range(n):
    cashs.append(int(input()))

st = time.time()


def changes(target,cashs):
    d=[10001]*target
    d[0]=0
    if d[target] != 10001:
        return d[target]
    
    reflist=[]
    for i in cashs:
        reflist.append(d[target-i])
    d[target]=min(reflist)+1