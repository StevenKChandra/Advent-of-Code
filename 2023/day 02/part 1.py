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

def is_possible(sets):
    """ function to determine whether sets of cubes fulfils 
        the MAX_CUBES constrain returns a boolean"""
    
    for set in sets: # iterate through the sets
        set = set.split(", ")

        for cubes in set: # see each cubes in a set

            # extract the number of cubes and their color
            num, color = cubes.split()

            # if not within the constrain, return False
            if int(num) > MAX_CUBES[color]:
                return False
            
    return True


def sum_possible_games(text):
    """ function to sum the possible games number from the list of lines
        takes a list of lines as input and returns a sum"""

    sum = 0

    for game_number in range(len(text)): # iterate through the text

        # split games into sets
        sets = text[game_number].split(": ")[1].split("; ")

        # if the sets are all possible, add game number to the sum
        if is_possible(sets):
            sum += game_number + 1
    
    return sum

def calculate(line_digits):
    """ sums the calibration numbers 
        takes a list of digits and returns an integer"""
        
    sum = 0

    for digits in line_digits: # iterate through the list
        sum += digits[0]*10 + digits[-1] # sum the calibration number

    return sum

if __name__== "__main__":

    MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

    text = parse_input("input.txt")

    print(sum_possible_games(text))