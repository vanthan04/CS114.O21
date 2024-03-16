def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))


for target in targets:
    position = binary_search(arr, target)
    temp=position
    while arr[position] == arr[temp]:
        temp-=1
    
    print(temp+1 if position != -1 else -1)