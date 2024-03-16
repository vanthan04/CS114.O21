r, c = (map(int, input().split()))

matrix = [[0]*c for _ in range(r)]
for i in range(r):
    inp = input().split()
    for j in range(c):
        matrix[i][j] = int(inp[j])

matrix = matrix[::-1]

for i in range(r):
    joined_str = " ".join(str(num) for num in matrix[i])
    print(joined_str)

