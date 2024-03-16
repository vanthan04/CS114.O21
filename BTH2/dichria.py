from re import template
import sys
r, c = map(int, sys.stdin.readline().split())

matrix=[]
for i in range(r):
  row_input = list(map(int, sys.stdin.readline().split()))
  matrix.append(row_input)

arr=matrix

def daonguoc(arr):
  x=arr[0]
  del arr[0]
  arr.append(x)
  return  arr

def daoxuoi(arr):
  arr.insert(0,arr[-1])
  arr.pop()
  return arr

if r==1:
  x=matrix[0][c-1]
  matrix[0].pop()
  matrix[0].insert(0,x)
  joined_str = " ".join(str(num) for num in matrix[0])
  print(joined_str)
elif c==1:
  x=matrix[r-1]
  matrix.pop()
  matrix.insert(0, x)
  for i in range(r):
    print(matrix[i][0])
else:
  left=top=0
  right=c-1
  bottom=r-1
  ria=0
  m=min(r,c)
  if m%2==0:
    n=m//2
  else:
    n=m//2+1

  for _ in range(n):
    temp=[]
    if bottom==top:
      for i in range(left, right+1):
        temp.append(matrix[bottom][i])
    elif left==right:
      for i in range(top, bottom+1):
        temp.append(matrix[i][left])
    else:
      for i in range(left,right+1):
        temp.append(matrix[top][i])
      for i in range(top+1, bottom+1):
        temp.append(matrix[i][right])
    
      for i in range(right-1,left, -1):
        temp.append(matrix[bottom][i])

      for i in range(bottom, top, -1):
        temp.append(matrix[i][left])

    if ria%2==0:
      
      if bottom==top:

        temp=daoxuoi(temp)
        for i in range(right, left-1, -1):
          arr[bottom][i]=temp.pop()

      elif left==right:
        temp=daoxuoi(temp)
        for i in range(bottom, top-1, -1):
          arr[i][left]=temp.pop()

      else:
        for i in range(top, bottom+1):
          arr[i][left]=temp.pop()

        for i in range(left+1, right+1):
          arr[bottom][i]=temp.pop()
        
        for i in range(bottom-1,top-1, -1):
          arr[i][right]=temp.pop()

        for i in range(right-1, left, -1):
          arr[top][i]=temp.pop()
      
    else:
      temp=daonguoc(temp)
      if bottom==top:
        for i in range(right, left-1, -1):
          arr[bottom][i]=temp.pop()

      elif left==right:
        for i in range(bottom, top-1, -1):
          arr[i][left]=temp.pop()

      else:

        for i in range(top+1,bottom+1):
          arr[i][left] = temp.pop()

        for i in range(left+1, right+1):
          arr[bottom][i]=temp.pop()

        for i in range(bottom-1,top-1, -1):
          arr[i][right]=temp.pop()
          
        for i in range(right-1, left-1, -1):
          arr[top][i]=temp.pop()
          
    left+=1
    right-=1
    top+=1
    bottom-=1
    ria+=1

  for i in range(r):
    joined_str = " ".join(str(num) for num in arr[i])
    print(joined_str)

