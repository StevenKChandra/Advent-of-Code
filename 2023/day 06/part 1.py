import re
import math

def parse_input(filepath):
    with open(filepath, "r") as f: # open the file
        
        time = re.findall("\d+",f.readline())
        time = [int(i) for i in time]

        distance = re.findall("\d+",f.readline())
        distance = [int(i) for i in distance]
    
    power = 1
    for i in range(len(time)):
        discriminant = math.sqrt(time[i]**2-4*distance[i])

        lower_bound = math.floor((time[i]-discriminant)/2+0.0000001)
        upper_bound = math.floor((time[i]+discriminant)/2-0.0000001)

        power *= (upper_bound - lower_bound)

    return power

print(parse_input("input.txt"))