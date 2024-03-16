matrix = [[0]*3 for _ in range(3)]


for i in range(3):
    row_input = input().split()
    for j in range(3):
        matrix[i][j] = int(row_input[j])


N = int(input())
arr = [int(input()) for _ in range(N)]

def check():
    # Kiá»m tra cÃ¡c hÃ ng
    for i in range(3):
        temp = 0
        for j in range(3):
            if matrix[i][j] in arr:
                temp += 1
        if temp == 3:
            return True

    # Kiá»m tra cÃ¡c cá»t
    for j in range(3):
        temp = 0
        for i in range(3):
            if matrix[i][j] in arr:
                temp += 1
        if temp == 3:
            return True

    # Kiá»m tra ÄÆ°á»ng chÃ©o chÃ­nh
    temp = 0
    for i in range(3):
        if matrix[i][i] in arr:
            temp += 1
    if temp == 3:
        return True

    # Kiá»m tra ÄÆ°á»ng chÃ©o phá»¥
    temp = 0
    for i in range(3):
        if matrix[i][2 - i] in arr:
            temp += 1
    if temp == 3:
        return True

    return False

if check():
    print("Yes")
else:
    print("No")