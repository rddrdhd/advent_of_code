#Task: https://adventofcode.com/2023/day/5

import re
f = open('y2023/data/day05.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

class Mapa:
    # from array [50,98, 2] to source range(98..100) and destination range(50..52)
    # from array [52,50,48] to source range(50..98)  and destination range(52..100)
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


def part2():
    maps = get_maps(lines)
    seed_rs = []
    for x in re.findall('\d+ \d+',lines[0]):
        x_a = x.split(" ")
        seed_rs.append(range(int(x_a[0]),int(x_a[0])+int(x_a[1])))

    for map in maps:
        new_seed_rs = []

        while seed_rs:
            seed_r = seed_rs.pop()

            for i in range(map.count_rules):
                dest_r = map.destination_ranges[i]
                sour_r = map.source_ranges[i]

                # intersection
                inter_r = range(max(seed_r.start,sour_r.start),min(seed_r.stop,sour_r.stop))
                if inter_r.start < inter_r.stop:
                    diff = dest_r.start - sour_r.start
                    # add the intersected part to the new round pile
                    new_r = range(inter_r.start + diff, inter_r.stop + diff)
                    new_seed_rs.append(new_r)
                    # throw the rest back to the old round pile
                    if seed_r.start < inter_r.start:
                        seed_rs.append(range(seed_r.start, inter_r.start))
                    if seed_r.stop > inter_r.stop:
                        seed_rs.append(range(inter_r.stop, seed_r.stop))
                    break 
            else:
                # ranges for which no rules were found
                new_seed_rs.append(seed_r)  

        seed_rs = new_seed_rs

    sorted = [r.start for r in new_seed_rs]
    return min(sorted) # 72263011
