import itertools

def sum_arrangement(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        damaged_list = []
        unknown_list = []
        groupings_list = []
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()
            line = line.split()

            damaged = []
            unknown = []

            i = 0
            for char in line[0]:
                if char == "#":
                    damaged.append(i)
                if char == "?":
                    unknown.append(i)
                i += 1
            
            damaged_list.append([int(num) for num in damaged])
            unknown_list.append([int(num) for num in unknown])
            groupings_list.append([int(num) for num in line[1].split(",")])
            
    sum = 0
    for i in range(len(damaged_list)):
        total_damaged = 0
        for num in groupings_list[i]:
            total_damaged += num
        current_damaged = len(damaged_list[i])
        required_damaged = total_damaged - current_damaged

        possible_arrangement = itertools.combinations(unknown_list[i], required_damaged)

        for arrangement in possible_arrangement:
            damaged = sorted(damaged_list[i] + [num for num in arrangement])

            groupings =[]
            k = 1
            for j in range(1, len(damaged)):
                if damaged[j] == damaged[j-1] + 1:
                    k += 1
                else:
                    groupings.append(k)
                    k = 1
            groupings.append(k)

            if groupings == groupings_list[i]:
                sum += 1
    return sum

if __name__ == "__main__":
    print(sum_arrangement("input.txt"))