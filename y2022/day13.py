# Task: https://adventofcode.com/2022/day/13

lines = open('y2022/data/day13.txt').read()
lines = [line for line in lines.split("\n\n")]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            c = compare(left[i], right[i])
            if c == -1:
                return -1
            elif c == 1:
                return 1
            i += 1
        if i == len(left) and i < len(right):
            return -1
        elif i < len(left) and i == len(right):
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        return compare(left, [right])


def part1():
    result = 0
    for i, group in enumerate(lines):
        left, right = group.split("\n")
        left = eval(left)
        right = eval(right)
        if (compare(left, right)) == -1:
            result += 1 + i
    return result


def part2():
    result = 1
    packets = []
    for i, group in enumerate(lines):
        left, right = group.split("\n")
        left = eval(left)
        right = eval(right)
        packets.append(left)
        packets.append(right)
    packets.append([[2]])
    packets.append([[6]])

    from functools import cmp_to_key
    packets.sort(key=cmp_to_key(compare))

    for i, packet in enumerate(packets):
        if packet == [[2]] or packet == [[6]]:
            result *= i + 1
    return result
