import time

n = int(input())
numbers=[]
for i in range(n):
    numbers.append(int(input()))
start=time.time()


numbers.sort()
numbers.reverse()

for i in numbers:
    print(i, end=' ')

end=time.time()
print('\ntime:',end-start)