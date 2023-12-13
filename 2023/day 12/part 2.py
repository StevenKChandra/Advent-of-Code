from functools import cache


def arrangement_is_valid(arrangement, row):
    if len(arrangement) > len(row):
        if arrangement[-1] != ".":
            return False
    return all(char_arrangement == char_row or char_row == "?"for char_arrangement, char_row in zip(arrangement, row))

@cache
def count_arrangements(row, group):
    first_group = group[0]
    suffix_len_min = sum(group[1:]) + len(group) - 1
    
    count = 0
    for prefix_len in range(len(row) - suffix_len_min - first_group + 1):
        arrangement = "." * prefix_len + "#" * first_group + "."
        if arrangement_is_valid(arrangement, row):
            if len(group) == 1:
                if all(char != "#" for char in row[len(arrangement):]):
                    count += 1
            else:
                count += count_arrangements(row[len(arrangement):], group[1:])
    
    return count

    

def sum_arrangement(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        rows = []
        groupings = []
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()
            line = line.split()

            rows.append(((line[0]+"?")*5)[:-1])
            groupings.append(tuple(int(num) for num in ((line[1]+",")*5)[:-1].split(",")))
            
    sum = 0

    for row, group in zip(rows, groupings):
        sum += count_arrangements(row, group)

    return sum

if __name__ == "__main__":
    print(sum_arrangement("input.txt"))