def calculate_hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value = (value * 17) % 256
    return value

def sum_hash(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        return sum([calculate_hash(string) for string in f.readline().strip().split(",")])

if __name__ == "__main__":
    print(sum_hash("input.txt"))