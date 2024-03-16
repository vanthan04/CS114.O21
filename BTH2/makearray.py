import sys

n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
  x = int(sys.stdin.readline())
  arr.append(x)

l = min(arr)
r = max(arr)

print((r-l-1)-(len(arr)-2))