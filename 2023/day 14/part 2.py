import copy

def move_rock_up(rock_position, map, direction):
    number_of_row = len(map)
    number_of_col = len(map[0])

    x = rock_position[0]
    y = rock_position[1]
    
    if direction == "n":    
        while x != 0 and map[x-1][y] == ".":
            map[x-1][y], map[x][y] = map[x][y], map[x-1][y]
            x = x - 1
    if direction == "w":
        while y != 0 and map[x][y-1] == ".":
            map[x][y-1], map[x][y] = map[x][y], map[x][y-1]
            y = y - 1
    if direction == "s":
        while x != (number_of_row - 1) and map[x+1][y] == ".":
            map[x+1][y], map[x][y] = map[x][y], map[x+1][y]
            x = x + 1
    if direction == "e":
        while y != (number_of_col - 1) and map[x][y+1] == ".":
            map[x][y+1], map[x][y] = map[x][y], map[x][y+1]
            y = y + 1
    return map

def sum_arrangement(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        map = []
        for line in f:
            line = line.rstrip()
            row = []
            for char in line:
                row.append(char)
            map.append(row)
    
    number_of_row = len(map)
    number_of_col = len(map[0])

    map_memory = []
    for k in range(1000000000):
        for i in range(number_of_row):
            for j in range(number_of_col):
                if map[i][j] == "O":
                    map = move_rock_up((i,j), map, "n")
        for i in range(number_of_row):
            for j in range(number_of_col):
                if map[i][j] == "O":
                    map = move_rock_up((i,j), map, "w")
        for i in reversed(range(number_of_row)):
            for j in range(number_of_col):
                if map[i][j] == "O":
                    map = move_rock_up((i,j), map, "s")
        for i in range(number_of_row):
            for j in reversed(range(number_of_col)):
                if map[i][j] == "O":
                    map = move_rock_up((i,j), map, "e")
        
        if map in map_memory:
            last_pattern = map_memory.index(map)
            break
        map_memory.append(copy.deepcopy(map))
    
    cycle = len(map_memory) - last_pattern
    remainder = (1000000000 - last_pattern - 1) % cycle

    the_1000000000th_map = map_memory[last_pattern + remainder]
    
    total = 0

    for i in range(number_of_row):
        total += sum([char == "O" for char in the_1000000000th_map[i]]) * (number_of_row - i) 
    
    return total

if __name__ == "__main__":
    print(sum_arrangement("input.txt"))