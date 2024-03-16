import sys

m, n = map(int, sys.stdin.readline().split())
matrix = []
for i in range(m):
  matrix.append(list(map(int, sys.stdin.readline().split())))

count=0
for i in range(m):
  for j in range(n):
    if matrix[i][j]==1:
        # Tăng ranh giới nếu
      # ô bên trái không được sơn
      if j==0 or matrix[i][j-1]==0:
        count+=1
      # ô bên phải không được sơn
      if j==n-1 or matrix[i][j+1]==0:
        count+=1
      # ô bên trên không được sơn:
      if i==0 or matrix[i-1][j]==0:
        count+=1
      # ô bên dưới không được sơn
      if i==m-1 or matrix[i+1][j]==0:
        count+=1

print(count)