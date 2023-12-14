def move_rock_up(rock_position, map):
    x = rock_position[0]
    y = rock_position[1]
    while x != 0 and map[x-1][y] == ".":
        map[x-1][y], map[x][y] = map[x][y], map[x-1][y]
        x = x - 1
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
    for i in range(number_of_row):
        for j in range(number_of_col):
            if map[i][j] == "O":
                map = move_rock_up((i,j), map)
    
    total = 0
    for i in range(number_of_row):
        total += sum([char == "O" for char in map[i]]) * (number_of_row - i) 
    
    return total

if __name__ == "__main__":
    print(sum_arrangement("input.txt"))