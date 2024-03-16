import sys
map(int, sys.stdin.readline().split())
online=list(map(int, sys.stdin.readline().split()))
arr=list(map(int, sys.stdin.readline().split()))

arr.sort()
count=0
i=0
j=0
while i < len(arr) and j < len(online):
    if arr[i] < online[j]:
      i += 1
    elif arr[i] > online[j]:
      j += 1
    else:
      count += 1
      i += 1
      j += 1
    
print(count)
      