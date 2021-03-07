'''
incompleted

A character is on an N*M-sized map. Each location on the map can be described as (A, B), A means how far from the North and B means how far from the West. On the map, there are land and sea.  The character can move through the land only. The character will move automatically by the rules down below.

Starting at the current location and direction, the character will choose his way from his left.
If there is a land that he has never been, he will turn left and move to the land. If there isn't, he will make his turn but stand still and go back to the first step.


input condition:
	starting position '(column)(row)'
output condition:
	the number of cases
'''

import time

N,M = map(int,input().split())
A,B,d = map(int,input().split())
landseaR=[]
for i in range(N):
    landseaC = list(map(int,input().split()))
    landseaR.append(landseaC)
start_time=time.time()

def turn_left(a):
    if a>0:
        a -= 1
    elif a == 0:
        a = 3
    return a

cnt=1
turns=0
da=[-1,0,1,0]
db=[0,1,0,-1]

while True:
    landseaR[A][B]=3
    turn_left(d)

    go_a= A+da[d]
    go_b= B+db[d]
    
    if landseaR[go_a][go_b] ==0:
        landseaR[go_a][go_b] = 3

        A=go_a
        B=go_b
        cnt+=1
        turns=0
        continue
    else:
        turns+=1

    if turns ==4:
        go_a = A-da[d]
        go_b = B-db[d]

        if landseaR[go_a][go_b] ==0:
            A = go_a
            B = go_b
            turns = 0
        else:
            break

    '''
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

    if landseaR[A][B-1]!=0 and landseaR[A-1][B]!=0 and landseaR[A+1][B]!=0 and landseaR[A][B+1]!=0:
        if d==0: A+=1
        elif d==1:B-=1
        elif d==2:A-=1
        elif d==3:B+=1
        
        if landseaR[A][B]==1:
            break'''
        

print(cnt)
end_time=time.time()
print('time:',end_time-start_time)