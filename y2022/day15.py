import re

f = open('y2022/data/day15.txt', 'r')
lines = f.readlines()
f.close()
lines = [l.strip() for l in lines]


def count_empty_places(lines, main_y=10):
    known = set()
    intervals = []

    for line in lines:
        sx, sy, bx, by = [int(j) for j in re.findall(r'\d+', line)]
        distance = abs(sx - bx) + abs(sy - by)
        reach = distance - abs(sy - main_y)

        if reach < 0:
            continue

        left_x = sx - reach
        right_x = sx + reach

        intervals.append((left_x, right_x))

        if by == main_y:
            known.add(bx)

    intervals.sort()

    q = []

    for left_x, right_x in intervals:
        if not q:
            q.append([left_x, right_x])
            continue

        left_q, right_q = q[-1]

        if left_x > right_q + 1:
            q.append([left_x, right_x])
            continue

        q[-1][1] = max(right_q, right_x)

    empty = set()

    for left_x, right_x in q:
        for x in range(left_x, right_x + 1):
            empty.add(x)

    return len(empty - known)


def part1():
    return count_empty_places(lines, 2000000)


def part2():
    return 0
