import re
import math

def parse_input(filepath):
    with open(filepath, "r") as f: # open the file

        time = re.findall("\d+",f.readline())
        time = int("".join(time))
        
        distance = re.findall("\d+",f.readline())
        distance = int("".join(distance))
    

    discriminant = math.sqrt(time**2-4*distance)

    lower_bound = math.floor((time-discriminant)/2+0.0000001)
    upper_bound = math.floor((time+discriminant)/2-0.0000001)

    power = (upper_bound - lower_bound)

    return power

print(parse_input("input.txt"))