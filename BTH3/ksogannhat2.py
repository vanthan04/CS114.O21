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
while True:
    try:
        k,x = map(int, sys.stdin.readline().split())

        if x<arr[0]:
            print(arr[0], arr[k-1])
        elif x>arr[-1]:
            print(arr[-k], arr[-1])
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
                    if x-arr[i] > arr[j]-x:        
                        print(arr[i+1], arr[j])
                    else:
                        print(arr[i], arr[j-1])
                else:
                    print(arr[i], arr[j])

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
                        print(arr[i+1], arr[j])
                    else:
                        print(arr[i], arr[j-1])
                else:
                    print(arr[i], arr[j])
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
                        print(arr[i+1], arr[j])
                    else:
                        print(arr[i], arr[j-1])   
                
                else:
                    print(arr[i], arr[j])
    except:
        break