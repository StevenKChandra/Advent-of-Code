with open("2024/day 10/input.txt", "r") as f:
    map = f.read().strip().split("\n")
    map = [[int(x) for x in row] for row in map]

def find_path(i, j, map):
    count = 0
    def dfs(i, j, n):
        nonlocal map
        nonlocal count
        
        if n == 9:
            count += 1
            return
        
        if i > 0 and map[i-1][j] == n + 1:
            dfs(i-1, j, n + 1)
        if i < len(map) - 1 and map[i+1][j] == n + 1:
            dfs(i+1, j, n + 1)
        if j > 0 and map[i][j-1] == n + 1:
            dfs(i, j-1, n + 1)
        if j < len(map[0]) - 1 and map[i][j+1] == n + 1:
            dfs(i, j+1, n + 1)
        
    dfs(i, j, 0)

    return count

count = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            count += find_path(i, j, map)

print(count)

