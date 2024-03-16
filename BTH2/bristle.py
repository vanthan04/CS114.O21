import sys
n=int(sys.stdin.readline())

arr=list(map(float, sys.stdin.readline().split()))
x=int(sys.stdin.readline())
y=int(sys.stdin.readline())
z=float(sys.stdin.readline())

bonus=[]
for i in range(len(arr)-1):
  bonus.append(arr[i]+z)

st=len(arr)*x
gai=0
flag=0

for i in range(1, len(arr)):
  count=0
  for j in range(flag, i):
    if arr[i] <= bonus[j]:
      count+=1
    else:
      flag=j
  gai+=count*y

print(st+gai)