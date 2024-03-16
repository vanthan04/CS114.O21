def count_stars(image):
    def is_star_pixel(pixel):
        return pixel == "-"

    rows = len(image)
    cols = len(image[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_valid_and_star_pixel(x, y):
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and is_star_pixel(image[x][y])

    def dfs(x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_and_star_pixel(nx, ny):
                dfs(nx, ny)

    count = 0

    for i in range(rows):
        for j in range(cols):
            if not is_star_pixel(image[i][j]):  
                continue
            if not visited[i][j]:
                dfs(i, j)
                count += 1
    return count

i=1
while True:
    try:
        m, n = map(int, input().split())
        image = []
        for _ in range(m):
            row = input().strip()
            image.append(row)

        print("Case "+ str(i)+": "+str(count_stars(image)))
        i+=1
    except:
        break