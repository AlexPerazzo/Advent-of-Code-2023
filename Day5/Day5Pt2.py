def make_list(string):
    
    with open(f"Day5/{string}-map.txt") as file:
        foo = []
        for line in file:
            line = line.strip()
            foo.append(line)
    return foo


def convert(items_to_convert, converting_list):
    converted_list = []
    count = 0
    for item in items_to_convert:
        item = int(item)
        for info in converting_list:
            parts = info.split(" ")
            
            destination = int(parts[0])
            source = int(parts[1])
            range = int(parts[2])
            if item >= source and item <= source + range:
                converted_list.append(destination + (item - source))
                count += 1

    if count != len(converted_list):
        converted_list.append(item)

    return converted_list

def determine_seeds(seeds):
    all_seeds = []
    for i in range(0, len(seeds), 2):
        for j in range(int(seeds[i+1])):
            all_seeds.append(int(seeds[i]) + j)
            print(j)


    return all_seeds

with open("Day5/seeds.txt") as file:
    for line in file:
        line = line.strip()
        seeds = line.split(" ")

all_seeds = determine_seeds(seeds)

seed_to_soil = make_list("seed-to-soil")
soil_to_fertilizer = make_list("soil-to-fertilizer")
fertilizer_to_water = make_list("fertilizer-to-water")
water_to_light = make_list("water-to-light")
light_to_temperature = make_list("light-to-temperature")
temperature_to_humidity = make_list("temperature-to-humidity")
humidity_to_location = make_list("humidity-to-location")


soil = convert(all_seeds, seed_to_soil)
fertilizer = convert(soil, soil_to_fertilizer)
water = convert(fertilizer, fertilizer_to_water)
light = convert(water, water_to_light)
temperature = convert(light, light_to_temperature)
humidity = convert(temperature, temperature_to_humidity)
location = convert(humidity, humidity_to_location)

print(min(location))

## Maybe work backwards? What is the lowest location, then find the humidity based off that so on and so forth until you get a seed. Check if seed is in possible seeds.