import re

def sum_extrapolation(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        sum = 0
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()

            history = re.findall("-?[\d]+", line)
            history = [int(number) for number in history]
            sum += extrapolate_next(history)

    return sum

def extrapolate_next(datas):
    data_length = len(datas)

    if datas == [0]*(data_length-1):
        return 0
    
    difference = []
    for i in range(data_length-1):
        difference.append(datas[i+1]-datas[i])

    return datas[-1] + extrapolate_next(difference)

if __name__ == "__main__":
    print(sum_extrapolation("input.txt"))