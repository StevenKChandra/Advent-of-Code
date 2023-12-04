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

def find_number_and_star(text):
    """ """
    all_numbers_matches = []
    star_position = []

    for line in text: # iterate through the sets
        numbers = re.finditer("\d+", line)
        stars = re.finditer("\*", line)

        number_placeholder = []
        for number in numbers:
            number_placeholder.append((int(number.group()), [i for i in range(number.span()[0], number.span()[1])]))

        position = []
        for star in stars:
            position.append(star.span()[0])

        all_numbers_matches.append(number_placeholder)
        star_position.append(position)        

    return all_numbers_matches, star_position


def count_gear_number(line_number, numbers, star_position):
    count = 0
    product = 1
    used_number = []
    for i in range(max(line_number-1, 0), min(line_number+2, NUMBER_OF_LINES)):
        for j in range(max(star_position-1, 0), min(star_position+2, NUMBER_OF_CHARACTERS)):
            for number in numbers[i]:
                if j in number[1] and not number in used_number:
                    count += 1
                    product *= number[0]
                    used_number.append(number)
    if count == 2 :
        return product
    return 0

def sum_gear_numbers(numbers, stars_positions):
    """ """

    sum = 0

    i = 0
    for line in stars_positions:
        for star in line:
            sum += count_gear_number(i, numbers, star)
        i += 1
    return sum


if __name__== "__main__":


    text = parse_input("2023\day 03\input.txt")

    NUMBER_OF_LINES = len(text)
    NUMBER_OF_CHARACTERS = len(text[0])

    numbers, stars = find_number_and_star(text)

    print(sum_gear_numbers(numbers, stars))