def parse_text(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        i = 0
        text = []
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()

            text.append(line)

            j = 0
            for char in line:

                if char == "S":
                    starting_point = (i, j)
                    prev = (i, j)
                    next = (i+1, j)
                    # next = (i, j+1)
            
                j += 1
            
            i += 1
    
    
    path = [starting_point, next]
    while next != starting_point:
        char = text[next[0]][next[1]]
        if char == "|":
            if prev[0] == next[0]-1:
                prev = next
                next = (next[0]+1, next[1])
            else:
                prev = next
                next = (next[0]-1, next[1])
        if char == "-":
            if prev[1] == next[1]-1:
                prev = next
                next = (next[0], next[1]+1)
            else:
                prev = next
                next = (next[0], next[1]-1)
        if char == "L":
            if prev[0] == next[0]-1:
                prev = next
                next = (next[0], next[1]+1)
            else:
                prev = next
                next = (next[0]-1, next[1])
        if char == "J":
            if prev[0] == next[0]-1:
                prev = next
                next = (next[0], next[1]-1)
            else:
                prev = next
                next = (next[0]-1, next[1])
        if char == "7":
            if prev[0] == next[0]+1:
                prev = next
                next = (next[0], next[1]-1)
            else:
                prev = next
                next = (next[0]+1, next[1])
        if char == "F":
            if prev[0] == next[0]+1:
                prev = next
                next = (next[0], next[1]+1)
            else:
                prev = next
                next = (next[0]+1, next[1])
        path.append(next)

    i_max = len(text)
    j_max = len(text[0])
    area_count = 0
    inside = False
    for i in range(i_max):
        inside = False
        last_barrier = None
        for j in range(j_max):
            char = text[i][j]
            if (i, j) in path:
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
                    area_count += 1
    return area_count


if __name__ == "__main__":
    print(parse_text("input.txt"))
