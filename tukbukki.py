import time
import random
'''
tuk=[]
for i in range(1000000):
    tuk.append(random.randint(1,2000000000))
m=random.randint(1,200)
print(m)
'''
n,m =map(int,input().split())
tuk = list(map(int,input().split()))

st=time.time()

def binary_search(array, target, start, end):
    total = 0
    if start > end:
        return None
    mid = (start+end)//2
    #result = total - (mid*len(array))
    for i in array:
        if i>mid:
            total += i-mid
        else:
            pass

    if total == target:
        return mid
    elif total > target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)
    
print(binary_search(tuk,m,0,max(tuk)))
et=time.time()
print('time:',et-st)