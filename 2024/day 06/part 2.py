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

count = 0

for i in range(n):
    row_copy = [neighboors_table[i][j].copy() for j in range(n)]
    for j in range(n):
        if map[i][j] in ["#", "^"]:
            continue

        col_copy = [neighboors_table[_][j].copy() for _ in range(n)]

        next = neighboors_table[i][j][0]
        if next == None:
            next = n
        for k in range(j+1, next):
            neighboors_table[i][k][2] = j
        
        next = neighboors_table[i][j][1]
        if next == None:
            next = n
        for k in range(i+1, next):
            neighboors_table[k][j][3] = i

        next = neighboors_table[i][j][2]
        if next == None:
            next = 0
        for k in range(next, j):
            neighboors_table[i][k][0] = j

        next = neighboors_table[i][j][3]
        if next == None:
            next = 0
        for k in range(next, i):
            neighboors_table[k][j][1] = i

        direction = 3
        pos = start_pos
        
        visited = set()

        while True:
            if (pos[0], pos[1], direction) in visited:
                print(i, j)
                count += 1
                break

            visited.add((pos[0], pos[1], direction))

            if direction == 0:
                next = neighboors_table[pos[0]][pos[1]][0]
                if next == None:
                    next_pos = (pos[0], n)
                else:
                    next_pos = (pos[0], next-1)

            elif direction == 1:
                next = neighboors_table[pos[0]][pos[1]][1]
                if next == None:
                    next_pos = (n, pos[1])
                else:
                    next_pos = (next-1, pos[1])

            elif direction == 2:
                next = neighboors_table[pos[0]][pos[1]][2]
                if next == None:
                    next_pos = (pos[0], 0)
                else:
                    next_pos = (pos[0], next+1)

            elif direction == 3:
                next = neighboors_table[pos[0]][pos[1]][3]
                if next == None:
                    next_pos = (0, pos[1])
                else:
                    next_pos = (next+1, pos[1])
                
            if next == None:
                break

            direction = (direction+1) % 4

            pos = next_pos

        for k in range(n):
            neighboors_table[i][k] = row_copy[k].copy()
            neighboors_table[k][j] = col_copy[k].copy()   

print(count)