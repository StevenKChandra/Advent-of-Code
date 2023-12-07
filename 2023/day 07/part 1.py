import random

def identify_type(cards):


    card_labels = {}
    for char in cards:
        if not char in card_labels:
            card_labels[char] = 1
        else:
            card_labels[char] += 1
    
    if len(card_labels) == 1:
        return "five of a kind"
    
    elif 4 in card_labels.values():
        return "four of a kind"
    
    elif 3 in card_labels.values():

        if 2 in card_labels.values():
            return "full house"
        
        return "three of a kind"
    
    elif len(card_labels) == 3:
        return "two pair"
    
    elif len(card_labels) == 4:
        return "one pair"
    
    return "high card"

def compare(first_hand, second_hand):
    if TYPE_RANK.index(first_hand["type"]) > TYPE_RANK.index(second_hand["type"]):
        return True
    elif TYPE_RANK.index(first_hand["type"]) == TYPE_RANK.index(second_hand["type"]):
        for i in range(len(first_hand["cards"])):
            if LABEL_RANK.index(first_hand["cards"][i]) > LABEL_RANK.index(second_hand["cards"][i]):
                return True
            elif LABEL_RANK.index(first_hand["cards"][i]) < LABEL_RANK.index(second_hand["cards"][i]):
                return False
    return False

def quick_sort(hands):
    if len(hands) < 2 :
        return hands
    pivot = [hands[0], hands[len(hands)//2], hands[-1]]
    random.shuffle(pivot)
    pivot = pivot[0]


    left = []
    right = []
    for hand in hands:
        if compare(hand, pivot):
            right.append(hand)
        else:
            left.append(hand)
    
    return (quick_sort(left)+quick_sort(right))


def parse_input(filepath):
    with open(filepath, "r") as f: # open the file
        
        hands = []
        for line in f:
            line = line.strip().split()
            
            hand = {}
            hand["cards"] = line[0]
            hand["type"] = identify_type(line[0])
            hand["bids"] = int(line[1])

            hands.append(hand)

    return hands

def sum_winnings(hands):
    winnings = 0
    for i in range(len(hands)):
        winnings += (i+1)*hands[i]["bids"]
    return winnings

TYPE_RANK = ["high card", "one pair", "two pair", "three of a kind", "full house", "four of a kind", "five of a kind"]
LABEL_RANK = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

if __name__ == "__main__":
    hands = parse_input("input.txt")
    hands = quick_sort(hands)
    print(sum_winnings(hands))