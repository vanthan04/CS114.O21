n = int(input())

arr = []

for i in range(n):
    x = int(input())
    arr.append(x)


def check(arr):
    count = 0
    i=0
    j=len(arr)-1
    while i < j:
        if count > 1:
            return False
        else:
            if arr[i] != arr[j]:
                count+=1
        i+=1
        j-=1
    return True
if check(arr):
    print("TRUE")
else:
    print("FALSE")