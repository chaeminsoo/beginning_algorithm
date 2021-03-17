import time

n,m =map(int,input().split())
tuk = list(map(int,input().split()))

st=time.time()

tuk.sort(reverse=True)
tuktall=tuk[0]
for i in range(tuktall, 0, -1):

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

