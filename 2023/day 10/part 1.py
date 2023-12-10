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
                    next = (i-1, j)
            
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
    return len(path)//2


if __name__ == "__main__":
    print(parse_text("input.txt"))