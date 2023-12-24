def count_garden_plot(filepath):
    """ """

    with open(filepath, "r") as f: # open the file

        map = []
        for i, line in enumerate(f):
            line = line.rstrip()

            row = []
            for j, char in enumerate(line):
                if char == "S":
                    starting_position = (i, j)
                    row.append(".")
                else:
                    row.append(char)
            map.append(row)
    
    size = len(map)
    edge = size // 2

    for i in range(len(map)):
        map[i] *= 5
    map *= 5
    starting_position = (starting_position[0]+size*2, starting_position[1]+size*2)

    data = []
    possible_positions = [starting_position]
    for i in range(edge + size * 2):
        new_positions = []
        while possible_positions:
            point = possible_positions.pop(0)
            next_points = next_step(point, map)
            for point in next_points:
                if not point in new_positions:
                    new_positions.append(point)
        possible_positions = new_positions
        if i+1 in [edge, edge + size, edge + size * 2]:
            data.append(len(possible_positions))

    a = (data[2] - (2 * data[1]) + data[0]) // 2 
    b = data[1] - data[0] - a
    c = data[0]

    f = lambda n: a * n**2 + b * n + c
    return f(26501365 - edge)

def next_step(point, map):
    i_max = len(map) - 1
    j_max = len(map[0]) - 1
    i, j = point
    next_points = []
    if i !=0 and map[i-1][j] == ".":
        next_points.append((i-1,j))
    if j !=0 and map[i][j-1] == ".":
        next_points.append((i,j-1))
    if i !=i_max and map[i+1][j] == ".":
        next_points.append((i+1,j))
    if j !=j_max and map[i][j+1] == ".":
        next_points.append((i,j+1))
    return next_points


if __name__ == "__main__":  
    print(count_garden_plot("input.txt"))