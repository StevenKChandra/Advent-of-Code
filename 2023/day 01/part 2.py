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

        # set starting point at index 0
        start_point = 0

        for end_point in range(len(line)): # iterate end point through the line

            # check if the endpoint is a digit
            if line[end_point].isdigit():

                # if so, record the digit               
                digits.append(int(line[end_point]))

                # set the starting point at the next index
                # as it is not possible to create a digit string with number
                start_point = end_point + 1
            
            # find if there is digit string from the starting point to the endpoint
            for digit_string in DIGITS:
                if digit_string in line[start_point:end_point + 1]:
                    
                    # if so, record the digit
                    digits.append(DIGITS.index(digit_string))

                    # set the starting point at (the start of the digit string + 1)
                    # since the rest of the string might be a part of other digit string 
                    start_point += line[start_point:end_point+1].index(digit_string) + 1
                    break

        line_digits.append(digits)
    
    return line_digits

def calculate(line_digits):
    """ sums the calibration numbers 
        takes a list of digits and returns an integer"""
        
    sum = 0

    for digits in line_digits: # iterate through the list
        sum += digits[0]*10 + digits[-1] # sum the calibration number
        # print(sum)

    return sum

if __name__== "__main__":
    DIGITS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    text = parse_input("input.txt")

    line_digits = extract_digits(text)

    print(calculate(line_digits))