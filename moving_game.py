'''
incompleted
'''

import time

N,M = map(int,input().split())
A,B,d = map(int,input().split())
landseaR=[]
for i in range(N):
    landseaC = list(map(int,input().split()))
    landseaR.append(landseaC)
start_time=time.time()

def turn(a):
    if a>0:
        a -= 1
    elif a == 0:
        a = 3
    return a
cnt=1
aaa=0
while aaa<3:
    landseaR[A][B]=3
    
    if landseaR[A][B-1]!=0 and landseaR[A-1][B]!=0 and landseaR[A+1][B]!=0 and landseaR[A][B+1]!=0:
        if d==0: A+=1
        elif d==1:B-=1
        elif d==2:A-=1
        elif d==3:B+=1
        
        if landseaR[A][B]==1:
            break
    else:
        if d==0:
            if landseaR[A][B-1] ==0:
                B-=1
                cnt+=1
            elif landseaR[A][B-1]!=0:
                pass
        elif d==1:
            if landseaR[A-1][B] ==0:
                A-=1
                cnt+=1
            elif landseaR[A-1][B]!=0:
                pass
        elif d==2:
            if landseaR[A][B+1] ==0:
                B+=1
                cnt+=1
            elif landseaR[A][B+1]!=0:
                pass
        elif d==3:
            if landseaR[A+1][B]==0:
                A+=1
                cnt+=1
            elif landseaR[A+1][B]!=0:
                pass
    turn(d)
    aaa+=1
    continue
    

print(cnt)
end_time=time.time()
print('time:',end_time-start_time)