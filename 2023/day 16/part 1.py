def simulate_beam(direction, start_point, map, simulated_beam, energized_tiles):
    i = start_point[0]
    j = start_point[1]
    num_row = len(map)
    num_col = len(map[0])
    while True:
        energized_tiles[i][j] = "#"
        if map[i][j] in (".", "#"):
            if direction == "u" and i != 0:
                i -= 1
            elif direction == "d" and i != num_row - 1:
                i += 1
            elif direction == "l" and j != 0:
                j -= 1
            elif direction == "r" and j != num_col - 1:
                j += 1
            else:
                break
        elif map[i][j] == "\\":
            if direction == "u" and j != 0:
                j -= 1
                direction = "l"
            elif direction == "l" and i != 0:
                i -= 1
                direction = "u"
            elif direction == "d" and j != num_col - 1:
                j += 1
                direction = "r"
            elif direction == "r" and i != num_row - 1:
                i += 1
                direction = "d"
            else:
                break
        elif map[i][j] == "/":
            if direction == "d" and j != 0:
                j -= 1
                direction = "l"
            elif direction == "r" and i != 0:
                i -= 1
                direction = "u"
            elif direction == "u" and j != num_col - 1:
                j += 1
                direction = "r"
            elif direction == "l" and i != num_row - 1:
                i += 1
                direction = "d"
            else:
                break
        elif map[i][j] == "|":
            if direction == "u" and i != 0:
                i -= 1
            elif direction == "d" and i != num_row - 1:
                i += 1
            elif direction in ("l", "r"):
                if i != 0 and ((i-1, j), "u") not in simulated_beam:
                    simulated_beam.append(((i-1, j), "u"))
                    simulate_beam("u", (i-1, j), map, simulated_beam, energized_tiles)
                if i != num_row -1 and ((i+1, j), "d") not in simulated_beam:
                    simulated_beam.append(((i+1, j), "d"))
                    simulate_beam("d", (i+1, j), map, simulated_beam, energized_tiles)
                break                
            else:
                break
        elif map[i][j] == "-":
            if direction == "l" and j != 0:
                j -= 1
            elif direction == "r" and j != num_row - 1:
                j += 1
            elif direction in ("u", "d"):
                if j != 0 and ((i, j-1), "l") not in simulated_beam:
                    simulated_beam.append(((i, j-1), "l"))
                    simulate_beam("l", (i, j-1), map, simulated_beam, energized_tiles)
                if j != num_col -1 and ((i, j+1), "r") not in simulated_beam:
                    simulated_beam.append(((i, j+1), "r"))
                    simulate_beam("r", (i, j+1), map, simulated_beam, energized_tiles)
                break                
            else:
                break

def count_energized_tiles(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        map = []
        for line in f:
            line = line.rstrip()
            row = []
            for char in line:
                row.append(char)
            map.append(row)
    simulated_beam = []
    energized_tiles = [["." for i in range(len(map[0]))] for j in range(len(map))]
    simulate_beam("r", (0,0), map, simulated_beam, energized_tiles)

    count = 0
    for line in energized_tiles:
        count += sum([char == "#" for char in line])
    return count

if __name__ == "__main__":
    print(count_energized_tiles("input.txt"))