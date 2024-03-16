matrix = [[0]*2 for _ in range(2)]


for i in range(2):
    row_input = input()
    for j in range(2):
        matrix[i][j] = row_input[j]

if matrix[0].count('#') + matrix[1].count('#') == 4 or matrix[0].count('#') + matrix[1].count('#') == 3:
    print("Yes")
else:
    if (matrix[0][0] == '#' and matrix[1][1] == '#') or (matrix[0][1] == '#' and matrix[1][0] == '#'):
        print("No") 
    else:
        print("Yes")