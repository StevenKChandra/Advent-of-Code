def find_reflection_position(pattern):
    for i in range(len(pattern)-1):
        no_pattern = False
        for j in range(min(i+1, len(pattern)-i-1)):
            if no_pattern:
                continue
            if pattern[i-j] != pattern[i+j+1]:
                no_pattern = True
        
        if not no_pattern:
            return i+1
    return 0
                
def sum_arrangement(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        patterns = f.read().split("\n\n")

    patterns = [[row for row in pattern.split('\n')] for pattern in patterns]

    sum = 0
    for pattern in patterns:
        pattern_by_column = ["".join([pattern[j][i] for j in range(len(pattern))]) for i in range(len(pattern[0]))]
        sum += 100 * find_reflection_position(pattern) + find_reflection_position(pattern_by_column)
    
    return sum

if __name__ == "__main__":
    print(sum_arrangement("input.txt"))