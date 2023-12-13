def find_reflection_position(pattern, initial = 0):
    for i in range(len(pattern)-1):
        no_pattern = False
        for j in range(min(i+1, len(pattern)-i-1)):
            if no_pattern:
                continue
            if pattern[i-j] != pattern[i+j+1]:
                no_pattern = True
        
        if not no_pattern and i+1 != initial:
            return i+1
    return 0

def reverse(char):
    if char == ".": return "#"
    else: return "."

def sum_arrangement(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        patterns = f.read().split("\n\n")

    patterns = [[row for row in pattern.split('\n')] for pattern in patterns]

    sum = 0
    for pattern in patterns:
        pattern_by_column = ["".join([pattern[j][i] for j in range(len(pattern))]) for i in range(len(pattern[0]))]
        no_pattern = True
        initial_row = find_reflection_position(pattern)
        initial_col = find_reflection_position(pattern_by_column)
        row = initial_row
        col = initial_col
        i = 0
        while no_pattern and i < len(pattern):
            j = 0
            while no_pattern and j < len(pattern[0]):
                pattern[i] = "".join([pattern[i][k] if k != j else reverse(pattern[i][k]) for k in range(len(pattern[i]))])
                pattern_by_column[j] = "".join([pattern_by_column[j][k] if k != i else reverse(pattern_by_column[j][k]) for k in range(len(pattern_by_column[j]))])
                row = find_reflection_position(pattern, initial_row)
                col = find_reflection_position(pattern_by_column, initial_col)
                if (row != 0 and row != initial_row) or (col != 0 and col != initial_col):
                    no_pattern = False
                    print(i,j)
                pattern[i] = "".join([pattern[i][k] if k != j else reverse(pattern[i][k]) for k in range(len(pattern[i]))])
                pattern_by_column[j] = "".join([pattern_by_column[j][k] if k != i else reverse(pattern_by_column[j][k]) for k in range(len(pattern_by_column[j]))])
                j += 1
            i += 1
        if row != 0 and row != initial_row:
            sum += 100 * row
        else:
            sum += col
    return sum

if __name__ == "__main__":
    print(sum_arrangement("input.txt"))
    # print(sum_arrangement("2023/day 13/input.txt"))
    # print(sum_arrangement("2023/day 13/test.txt"))

d = [[list(y) for y in x.split("\n")] for x in open("input.txt").read().split("\n\n")]

def f(mirror, old_reflection = 0):
    for i in range(1, len(mirror[0])):
        m = min([len(mirror[0][:i]),len(mirror[0][i:])])
        if len(mirror[0][:i]) < len(mirror[0][i:]):
            if [x[:i] for x in mirror] == [x[i:i+m][::-1] for x in mirror]:
                if i != old_reflection:
                    return i
        if len(mirror[0][:i]) > len(mirror[0][i:]):
            if [x[i-m:i] for x in mirror] == [x[i:][::-1] for x in mirror]:
                if i != old_reflection:
                    return i 
    for i in range(1, len(mirror)):
        m = min([len(mirror[:i]),len(mirror[i:])])
        if len(mirror[:i]) < len(mirror[i:]):
            if mirror[:i] == mirror[i:i+m][::-1]:
                if i* 100 != old_reflection:
                    return i * 100
        if len(mirror[:i]) > len(mirror[i:]):
            if mirror[i-m:i] == mirror[i:][::-1]:
                if i* 100 != old_reflection:
                    return i * 100
    return 0

def smudge_removal(mirror, old_reflection):
    for row in range(len(mirror)):
        for col in range(len(mirror[0])):
            if mirror[row][col] == "#":
                mirror[row][col] = "."
                new_reflection = f(mirror, old_reflection = old_reflection)
                if new_reflection != 0:
                    print(row,col)
                    return new_reflection 
                else: 
                    mirror[row][col] = "#"
            if mirror[row][col] == ".":
                mirror[row][col] = "#"
                new_reflection = f(mirror, old_reflection = old_reflection )
                if new_reflection != 0:
                    print(row,col)
                    return new_reflection 
                else: 
                    mirror[row][col] = "."
    return 0

part_1 = 0 
part_2 = 0
for mirror in d:
    old_reflection = f(mirror)
    part_1 += old_reflection
    part_2 += smudge_removal(mirror, old_reflection)
                    
print("Part 1", part_1)
print("Part 2", part_2)

