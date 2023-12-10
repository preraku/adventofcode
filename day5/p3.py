from tqdm import tqdm
import multiprocessing as mp
from itertools import repeat
def get_lines(path: str) -> list:
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_seed_ranges(lines: list) -> list:
    seed_line = lines[0].split(':')[1]
    seed_line = seed_line.split()
    seeds = []
    for i in range(0, len(seed_line), 2):
        lo, rnge = seed_line[i], seed_line[i + 1]
        seeds.append((
            int(lo),
            int(lo) + int(rnge) - 1
        ))
    return seeds

def get_total_seeds(seeds: list) -> int:
    total_seeds = 0
    for seed_range in seeds:
        total_seeds += seed_range[1] - seed_range[0] + 1
    return total_seeds

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

def get_maps(lines: list) -> list:
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
    return all_maps

def get_location(seed: int, all_maps: list[list]) -> int:
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

# tqdm_it = tqdm(total=total_seeds)

# for lo, hi in seeds:
#     for seed in range(lo, hi + 1):
#         min_location = min(min_location, get_location(seed))
#         tqdm_it.update(1)

if __name__ == '__main__':
    lines = get_lines('sample1.txt')
    seeds = get_seed_ranges(lines)
    total_seeds = get_total_seeds(seeds)
    all_maps = get_maps(lines)
    maps = all_maps
    print(f"Total seeds: {total_seeds}")
    min_location = float('inf')
    for lo, hi in seeds:
        with mp.Pool(8) as pool:
            min_location = min(min_location, min(pool.map(get_location, range(lo, hi + 1), repeat(maps, hi - lo + 1))))
            # tqdm_it.update(hi - lo + 1)
    print(min_location)


# tqdm_it.close()
