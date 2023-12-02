from functools import reduce

def parse_input(filepath):
    """ function to parse the input text document into text with lines
        takes file path as input and returns a list of lines"""

    text = []
    with open(filepath, "r") as f: # open the file
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()
            text.append(line)

    return text

def power_of_cubes(sets):
    """ function to determine whether sets of cubes fulfils 
        the MAX_CUBES constrain, returns a boolean"""
    
    minimum_cubes = {}
    for set in sets: # iterate through the sets
        set = set.split(", ")

        for cubes in set: # see each cubes in a set

            # extract the number of cubes and their color
            num, color = cubes.split()

            # if not within the constrain, return False
            if not color in minimum_cubes:
                minimum_cubes[color] = 0
            if minimum_cubes[color] < int(num):
                minimum_cubes[color] = int(num)
    
    return reduce(lambda x, y: x * y, minimum_cubes.values())


def sum_power_of_cubes(text):
    """ function to sum the power of cubes from each games
        takes a list of lines as input and returns a sum"""

    sum = 0

    for game_number in range(len(text)): # iterate through the text

        # split games into sets
        sets = text[game_number].split(": ")[1].split("; ")

        # if the sets are all possible, add game number to the sum
        sum += power_of_cubes(sets)
    
    return sum

def calculate(line_digits):
    """ sums the calibration numbers 
        takes a list of digits and returns an integer"""
        
    sum = 0

    for digits in line_digits: # iterate through the list
        sum += digits[0]*10 + digits[-1] # sum the calibration number

    return sum

if __name__== "__main__":

    text = parse_input("input.txt")

    print(sum_power_of_cubes(text))