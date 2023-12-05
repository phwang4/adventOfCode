def parse_almanac():
    with open('5.txt') as almanac:
        mapping_info = almanac.readlines()
        seeds = list(map(int, mapping_info[0].strip().split(':')[1].strip().split(' ')))
        maps = {}

        current_map = None
        for line in mapping_info[2:]:
            if ':' in line:
                current_map = line.strip()
                maps[current_map] = []
            else:
                mapping_numbers = line.strip().split(' ')
                if (mapping_numbers != ['']):
                    maps[current_map].append(list(map(int, mapping_numbers)))
        return seeds, maps

def get_destinations(seeds, maps, key):
    destinations = []
    for start_seed,end_seed in seeds:
        for destination, source, range in maps[key]:
            if (source < start_seed < (source + range)):
                destinations.append([destination + start_seed - source, end_seed])
                print(f'found mapping for {start_seed=} {source=}')
                break
    return destinations

def get_all_seeds(seeds):
    seed_pairs = []
    for x in range(0, len(seeds), 2):
        start = seeds[x]
        length = seeds[x+1]
        seed_pairs.append([start, length])
    return seed_pairs

seeds, maps = parse_almanac()
sources = get_all_seeds(seeds)
print(sources)
for key in maps:
    sources = get_destinations(sources, maps, key)
    print(f'updating for {key=}, destination={sources}')
print(min(sources))