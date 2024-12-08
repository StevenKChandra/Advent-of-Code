with open("input.txt", "r") as f:
    map = f.read().strip()
   
map = map.split()

n = len(map)

table = {}

def calculate(x_0, y_0, x_1, y_1):
    x_dif = x_0 - x_1
    y_dif = y_0 - y_1
   
    antinodes = []
   
    while x_0 >= 0 and x_0 < n and y_0 >= 0 and y_0 < n:
        antinodes.append((x_0, y_0))
        x_0 = x_0 + x_dif
        y_0 = y_0 + y_dif
   
    while x_1 >= 0 and x_1 < n and y_1 >= 0 and y_1 < n:
        antinodes.append((x_1, y_1))
        x_1 = x_1 - x_dif
        y_1 = y_1 - y_dif
   
    return antinodes

for i in range(n):
    for j in range(n):
        if map[i][j] == ".":
            continue
        code = map[i][j]
        if code not in table:
            table[code] = []
        table[code].append((i, j))

visited = [[False]*n for _ in range(n)]

for position in table.values():
    for i in range(len(position)):
        x_0, y_0 = position[i]
        for j in range(i+1, len(position)):
            x_1, y_1 = position[j]
           
            antinodes = calculate(x_0, y_0, x_1, y_1)
           
            for (x, y) in antinodes:
                visited[x][y] = True
count = 0

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            count += 1
           
print(count)