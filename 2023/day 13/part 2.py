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
