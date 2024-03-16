def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right

import sys
sys.stdin.readline()
arr=list(map(int, sys.stdin.readline().split()))
k,x = map(int, sys.stdin.readline().split())

if x<arr[0]:
  for i in range(k):
    print(arr[i], end=" ")
elif x>arr[-1]:
  for i in range(k):
    print(arr[len(arr)-k+i], end=" ")
else: 
    result=binary_search(arr, x)
    i=result-k//2
    j=result+k//2

    if i<0:
        j+=abs(i)
        i=0
    if j>=len(arr):
        i-=abs(j-len(arr)-1)
        j=len(arr)-1
    
    if x-arr[i]==arr[j]-x:
        if k%2==0:
          for z in range(i,j):
            print(arr[z], end=" ")
        else:
          for z in range(i, j+1):
             print(arr[z], end=" ")

    elif x-arr[i]<arr[j]-x:
        i-=1
        j-=1
        while i>=0 and x-arr[i]<arr[j]-x:
            i-=1
            j-=1

        if i<0:
           j+=abs(i)
           i=0
           
        if k%2==0:
            if x-arr[i] > arr[j]-x:        
                for z in range(i+1,j+1):
                    print(arr[z], end=" ")
            else:
                for z in range(i,j):
                    print(arr[z], end=" ")
        else:
          for z in range(i, j+1):
             print(arr[z], end=" ")
    else:
        i+=1
        j+=1 
        while j<len(arr) and x-arr[i]>arr[j]-x:
            i+=1
            j+=1
        
        if j>=len(arr):
            i-=abs(j-len(arr)-1)
            j=len(arr)-1
        
        if k%2==0:
            if x-arr[i] > arr[j]-x:        
                for z in range(i+1,j+1):
                    print(arr[z], end=" ")
            else:
                for z in range(i,j):
                    print(arr[z], end=" ")   
          
        else:
            for z in range(i, j+1):
                print(arr[z], end=" ")