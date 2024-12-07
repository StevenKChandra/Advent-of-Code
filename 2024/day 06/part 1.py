with open("2024/day 06/input.txt") as f:
    map = f.read().strip()

map = map.split("\n")

n = len(map)

neighboors_table = [[[None, None, None, None] for i in range(n)] for j in range(n)]

for i in range(n):
    prev = [None, None, None, None]
    for j in range(n):
        if map[i][j] == "^":
            start_pos = (i, j)
        
        if map[i][j] == "#":
            prev[2] = j
        else:
            neighboors_table[i][j][2] = prev[2]

        if map[j][i] == "#":
            prev[3] = j
        else:
            neighboors_table[j][i][3] = prev[3]

        if map[i][n-j-1] == "#":
            prev[0] = n-j-1
        else:
            neighboors_table[i][n-j-1][0] = prev[0]

        if map[n-j-1][i] == "#":
            prev[1] = n-j-1
        else:
            neighboors_table[n-j-1][i][1] = prev[1]

visited_table = [[False for i in range(n)] for j in range(n)]


direction = 3

pos = start_pos

while True:
    if direction == 0:
        next = neighboors_table[pos[0]][pos[1]][0]
        if next == None:
            next_pos = (pos[0], n)
        else:
            next_pos = (pos[0], next-1)

        for i in range(pos[1], next_pos[1]):
            visited_table[pos[0]][i] = True

    elif direction == 1:
        next = neighboors_table[pos[0]][pos[1]][1]
        if next == None:
            next_pos = (n, pos[1])
        else:
            next_pos = (next-1, pos[1])

        for i in range(pos[0], next_pos[0]):
            visited_table[i][pos[1]] = True

    elif direction == 2:
        next = neighboors_table[pos[0]][pos[1]][2]
        if next == None:
            next_pos = (pos[0], 0)
        else:
            next_pos = (pos[0], next+1)

        for i in range(next_pos[1]+1, pos[1]+1):
            visited_table[pos[0]][i] = True

    elif direction == 3:
        next = neighboors_table[pos[0]][pos[1]][3]
        if next == None:
            next_pos = (0, pos[1])
        else:
            next_pos = (next+1, pos[1])

        for i in range(next_pos[0]+1, pos[0]+1):
            visited_table[i][pos[1]] = True
    
    if next == None:
        break

    direction = (direction+1) % 4

    pos = next_pos

count = 0
for i in range(n):
    for j in range(n):
        if visited_table[i][j]:
            count += 1
            
print(count)