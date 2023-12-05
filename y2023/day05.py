#Task: https://adventofcode.com/2023/day/5

import re
f = open('y2023/data/day05.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

class Mapa:
    def __init__(self, arrays_of_numbers):
        destination_ranges = []
        source_ranges = []
        for a in arrays_of_numbers:
            destination_ranges.append(range(a[0], a[0]+a[2]))
            source_ranges.append(range(a[1], a[1]+a[2]))

        self.destination_ranges = destination_ranges
        self.source_ranges = source_ranges
        self.count_rules = len(arrays_of_numbers)

    def __repr__(self) -> str:
        string = "MAP: ("+str(self.count_rules)+")\n"
        for i in range(len(self.destination_ranges)):
            string+=str(self.source_ranges[i])
            string+="->"
            string+=str(self.destination_ranges[i])
            string+="\n"
        return string

def get_maps(lines):
    maps = []
    rules = []
    for line in lines[3:]:
        nums = [int(x) for x in re.findall('\d+',line)]
        if nums:
            rules.append(nums)
        elif line == '':
            mapa = Mapa(rules)
            rules = []
            maps.append(mapa)
    return maps

def part1():
    # init maps with rules
    maps = get_maps(lines)
    seeds = [int(x) for x in re.findall('\d+',lines[0])]
    new_seeds = []
    for map in maps:
        for seed in seeds:
            seed_found = False
            i = 0
            while not seed_found and i < map.count_rules:
                if seed in map.source_ranges[i]:
                    seed_found = True
                    index = seed - map.source_ranges[i][0]
                    new_seeds.append(map.destination_ranges[i][index])
                i+=1
            if not seed_found:
                new_seeds.append(seed)
        seeds = new_seeds.copy()
        new_seeds = []
    return min(seeds) # 251346198

#WIP
def part2():
    maps = get_maps(lines)
    seed_ranges = []
    for x in re.findall('\d+ \d+',lines[0]):
        xs = x.split(" ")
        seed_ranges.append(range(int(xs[0]),int(xs[0])+int(xs[1])))
    print(seed_ranges)
    new_seed_ranges = []
    for map in maps:
        for seed_range in seed_ranges:
            range_found = False
            i = 0
            while not range_found and i < map.count_rules:
                intersection = range(max(seed_range.start,map.source_ranges[i].start), min(seed_range.stop,map.source_ranges[i].stop)) or None
                print(seed_range,"&",map.source_ranges[i],"\t->",end=" ")
                if intersection:
                    print(intersection)
                else:
                    print("no intersection")
                i+= 1
            if not range_found:
                new_seed_ranges.append(seed_range)
        seed_ranges = new_seed_ranges.copy()
        new_seed_ranges = []
    return 0