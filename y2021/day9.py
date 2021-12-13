# Task: https://adventofcode.com/2021/day/X
from typing import List

f = open('y2021/data/day9.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]


def part1():
    line_length = len(lines[0])
    height = len(lines)
    risk_levels = []
    for y in range(height):
        for x in range(line_length):
            is_local_min = True
            if x != 0 and lines[y][x - 1] <= lines[y][x]:
                is_local_min = False
            if y != 0 and lines[y - 1][x] <= lines[y][x]:
                is_local_min = False
            if x != line_length - 1 and lines[y][x + 1] <= lines[y][x]:
                is_local_min = False
            if y != height - 1 and lines[y + 1][x] <= lines[y][x]:
                is_local_min = False
            if is_local_min:
                risk_levels.append(int(lines[y][x]) + 1)
    return sum(risk_levels)  # 465


def part2():
    line_length = len(lines[0])
    height = len(lines)
    local_mins = []

    # get local mins
    for y in range(height):
        for x in range(line_length):
            is_local_min = True
            if x != 0 and lines[y][x - 1] <= lines[y][x]:
                is_local_min = False
            if y != 0 and lines[y - 1][x] <= lines[y][x]:
                is_local_min = False
            if x != line_length - 1 and lines[y][x + 1] <= lines[y][x]:
                is_local_min = False
            if y != height - 1 and lines[y + 1][x] <= lines[y][x]:
                is_local_min = False
            if is_local_min:
                local_mins.append([int(lines[y][x]), y, x])  # [0] for value, [1] for y, [2] for x

    basin_sizes = []

    # compute basin sizes around local minimums
    for local_min in local_mins:
        value = int(local_min[0])
        y = local_min[1]
        x = local_min[2]
        todo = []
        done = []
        size = 1

        # add fist "good neighbours" to to-do list (consider this as the "do" part in "do while")
        if x > 0 and 9 > int(lines[y][x - 1]) > value:  # left
            todo.append([lines[y][x - 1], y, x - 1])
        if y > 0 and y != 0 and 9 > int(lines[y - 1][x]) > value:  # up
            todo.append([lines[y - 1][x], y - 1, x])
        if x + 1 < len(lines[0]) - 1 and 9 > int(lines[y][x + 1]) > value:  # right
            todo.append([lines[y][x + 1], y, x + 1])
        if y + 1 < len(lines) and 9 > int(lines[y + 1][x]) > value:  # bottom
            todo.append([lines[y + 1][x], y + 1, x])

        while todo:
            item = todo.pop()

            value = int(item[0])
            y = item[1]
            x = item[2]
            if item not in done:
                size += 1
                if x != 0 and 9 > int(lines[y][x - 1]) > value:
                    todo.append([lines[y][x - 1], y, x - 1])
                if y != 0 and 9 > int(lines[y - 1][x]) > value:
                    todo.append([lines[y - 1][x], y - 1, x])
                if (x + 1 < len(lines[0])) and 9 > int(lines[y][x + 1]) > value:
                    todo.append([lines[y][x + 1], y, x + 1])
                if (y + 1 < len(lines)) and 9 > int(lines[y + 1][x]) > value:
                    todo.append([lines[y + 1][x], y + 1, x])
                done.append(item)
        basin_sizes.append(size)
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]  # 1269555


