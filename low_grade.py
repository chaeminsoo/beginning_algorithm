import time

n = int(input())
gradelist=[]
for i in range(n):
    name, grade = input().split()
    gradelist.append((name,int(grade)))
st=time.time()
def setting(data):
    return data[1]

reuslt = sorted(gradelist, key=setting)

for i in reuslt:
    print(i[0], end=' ')
et=time.time()
print('\ntime:', et-st)