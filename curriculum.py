from collections import deque
import copy

n = int(input())
# number of classes

prereq =  [0]*(n+1)
# number of entries

curri = [[] for i in range(n+1)]

time = [0]*(n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))
    curri[i] = data
    prereq[i] = data[1:]
    time[i] = data[0]

ref_result1 = copy.deepcopy(time)
#ref_result2 = copy.deepcopy(time)
ref_num=0
cnt=0
for i in prereq[1:]:
    qpre =deque(i)
    cnt +=1
    while qpre:
        ref = qpre.popleft()    

        if ref == -1:
            continue
        else:
            ref_num += time[ref]
            #ref_result1[cnt] += time[ref]
            #ref_result2[cnt] += ref_result2[ref]
    ref_result1[cnt] += ref_num
    ref_num = 0

print(ref_result1)
#print(ref_result2)
print(prereq)
print(time)
print(qpre)