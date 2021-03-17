import time

n=int(input())
ihave=list(map(int,input().split()))
m=int(input())
request=list(map(int,input().split()))

st=time.time()

ihave.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) //2
    if array[mid] == target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target,mid+1,end)

for i in request:
    result = binary_search(ihave, i,0,n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=" ")

et=time.time()
print('\ntime:',et-st)