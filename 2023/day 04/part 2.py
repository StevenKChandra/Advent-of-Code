def parse_input(filepath):
    """ """

    cards = {}
    card_number = 1
    with open(filepath, "r") as f:
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()

            line = line.split(": ")[1].split(" | ")

            cards[card_number] = {"winning numbers": line[0].split(), "list of numbers": line[1].split(), "number of instance": 1}

            card_number += 1

    return cards

def count_number_of_cards(cards):

    count = 0
    for card in cards:
        matching_count = 0
        for number in cards[card]["winning numbers"]:
            if number in cards[card]["list of numbers"]:
                matching_count += 1
        for i in range(1, matching_count+1):
            if (card+i) in cards:
                cards[card+i]["number of instance"] += cards[card]["number of instance"]
        count += cards[card]["number of instance"]
    return count


if __name__== "__main__":

    cards = parse_input("input.txt")
    
    print(count_number_of_cards(cards))