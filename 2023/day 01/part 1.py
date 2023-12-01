def parse_input(filepath):
    """ function to parse the input text document into text with lines
        takes file path as input and returns a list of lines"""

    text = []
    with open(filepath, "r") as f: # open the file
        for line in f: # iterate through the text
            line = line.strip()
            text.append(line)

    return text

def extract_digits(text):
    """ function to extract the digits from the list of lines
        takes a list of lines as input and returns a list of digits"""

    line_digits = []

    for line in text: # iterate through the text
        digits = []
        for char in line: # iterate through the line
            if char.isdigit(): # check if the character is a digit
                digits.append(int(char))

        line_digits.append(digits)
    
    return line_digits

def calculate(line_digits):
    """ sums the calibration numbers 
        takes a list of digits and returns an integer"""
        
    sum = 0

    for digits in line_digits: # iterate through the list
        sum += digits[0]*10 + digits[-1] # sum the calibration number

    return sum

if __name__== "__main__":
    text = parse_input("input.txt")

    line_digits = extract_digits(text)

    print(calculate(line_digits))