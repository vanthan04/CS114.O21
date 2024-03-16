import sys
import re
matrix=[]
rows, cols = map(int, sys.stdin.readline().split())
for _ in range(rows):
    matrix.append(list(map(int,sys.stdin.readline().split())))

max_length=[]
for i in range(cols):
    length_max=len(str(matrix[0][i]))
    for j in range(1, rows):
        if len(str(matrix[j][i])) > length_max:
            length_max = len(str(matrix[j][i]))
    max_length.append(length_max)

for i in range(rows):
    for j in range(cols):
        space=max_length[j]-len(str(matrix[i][j]))
        if j==0:
            print(" "* space + str(matrix[i][j]), end="")
        else:
            print(" "* (space+1) + str(matrix[i][j]), end="")
            if j==cols-1:
                print()
