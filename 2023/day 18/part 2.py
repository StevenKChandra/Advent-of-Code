def calculate_lava_volume(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        dig_plan = [line.strip().split() for line in f]

    DIRECTIONS = {3: (-1,0), 1:(1,0), 2:(0,-1), 0:(0,1)}

    i = 0
    j = 0
    area = 0
    for instruction in dig_plan:
        previous_i = i
        previous_j = j
        direction = DIRECTIONS[int(instruction[2][-2])]
        i += direction[0] * int(instruction[2][2:-2], 16)
        j += direction[1] * int(instruction[2][2:-2], 16)
        print(i,j)
        area += 0.5*(previous_j * i - previous_i * j) + 0.5*(abs(previous_i - i) + abs(previous_j - j))
    print(i,j)

    return int(area + 1)


if __name__ == "__main__":  
    print(calculate_lava_volume("input.txt"))
    # print(calculate_lava_volume("2023/day 18/input.txt"))
    # print(calculate_lava_volume("test_input.txt"))
    # print(calculate_lava_volume("2023/day 18/test_input.txt"))