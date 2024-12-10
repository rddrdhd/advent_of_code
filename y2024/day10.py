#Task: https://adventofcode.com/2024/day/10
f = open('y2024/data/day10.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
DIRECTIONS = [N, E, S, W] # ^>v<
WIDTH = len(lines[0])
HEIGHT = len(lines)


def is_in_bounds(y, x):
    return 0 <= y < HEIGHT and 0 <= x < WIDTH


def get_trailhead_coords():
    trailheads = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '0':
                trailheads.append((y,x))
    return trailheads


def get_trail_ends_count(y, x):
    current_trail = set()
    to_visit = [(y, x)] 
    count = 0  
    
    while to_visit:
        y, x = to_visit.pop()
        
        if (y, x) in current_trail:
            continue
        current_trail.add((y, x))
        current_lvl = int(lines[y][x])
        
        for dy, dx in DIRECTIONS:
            ny, nx = y + dy, x + dx # neighbour
            
            if is_in_bounds(ny, nx) and (ny, nx) not in current_trail:
                try:
                    next_lvl = int(lines[ny][nx])
                    if next_lvl == current_lvl + 1:
                        if next_lvl == 9:
                            count += 1
                        to_visit.append((ny, nx))
                except ValueError: 
                    pass # dots in test inputs
    return count


def get_trail_paths_count(y, x, current_trail):
    current_lvl = int(lines[y][x])
    current_trail.add((y, x))  
    trails_count = 0 
    
    for dy, dx in DIRECTIONS:
        ny, nx = y + dy, x + dx # neighbour
        
        if is_in_bounds(ny, nx) and (ny, nx) not in current_trail:
            try:
                next_lvl = int(lines[ny][nx])
                if next_lvl == current_lvl + 1:  
                    if next_lvl == 9:
                        trails_count += 1 
                    else:
                        trails_count += get_trail_paths_count(ny, nx, current_trail)
            except ValueError:
                pass # dots in test inputs
    current_trail.remove((y, x))  
    return trails_count


def get_result(second_part):
    trailheads = get_trailhead_coords()
    total_score = 0
    
    for (y, x) in trailheads:
        if not second_part:
            total_score += get_trail_ends_count(y, x)
        else:
            current_trail = set()
            total_score += get_trail_paths_count(y, x, current_trail)
    
    return total_score


def part1():
    return get_result(second_part=False)


def part2():
    return get_result(second_part=True)


if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())