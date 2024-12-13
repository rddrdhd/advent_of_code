#Task: https://adventofcode.com/2024/day/12
from collections import defaultdict
f = open('y2024/data/day12.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)

DIRECTIONS = [N, E, S, W] # ^>v<
WIDTH=len(lines[0])
HEIGHT=len(lines)

AREA, PERIMETER = 0, 1

def in_bounds(y, x):
    return 0 <= y < HEIGHT and 0 <= x < WIDTH

def get_area(y, x, char, visited):
    area = 0
    visited.add((y, x))
    stack = [(y, x)]

    while stack:
        cy, cx = stack.pop()
        area += 1
        for dy, dx in DIRECTIONS:
            ny, nx = cy + dy, cx + dx
            if in_bounds(ny, nx) and (ny, nx) not in visited and lines[ny][nx] == char:
                visited.add((ny, nx))
                stack.append((ny, nx))

    return area

def get_perimeter(y,x,char):
    perimeter = 0
    visited = set()
    stack = [(y, x)]
    
    while stack:
        cy, cx = stack.pop()
        if (cy, cx) in visited:
            continue
        visited.add((cy, cx))

        for dy, dx in DIRECTIONS:
            ny, nx = cy + dy, cx + dx
            if in_bounds(ny, nx):
                if lines[ny][nx] == char:
                    if (ny, nx) not in visited:
                        stack.append((ny, nx))
                else:
                    perimeter += 1  # fence between areax
            else:
                perimeter += 1  # fence around input

    return perimeter


def get_corners(y, x, char):
    corners = 0
    visited = set()
    stack = [(y, x)]
    cells = set()

    while stack:
        cy, cx = stack.pop()
        if (cy, cx) in visited:
            continue
        visited.add((cy, cx))
        cells.add((cy, cx))

        for dy, dx in [N, S, W, E]:
            ny, nx = cy + dy, cx + dx
            if in_bounds(ny, nx) and (ny, nx) not in visited and lines[ny][nx] == char:
                stack.append((ny, nx))

    for cell in cells:
        for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:

            # outer corner
            if ((cell[0] + dx, cell[1]) not in cells and
                    (cell[0], cell[1] + dy) not in cells):
                corners += 1

            # inner corner
            if ((cell[0] + dx, cell[1]) in cells and
                    (cell[0], cell[1] + dy) in cells and
                    (cell[0] + dx, cell[1] + dy) not in cells):
                corners += 1

    return corners

    
def part1():
    sum = 0
    visited = set()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (y,x)not in visited:
                area = get_area(y, x, char, visited)
                perimeter = get_perimeter(y,x,char)
                #print(char, area, perimeter, area*perimeter)
                visited.add((y,x))
                sum += area * perimeter
    return sum

def part2():
    sum = 0
    visited = set()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (y,x)not in visited:
                area = get_area(y, x, char, visited)
                sides = get_corners(y, x, char)
                #print(char, area, sides, area*sides)
                visited.add((y,x))
                sum += area * sides
    return sum


if __name__ == "__main__":
    print()
    print("P1",part1()) # 1402544
    print("P2",part2()) # 862486