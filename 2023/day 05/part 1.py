def parse_mappings(section, index):
    placeholder = section[index].split("\n")[1:]
    return [iterator.split(" ") for iterator in placeholder]


def convert(iterator, datas):
    for data in datas:
        if iterator in range(int(data[1]), int(data[1])+int(data[2])):
            return iterator + int(data[0]) - int(data[1])
    return iterator 

def find_minimum_location(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        section = f.read().split("\n\n")
        seed_mappings = section[0].split(" ")[1:]
        soil_mappings = parse_mappings(section, 1)
        fertilizer_mappings = parse_mappings(section, 2) 
        water_mappings = parse_mappings(section, 3)
        light_mappings = parse_mappings(section, 4)
        temperature_mappings = parse_mappings(section, 5)
        humidity_mappings = parse_mappings(section, 6)
        location_mappings = parse_mappings(section, 7)
        
        min_location = float("inf")
        for seed in seed_mappings:
            soil = convert(int(seed), soil_mappings)
            fertilizer = convert(int(soil), fertilizer_mappings)
            water = convert(int(fertilizer), water_mappings)
            light = convert(int(water), light_mappings)
            temperature = convert(int(light), temperature_mappings)
            humidity = convert(int(temperature), humidity_mappings)
            location = convert(int(humidity), location_mappings)
            
            print(soil, fertilizer, water, light, temperature, humidity, location)
            if min_location > location:
                min_location = location

    return min_location
            
            
if __name__== "__main__":

    print(find_minimum_location("input.txt"))