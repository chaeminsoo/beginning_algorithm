'''
There are N*M forms of cards. (N: row, M: column)
You want to pick the largest number by following the rules below.
1: Choose the row you want to pick a card
2: The card that has the lowest number will pick automatically

input condition:
	1st line: natural number N, M(separated by ' '),(1<=N,M<=100)
	2nd line: list of numbers based on given size(N*M)
output condition:
	1st line: result
'''
n,m = map(int,input().split())
result =0
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data) 
    result = max(result, min_value)

print(result)