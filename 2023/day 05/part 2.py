def parse_mappings(section, index):
    placeholder = section[index].split("\n")[1:]
    return [iterator.split(" ") for iterator in placeholder]


def convert(inputs, output_map):
    outputs = []
    for map in output_map:
        min_dest = int(map[0])
        min_source = int(map[1])
        difference = min_dest - min_source
        range = int(map[2])
        max_source = min_source + range
        for input in inputs:
            if input["min"] >= min_source and input["max"] <= max_source:
                outputs.append({"min": input["min"] + difference, "max": input["max"] + difference})
                input["min"] = input["max"]
            elif input["min"] >= min_source and max_source >= input["min"] and input["max"] >= max_source:
                outputs.append({"min": input["min"] + difference, "max": max_source + difference})
                input["min"] = max_source
            elif input["min"] <= min_source and min_source <= input["max"] and input["max"] <= max_source:
                outputs.append({"min": min_source + difference, "max": input["max"] + difference})
            elif input["min"] <= min_source and input["max"] >= max_source:
                outputs.append({"min": min_source + difference, "max": max_source + difference})
                inputs.append({"min": max_source,"max": input["max"]})
                input["max"] = min_source
    for input in inputs:
        if input["min"]!=input["max"]:
            outputs.append(input)

    return outputs

def find_minimum_location(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        section = f.read().split("\n\n")
        seed_mappings = section[0].split(" ")[1:]
        
        seeds = []
        for i in range(0, len(seed_mappings), 2):
            seeds.append({"min": int(seed_mappings[i]), "max": int(seed_mappings[i]) + int(seed_mappings[i+1])})
        soil_mappings = parse_mappings(section, 1)
        fertilizer_mappings = parse_mappings(section, 2) 
        water_mappings = parse_mappings(section, 3)
        light_mappings = parse_mappings(section, 4)
        temperature_mappings = parse_mappings(section, 5)
        humidity_mappings = parse_mappings(section, 6)
        location_mappings = parse_mappings(section, 7)
        
        
        soil = convert(seeds, soil_mappings)
        print(soil)
        fertilizer = convert(soil, fertilizer_mappings)
        print(fertilizer)
        water = convert(fertilizer, water_mappings)
        print(water)
        light = convert(water, light_mappings)
        print(light)
        temperature = convert(light, temperature_mappings)
        print(temperature)
        humidity = convert(temperature, humidity_mappings)
        print(humidity)
        location = convert(humidity, location_mappings)
        print(location)
        
        min_location = float("inf")
        for loc in location:
            if loc["min"] < min_location:
                min_location = loc["min"]
        

    return min_location
            
            
if __name__== "__main__":

    print(find_minimum_location("input.txt"))