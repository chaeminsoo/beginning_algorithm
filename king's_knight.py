'''
There is a Knight on the 8*8 size chessboard. Make a program that gives us the number of cases of the Knight's available moves.
(The chessboard's rows are numbered 1 to 8 from the top and columns are characterized a to h from the left.)

input condition:
	starting position '(column)(row)'
output condition:
	the number of cases
'''

import time

loca = input() #a1
start_time = time.time()
columns={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
result =0

if 3<= columns[loca[0]] <=6:
    if 3<= int(loca[1]) <=6:
        result += 8
    elif int(loca[1]) ==2 or int(loca[1]) ==7:
        result += 6
    elif int(loca[1]) ==1 or int(loca[1]) ==8:
        result += 4
elif columns[loca[0]] == 2 or columns[loca[0]] ==7:
    if 3<= int(loca[1]) <=6:
        result+=6
    elif int(loca[1]) ==2 or int(loca[1]) ==7:
        result+=4
    elif int(loca[1]) ==1 or int(loca[1]) ==8:
        result+=3
elif columns[loca[0]] == 1 or columns[loca[0]] ==8:
    if 3<= int(loca[1]) <=6:
        result+=4
    elif int(loca[1]) ==2 or int(loca[1]) ==7:
        result+=4
    elif int(loca[1]) ==1 or int(loca[1]) ==8:
        result+=2
print(result)
end_time= time.time()
print('time:',end_time - start_time)