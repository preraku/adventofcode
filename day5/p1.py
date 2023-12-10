with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

def process_map(data_list, lines, row) -> int:
    while row < len(lines) and lines[row] != '':
        dest, source, interval = lines[row].split()
        data_list.append((
            int(source),
            int(source) + int(interval) - 1,
            int(dest),
            int(interval)
        ))
        row += 1
    return row + 2

seeds = lines[0].split(':')[1]
seeds = [int(val) for val in seeds.split()]
# seed = seeds[0]

row = 3
seed_to_soil = []
row = process_map(seed_to_soil, lines, row)

soil_to_fertilizer = []
row = process_map(soil_to_fertilizer, lines, row)

fertilizer_to_water = []
row = process_map(fertilizer_to_water, lines, row)

water_to_light = []
row = process_map(water_to_light, lines, row)

light_to_temperature = []
row = process_map(light_to_temperature, lines, row)

temperature_to_humidity = []
row = process_map(temperature_to_humidity, lines, row)

humidity_to_location = []
row = process_map(humidity_to_location, lines, row)

all_maps = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
]

def get_location(seed: int) -> int:
    for m in all_maps:
        # Search for the seed in the range [m[0], m[1]]
        displacement = 0
        for interval in m:
            lo, hi = interval[0], interval[1]
            if lo <= seed <= hi:
                displacement = - lo + interval[2]
                break
        seed = seed + displacement
    return seed

locations = [get_location(seed) for seed in seeds]
# print(locations)
print(min(locations))