def calculate_hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value = (value * 17) % 256
    return value

def arrange_boxes(boxes, string):
    if "=" in string:
        label, focal_length = string.split("=")
        box_num = calculate_hash(label)
        boxes[box_num][label] = int(focal_length)
    elif "-" in string:
        label = string[:-1]
        box_num = calculate_hash(label)
        if label in boxes[box_num]:
            boxes[box_num].pop(label)

def sum_hash(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        strings = [string for string in f.readline().strip().split(",")]

    boxes = {num:{} for num in range(256)}
    for string in strings:
        arrange_boxes(boxes, string)
    
    sum = 0
    for box_num, lenses in boxes.items():
        slot_number = 1
        for lense in lenses.items():
            sum += (box_num + 1) * slot_number * lense[1]
            slot_number += 1
    
    return sum


if __name__ == "__main__":
    print(sum_hash("input.txt"))