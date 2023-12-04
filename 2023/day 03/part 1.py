import re

def parse_input(filepath):
    """ """

    text = []
    with open(filepath, "r") as f: # open the file
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()
            text.append(line)

    return text

def parse_number_and_symbols(text):
    """ """
    all_numbers_matches = []
    symbols_position = []

    for line in text: # iterate through the sets
        numbers = re.finditer("\d+", line)
        symbols = re.finditer("[^\d^\.]", line)


        position = []
        for match in symbols:
            position.append(match.span()[0])

        all_numbers_matches.append(numbers)
        symbols_position.append(position)        

    return all_numbers_matches, symbols_position


def find_symbol(line_number, number_position, symbols):
    for i in range(max(line_number-1, 0), min(line_number+2, NUMBER_OF_LINES)):
        for j in range(max(number_position[0]-1, 0), min(number_position[1]+1, NUMBER_OF_CHARACTERS)):
            if j in symbols[i]:
                return True
    return False

def sum_valid_numbers(numbers, symbols):
    """ """

    sum = 0

    i = 0
    for line in numbers:
        for number in line:
            if find_symbol(i, number.span(), symbols):
                sum += int(number.group())
        i += 1
    return sum


if __name__== "__main__":


    text = parse_input("input.txt")

    NUMBER_OF_LINES = len(text)
    NUMBER_OF_CHARACTERS = len(text[0])

    numbers, symbols = parse_number_and_symbols(text)

    print(sum_valid_numbers(numbers, symbols))