# Task: https://adventofcode.com/2021/day/X
from collections import defaultdict

f = open('y2020/data/day10.txt', 'r')
lines = f.readlines()
f.close()


def get_all_adapters():
    adapters = list(map(int, lines))
    adapters += [0] # socket
    adapters += [adapters[-1] + 3] #
    adapters.sort()
    return adapters


def part1():
    diffs = [0, 0, 0]  # differences for 1, 2, 3 jolts
    adapters = get_all_adapters()
    last_adapter = adapters.pop()  # starting socket = 0
    for adapter in adapters:
        difference = adapter - last_adapter
        diffs[(difference - 1) % 3] += 1
        last_adapter = adapter
    return diffs[0] * diffs[2]  # differences 1 and 3


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
    adapters = get_all_adapters()
    ways = defaultdict(int)  # like array, but does not throw IndexError, just creates the index

    for adapter in adapters:
        if adapter == 0:
            sum_of_previous_ways = 1
        else:
            sum_of_previous_ways = sum(
                ways[adapter - x] for x in [1, 2, 3] if (adapter - x) in ways
            )
        ways[adapter] = sum_of_previous_ways
    return ways[adapters[-1]]
