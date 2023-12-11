def sum_distance(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        i = 0
        text = []
        galaxies = []
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()
            text.append(line)

            j = 0
            for char in line:

                if char == "#":
                    galaxies.append((i, j))

                j += 1
            
            i += 1
    
    empty_rows = []
    empty_columns = []
    NUMBER_OF_ROWS = len(text)
    NUMBER_OF_COLUMNS = len(text[0])

    for i in range(NUMBER_OF_ROWS):
        if  text[i] == "."*NUMBER_OF_ROWS:
            empty_rows.append(i)

    for i in range(NUMBER_OF_ROWS):
        if [line[i] for line in text] == ["."]*NUMBER_OF_COLUMNS:
            empty_columns.append(i)
    
    distance_sum = 0
    GALAXY_COUNT = len(galaxies)
    for i in range(GALAXY_COUNT):
        for j in range(i+1, GALAXY_COUNT):
            first_galaxy = galaxies[i]
            second_galaxy = galaxies[j]
            
            distance_sum += abs(first_galaxy[0] - second_galaxy[0])
            distance_sum += abs(first_galaxy[1] - second_galaxy[1])

            for k in empty_rows:
                if k in range(min(first_galaxy[0], second_galaxy[0]), max(first_galaxy[0], second_galaxy[0])):
                    distance_sum += 999999
            for k in empty_columns:
                if k in range(min(first_galaxy[1], second_galaxy[1]), max(first_galaxy[1], second_galaxy[1])):
                    distance_sum += 999999
    
    return distance_sum
    
if __name__ == "__main__":
    print(sum_distance("input.txt"))