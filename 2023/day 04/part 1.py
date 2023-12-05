def sum_points(filepath):
    """ """

    points = 0
    with open(filepath, "r") as f: # open the file
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()

            line = line.split(": ")[1].split(" | ")

            winning_numbers = line[0].split()
            list_of_numbers = line[1].split()

            current_card_points = 0
            for number in winning_numbers:
                if number in list_of_numbers:
                    if current_card_points == 0:
                        current_card_points = 1
                        print(number)
                    else:
                        current_card_points *= 2
            points += current_card_points
            
    return points

if __name__== "__main__":

    print(sum_points("input.txt"))