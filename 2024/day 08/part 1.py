with open("input.txt", "r") as f:
    map = f.read().strip()
   
map = map.split()

n = len(map)

table = {}

def calculate(x_0, y_0, x_1, y_1):
    x_dif = x_0 - x_1
    y_dif = y_0 - y_1
   
    x_2 = x_0 + x_dif
    y_2 = y_0 + y_dif
   
    x_3 = x_1 - x_dif
    y_3 = y_1 - y_dif
   
    return (x_2, y_2, x_3, y_3)

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
           
            x_2, y_2, x_3, y_3 = calculate(x_0, y_0, x_1, y_1)
           
            if x_2 >= 0 and x_2 < n and y_2 >= 0 and y_2 < n:
                visited[x_2][y_2] = True
           
            if x_3 >= 0 and x_3 < n and y_3 >= 0 and y_3 < n:
                visited[x_3][y_3] = True
               
count = 0

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            count += 1
           
print(count)