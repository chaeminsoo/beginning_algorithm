'''
Q: make the largest number using the given list of numbers by adding them 'M' times. You can't add specific index's number 'K' times in a row
   The size of the array is 'N' 

input condition:
    1st line: N(2<= N <= 1,000) , M(1<= M <= 10,000) , K(1<= K <= 10,000) ; separated by ' '
    2nd line: 'N' natural numbers ; separated by ' ' ; 1 <= natural numbers <= 10,000
    K <= M
output condition:
    1st line: result
'''
import time

n,m,k = map(int,input().split())
data = list(map(int, input().split()))

start_time = time.time()
data.sort()
first = data[n-1]
second = data[n-2]
#result = 0

result = (m//(k+1))*(first*k+second) + (m%(k+1))*first

'''
while True:
    for i in range(k):
        if m == 0: break
        result += first
        m -= 1
    if m == 0: break
    result += second
    m -= 1
'''
print(result)
end_time = time.time()
print('time: ',end_time-start_time)
    