import re
from math import lcm

def parse_input(filepath):
    """ """

    with open(filepath, "r") as f: # open the file

        instruction = f.readline().strip()

        f.readline()

        starting_points = []
        mappings = {}
        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()
            data = re.findall("[A-Z]+", line)
            if data[0][-1] == "A":
                starting_points.append(data[0])
            mappings[data[0]] = {"L": data[1], "R": data[2]}

    return instruction, starting_points, mappings

def check_is_finished(points):
    for point in points:
        if point[-1] != "Z":
            return False
    return True

def count_steps(instruction, starting_points, mappings):
    INSTRUCTION_LENGTH = len(instruction)

    step_list = []
    for point in starting_points:
        steps_count = 0
        current_step = point
        while current_step[-1] != "Z":
            current_step = mappings[current_step][instruction[(steps_count)%INSTRUCTION_LENGTH]]
            steps_count += 1
        step_list.append(steps_count)

    return lcm(*step_list)

if __name__ == "__main__":
    instruction, starting_points, mappings = parse_input("input.txt")
    print(count_steps(instruction, starting_points, mappings))