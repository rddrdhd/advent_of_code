#Task: https://adventofcode.com/2022/day/1
f = open('y2018/data/day03.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

import re

def part1():
    #TODO there has to be a better way :/
    used_fabric_coords=()
    overlaps={}
    for line in lines:
        _, x_coord, y_coord, x_size, y_size = re.findall(r'[0-9]+', line)
        x_coord, y_coord, x_size, y_size = int(x_coord), int(y_coord), int(x_size), int(y_size)
        for x in range(x_coord, x_coord+x_size):
            for y in range(y_coord, y_coord+y_size):
                coords = (x,y)
                if coords in used_fabric_coords:
                    if coords in overlaps:
                        overlaps[coords]+=1
                    else:
                        overlaps[coords]=2
                else:
                    used_fabric_coords=(coords,)+ used_fabric_coords
    return len(overlaps) # 114946

def part2():
    return 0
