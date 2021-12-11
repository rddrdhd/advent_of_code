# Task: https://adventofcode.com/2021/day/X
f = open('y2021/data/day11.txt', 'r')
lines = f.readlines()
lines = [s.strip() for s in lines]
lines = [list(map(int, s)) for s in lines]
f.close()

neighbour_coords = [{'y':-1, 'x': -1}, {'y':-1, 'x': 0}, {'y':-1, 'x': 1},
                    {'y': 0, 'x': -1}, {'y': 0, 'x': 1},
                    {'y': 1, 'x': -1}, {'y': 1, 'x': 0}, {'y': 1, 'x': 1}]

def get_valid_neighbours(x, y, max_x, max_y):
    neighbours = []
    if y != 0:  # upper row
        if x != 0:
            neighbours.append(neighbour_coords[0])
        neighbours.append(neighbour_coords[1])
        if x != max_x - 1:
            neighbours.append(neighbour_coords[2])
    if x != 0:  # left cell
        neighbours.append(neighbour_coords[3])
    if x != max_x - 1:  # right cell
        neighbours.append(neighbour_coords[4])
    if y != max_y - 1:  # bottom row
        if x != 0:
            neighbours.append(neighbour_coords[5])
        neighbours.append(neighbour_coords[6])
        if x != max_x - 1:
            neighbours.append(neighbour_coords[7])
    return neighbours


def flash_flood(flashes, y, x):
    neighbours = get_valid_neighbours(x, y, len(flashes), len(flashes[0]))
    flash_count = 0
    for n in neighbours:
        n_x = x + n['x']
        n_y = y + n['y']
        energy_level = int(flashes[n_y][n_x])
        if flashes[n_y][n_x] != 0:
            flashes[n_y][n_x] = energy_level + 1
            if flashes[n_y][n_x] > 9:
                flash_count += 1
                flashes[n_y][n_x] = 0
                flashes, fflash_count = flash_flood(flashes, n_y, n_x)
                flash_count += fflash_count
    return flashes, flash_count


def part1(steps=100):
    flash_count = 0
    for step in range(steps):
        flashes = []
        # find first flashes in this step
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                energy_level = int(lines[y][x])
                lines[y][x] = energy_level + 1
                if int(lines[y][x]) > 9:
                    lines[y][x] = 0
                    flashes.append({'y': y, 'x': x})
        llines = lines.copy()

        while len(flashes):
            flash_count += 1
            flash = flashes.pop()
            llines, fflash_count = flash_flood(lines, flash['y'], flash['x'])
            flash_count += fflash_count
        # print("\n----------------------------\nAfter step:", step+1)
        # for l in llines:
        #     print(l)
    return flash_count


def part2():
    f = open('y2021/data/day11.txt', 'r')
    lines = f.readlines()
    lines = [s.strip() for s in lines]
    lines = [list(map(int, s)) for s in lines]
    f.close()
    step_count = 0
    synced = False
    while not synced:
        step_count += 1
        flashes = []
        # find first flashes in this step
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                energy_level = int(lines[y][x])
                lines[y][x] = energy_level + 1
                if int(lines[y][x]) > 9:
                    lines[y][x] = 0
                    flashes.append({'y': y, 'x': x})

        while len(flashes):
            flash = flashes.pop()
            llines, _ = flash_flood(lines, flash['y'], flash['x'])
            synced = True
            for y in range(len(llines)):
                for x in range(len(llines[0])):
                    if llines[y][x] != 0:
                        synced = False

    return step_count # 329
