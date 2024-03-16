N = int(input())

for _ in range(N):
    a = input()
    b = input()
    if len(a) != len(b):
        print("NO")
        continue
    
    #Lấy các kí tự lẻ trong chuỗi a sau đó sort
    a_odd = list(a[::2]) 
    a_odd.sort()
    # Lấy các kí tự chẵn trong chuỗi a sau đó sort
    a_even = list(a[1::2])
    a_even.sort()   
    #Lấy các kí tự lẻ trong chuỗi b sau đó sort
    b_odd = list(b[::2]) 
    b_odd.sort()
    # Lấy các kí tự chẵn trong chuỗi b sau đó sort
    b_even = list(b[1::2])
    b_even.sort()

    if a_odd==b_odd and a_even==b_even:
        print("YES")
    else:
        print("NO")