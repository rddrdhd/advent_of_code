#Task: https://adventofcode.com/2023/day/12

from functools import cache 

f = open('y2023/data/day12.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"

@cache
def count_possible_arrangements(row, groups):

    if not groups:
        return "#" not in row
    
    if not row:
        return len(groups) == 0

    result = 0

    curr_spring = row[0]
    the_rest_of_springs = row[1:]
    if curr_spring == OPERATIONAL or curr_spring == UNKNOWN:
        result += count_possible_arrangements(the_rest_of_springs, groups)

    curr_group_size = groups[0]
    the_rest_of_groups = groups[1:]
    if (    (curr_spring == DAMAGED or curr_spring == UNKNOWN)
        and curr_group_size <= len(row)
        and OPERATIONAL not in row[: curr_group_size]
        and (curr_group_size == len(row) or row[curr_group_size] != DAMAGED) ):
            
            result += count_possible_arrangements(row[curr_group_size + 1 :], the_rest_of_groups)

    return result

def part1():
    total = 0
    for line in lines:
        row, groups = line.split()
        groups = tuple(int(x) for x in groups.split(","))
        total += count_possible_arrangements(row, groups)
    return total

def part2():
    total = 0
    for line in lines:
        pattern, counts = line.split()
        pattern = "?".join([pattern] * 5)
        counts = tuple(int(x) for x in counts.split(",")) * 5
        total += count_possible_arrangements(pattern, counts)
    return total