# Task: https://adventofcode.com/2022/day/6

f = open('y2022/data/day06.txt', 'r')
lines = f.readlines()
f.close()


line = lines[0].strip()

def get_marker_end_position(marker_length):
    for i in range(len(line) - marker_length):
        chunk = line[i:i + marker_length]
        if len(chunk) == len(list(set(chunk))):
            return i + marker_length


def part1():
    return get_marker_end_position(4)
    
    
def part2():
    return get_marker_end_position(14)
