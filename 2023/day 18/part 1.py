def calculate_lava_volume(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        dig_plan = [line.strip().split() for line in f]

    DIRECTIONS = {"U": (-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}

    i = 0
    j = 0
    i_min = 0
    i_max = 0
    j_min = 0
    j_max = 0
    for instruction in dig_plan:
        direction = DIRECTIONS[instruction[0]]
        i += direction[0] * int(instruction[1])
        j += direction[1] * int(instruction[1])
        if i_min > i:
            i_min = i
        if i_max < i:
            i_max = i
        if j_min > j:
            j_min = j
        if j_max < j:
            j_max = j
    i_range = i_max - i_min + 1
    j_range = j_max - j_min + 1

    map = [["." for j in range(j_range)] for i in range(i_range)]
    i = -i_min
    j = -j_min

    for instruction in dig_plan:
        for k in range(int(instruction[1])):
            direction = DIRECTIONS[instruction[0]]
            i += direction[0]
            j += direction[1]
            map[i][j] = "#"

    def translate_char(i, j, map):
        up, down, left, right = False, False, False, False
        if i != 0 and map[i-1][j] == "#":
            up = True
        if i != len(map)-1 and map[i+1][j] == "#":
            down = True
        if j != 0 and map[i][j-1] == "#":
            left = True
        if j != len(map[0])-1 and map[i][j+1] == "#":
            right = True
        translation = {
            (True,True,False,False) : "|",
            (True,False,True,False) : "J",
            (True,False,False,True) : "L",
            (False,True,True,False) : "7",
            (False,True,False,True) : "F",
            (False,False,True,True) : "-"
        }
        return translation[(up,down, left, right)]

    count = 0
    for i in range (i_range):
        inside = False
        last_barrier = None
        for j in range(j_range):
            if map[i][j] == "#":
                char = translate_char(i,j,map) 
                if char == "-" and char != "S":
                    continue
                if last_barrier == "L" and char =="7":
                    last_barrier = char
                    continue
                if last_barrier == "F" and char =="J":
                    last_barrier = char
                    continue
                inside = not inside
                last_barrier = char
            else:
                if inside:
                    count += 1
    for row in map:
        count += sum([char == "#" for char in row])
    return count

if __name__ == "__main__":  
    print(calculate_lava_volume("input.txt"))