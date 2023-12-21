from math import prod
def propagate_pulse(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        modules = {}
        io_pairs = {}
        for line in f:
            data = line.strip().split(" -> ")
            if data[0][0] == "%":
                modules[data[0][1:]] = {
                    "type": "flip-flop",
                    "destination": [destination for destination in data[1].split(", ")],
                    "state": False
                }
            elif data[0][0] == "&":
                modules[data[0][1:]] = {
                    "type": "conjunction",
                    "destination": [destination for destination in data[1].split(", ")],
                    "memory": None
                }
            else:
                modules[data[0]] = {
                    "type": data[0],
                    "destination": [destination for destination in data[1].split(", ")]
                }

            for destination in data[1].split(", "):
                if data[0] == "broadcaster":
                    if destination in io_pairs:
                        io_pairs[destination].append(data[0])
                    else:
                        io_pairs[destination] = [data[0]]
                else:
                    if destination in io_pairs:
                        io_pairs[destination].append(data[0][1:])
                    else:
                        io_pairs[destination] = [data[0][1:]]

    for key, value in modules.items():
        if value["type"] == "conjunction":
            value["memory"] = {input: False for input in io_pairs[key]}

    for input in io_pairs["rx"]:
        pattern = {input: None for input in io_pairs[input]}

    count = 0
    while not all([cycle !=  None for cycle in pattern.values()]):
        pulse_queue = [*simulate_pulse(modules, None, "broadcaster", False)]
        count += 1
        while pulse_queue:
            source, destination, pulse_type = pulse_queue.pop(0)
            new_pulse = simulate_pulse(modules, source, destination, pulse_type)
            if new_pulse:
                for pulse in new_pulse:
                    pulse_queue.append(pulse)
                if pulse[0] in pattern and pulse[1] == "gf" and pulse[2] and pattern[pulse[0]] ==  None:
                    pattern[pulse[0]] = count
    return prod(list(pattern.values()))

def simulate_pulse(modules, source, destination, pulse_type):
    if not destination in modules:
        return []
    module = modules[destination]
    if module["type"] == "flip-flop":
        if not pulse_type:
            module["state"] = not module["state"]
            return [(destination, new_destination, True and module["state"]) for new_destination in module["destination"]]
    elif module["type"] == "conjunction":
        module["memory"][source] = pulse_type
        if all([state == True for state in module["memory"].values()]):
            return [(destination, new_destination, False) for new_destination in module["destination"]]
        else:
            return [(destination, new_destination, True) for new_destination in module["destination"]]
    else:
        return [(destination, new_destination, pulse_type) for new_destination in module["destination"]]


if __name__ == "__main__":  
    # print(propagate_pulse("input.txt"))
    print(propagate_pulse("2023/day 20/input.txt"))