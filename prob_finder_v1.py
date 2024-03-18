import numpy as np
import math

n = int(input("max no. of steps: "))
max_no = pow((2*n + 1), 2)
rows = 2*n + 1

#construct spiral up to (2n+1) ^ 2
spiral = [[0 for i in range(rows)] for j in range(rows)]
spiral[n][n] = 1
spiral[n+1][n] = 2
i = n+1
j = n
i_prev = n
j_prev = n


def next(a,b):
    global i, j, i_prev, j_prev
    i_prev = i
    j_prev = j
    i = a
    j = b

for m in range(2, max_no):
    if j > j_prev:
        if spiral[i-1][j] == 0:
            spiral[i-1][j] = m+1
            next(i-1, j)
        else:
            spiral[i][j+1] = m+1
            next(i, j+1)
            
    elif j < j_prev:
        if spiral[i+1][j] == 0:
            spiral[i+1][j] = m+1
            next(i+1, j)
        else:
            spiral[i][j-1] = m+1
            next(i, j-1)
        
    elif i > i_prev:
        if spiral[i][j+1] == 0:
            spiral[i][j+1] = m+1
            next(i, j+1)
        else:
            spiral[i+1][j] = m+1
            next(i+1, j)

    else:
        if spiral[i][j-1] == 0:
            spiral[i][j-1] = m+1
            next(i, j-1)
        else:
            spiral[i-1][j] = m+1
            next(i-1, j)



#print spiral
'''
for i in range(2*n+1):
    for j in range(2*n+1):
        out = str(spiral[j][i])
        print(out, end = " " * (5-len(out)))
    print("")

'''

 

#test all moves along the spiral
moves = [1] * n
tens = 0

for i in range(pow(4, n)):
    for j in range(n):
        if moves[j] < 4:
            moves[j] = moves[j] + 1
            for k in range(j):
                moves[k] = 1
            break 
    a,b = (n, n)
    for elem in moves:
        if elem == 1:
            a += 1
        elif elem == 2:
            a = a - 1
        elif elem == 3:
            b += 1
        else:
            b = b-1
    if spiral[a][b] % 10 == 0:
        tens += 1


#prints probability
        
prob = tens / pow(4, n)
print(prob)
