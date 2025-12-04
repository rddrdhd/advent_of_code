#Task: https://adventofcode.com/2025/day/4
f = open('y2025/data/day04.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

directions = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

def get_coords_to_remove(coords):
    original_coords = set(coords.keys())
    for (x, y) in coords:
        count = 0
        for dx, dy in directions:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if (nx, ny) in original_coords:  
                count += 1
        coords[(x, y)] = count
    return [key for key, val in coords.items() if val < 4]


def part1():
    coords = {}
    for x, line in enumerate(lines):
        for y, content in enumerate(line):
            if content == "@":
                coords[(x, y)] = 0  

    return len(get_coords_to_remove(coords))


def part2():
    count = 0
    coords = {}
    for x, line in enumerate(lines):
        for y, content in enumerate(line):
            if content == "@":
                coords[(x, y)] = 0
    
    while True:
        coords_to_remove = get_coords_to_remove(coords)
        if not coords_to_remove:
            break
        for key in coords_to_remove:
            count += 1
            del coords[key]
    
    return count

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())