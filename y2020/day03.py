# Task: https://adventofcode.com/2020/day/3

f = open('y2020/data/day03.txt', 'r')
lines = f.readlines()
f.close()


def part1(offset_right=3, offset_down=1):
    count = 0
    x = offset_right
    y = offset_down

    while y < len(lines):
        if lines[y][x % len(lines[0].strip())] == "#":
            count += 1
        y += offset_down
        x += offset_right

    return count  # 148


def part2():
    return part1(1, 1) * part1(3, 1) * part1(5, 1) * part1(7, 1) * part1(1, 2)
