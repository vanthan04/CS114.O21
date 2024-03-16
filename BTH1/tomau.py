import math

inp = input().split()
H = int(inp[0])
W = int(inp[1])
K = int(inp[2])

matrix = []
for i in range(H):
    input_r = input()
    matrix.append(input_r)

for i in range(len(matrix)):
    matrix[i] = list(matrix[i])


def dem(matrix):
    count=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                count += 1
    return count

def thaythe(matrix, row, col):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row or j in col:
                matrix[i][j] = '*'
    return matrix

#Chatgpt để tìm tất cả các tổ hợp từ 1 đến n
#https://chat.openai.com/c/33c32e4d-0d2a-431c-88fc-409def54085c

def combinations(n):
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Thêm một bản sao của path vào kết quả
        for i in range(start, n):
            path.append(i)  # Thêm phần tử tiếp theo vào path
            backtrack(i + 1, path)  # Gọi đệ quy với vị trí tiếp theo
            path.pop()  # Xóa phần tử cuối cùng để thử một phần tử khác

    backtrack(0, [])
    return result

#Các tổ hợp được tạo thành từ các hàng của ma trận
rows = combinations(H)
cols = combinations(W)

count=0
temp = []
for i in range(len(rows)):
    for j in range(len(cols)):
        temp = [row[:] for row in matrix]
        temp = thaythe(temp, rows[i], cols[j])
        if dem(temp) == K:
            count += 1


print(count)