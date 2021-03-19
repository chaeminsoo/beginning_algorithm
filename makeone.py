import time

x = int(input())
cnt = 0

d=[0]*30001
cnt = 0
def mkn(n):
    if n == 1:
        return cnt
    