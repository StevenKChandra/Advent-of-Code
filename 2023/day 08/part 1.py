import re

def parse_instuction_and_mapping(filepath):
    """ """

    with open(filepath, "r") as f: # open the file

        instruction = f.readline().strip()

        f.readline()

        mapping = {}

        for line in f: # iterate through the text
            
            # strip the endlines
            line = line.strip()
            data = re.findall("[A-Z]+", line)
            mapping[data[0]] = {"L": data[1], "R": data[2]}

    return instruction, mapping

def count_steps(instruction, mapping):
    INSTRUCTION_LENGTH = len(instruction)

    steps_count = 0
    current_step = "AAA"
    while current_step != "ZZZ":
        current_step = mapping[current_step][instruction[(steps_count)%INSTRUCTION_LENGTH]]
        steps_count += 1

    return steps_count

if __name__ == "__main__":
    instruction, mapping = parse_instuction_and_mapping("input.txt")
    print(count_steps(instruction, mapping))