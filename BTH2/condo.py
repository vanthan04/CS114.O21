import sys
l, m = map(int, sys.stdin.readline().split())
l = l*100
arrleft=[]
arrright=[]
for i in range(m):
  d, location = sys.stdin.readline().split()
  if location=="right":
    arrright.append(int(d))
  else:
    arrleft.append(int(d))


def solve(t, arr):
  n=len(arr)-1
  i=0
  sum=0
  count=0
  if len(arr)==1:
    return 1
  elif len(arr)==0:
    return 0
  while i<=n:
    sum += arr[i]
    if sum>t:
      count+=1
      sum=0
      continue
    if i+1==n:
      if sum+arr[i+1]>t:
        count+=2
      else:
        count+=1
      break
    i+=1

  return count

count = 0
left = solve(l, arrleft)
right = solve(l, arrright)
if left==0:
  count = 2*right
if right==0:
  count=2*left-1
if left==right:
  count=2*left
if left<right:
  count=2*right
if right<left:
  count = 2*left-1

print(count)