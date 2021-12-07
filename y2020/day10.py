# Task: https://adventofcode.com/2021/day/X
from collections import defaultdict

f = open('y2020/data/test.txt', 'r')
lines = f.readlines()
f.close()


def get_all_adapters():
    adapters_out_joltage = list(map(int, lines))
    adapters_out_joltage.sort()
    another_adapter = adapters_out_joltage[-1] + 3
    adapters_out_joltage.append(another_adapter)
    return adapters_out_joltage


def part1():
    differences = [0, 0, 0]  # differences for 1, 2, 3 jolts
    last_adapter = 0  # starting socket
    adapters = get_all_adapters()
    for adapter in adapters:
        difference = adapter - last_adapter
        differences[(difference - 1) % 3] += 1  # Oth index for difference 1
        last_adapter = adapter
    return differences[0] * differences[2]  # differences 1 and 3


def part2():
    """
    (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4, 5, 6, 7, 10,     12, 15, 16, 19, (22)
    (0), 1, 4, 5,    7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4, 5,    7, 10,     12, 15, 16, 19, (22)
    (0), 1, 4,    6, 7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4,    6, 7, 10,     12, 15, 16, 19, (22)
    (0), 1, 4,       7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4,       7, 10,     12, 15, 16, 19, (22)
    ------------------------------------------------
    1           +1 +2          +4                   = 8
    Ways to adapter X are the sum of adapters with X-1, X-2 and X-3 jolts (if they exist)
    For adapter 0 (outlet) it is one way, same as adapters 1, 4, and 5.

    """
    adapters = [0] + get_all_adapters()
    ways = defaultdict(int)  # like array, but does not throw IndexError, just creates the index

    for adapter in adapters:
        if adapter == 0:
            c = 1
        else:
            c = sum(ways[adapter - x] for x in (1, 2, 3) if adapter - x in ways)
        ways[adapter] = c
    return ways[adapters[-1]]
