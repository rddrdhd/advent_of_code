#Task: https://adventofcode.com/2023/day/11
import itertools

f = open('y2023/data/day11.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

Y = 0
X = 1
START = 0
END = 1

def get_empty(lines):
    width = len(lines[0])
    height = len(lines)
    empty_rows = []
    empty_columns = []
    
    for x in range(width):
        empty = True
        for y in range(height):
            if lines[y][x] == '#':
                empty = False
        if empty:
            empty_columns.append(x)
    
    for y in reversed(range(height)):
        if '#' not in lines[y]:
            empty_rows.append(y)

    return empty_rows, empty_columns

def get_paths(lines):
    galaxies = []
    combo_paths = {}
    width = len(lines[0])
    height = len(lines)

    # get galaxies
    for y in range(height):
        for x in range(width):
            if lines[y][x]=='#':
                galaxies.append([y, x])
    
    # make combinations
    combinations = list(itertools.combinations(galaxies, 2))
    
    # get path length from the original input
    for i,combo in enumerate(combinations):
        path = abs(combo[START][Y]-combo[END][Y])+abs(combo[START][X]-combo[END][X])
        combo_paths[i] = [combo[START], combo[END], path] 
    return combo_paths

def get_sums_in_old_universe(age):
    times_older = age-1
    sum = 0
    
    empty_rows, empty_columns = get_empty(lines)
    combo_paths = get_paths(lines)

    # EXPANSE THE UNIVERSE
    for key, combo in combo_paths.items():
        x_range = range(*list(sorted([combo[0][X],combo[1][X]]))) 
        y_range = range(*list(sorted([combo[0][Y],combo[1][Y]])))
        
        for x in x_range:
            if x in empty_columns:
                combo_paths[key][2] += times_older
        for y in y_range:
            if y in empty_rows:
                combo_paths[key][2] += times_older

    for item in combo_paths.values():
        sum+=item[2]
    return sum 

def part2():
    return get_sums_in_old_universe(1000000) # 685038186836

def part1():
    return get_sums_in_old_universe(2) # 9556896

