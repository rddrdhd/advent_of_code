#Task: https://adventofcode.com/2023/day/13
f = open('y2023/data/day13.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

def find_mirror(grid):
    for col in range(1, len(grid)):
        left_part = grid[col:]
        right_part_mirrored = grid[:col][::-1]
        
        left_reflection = left_part[:len(right_part_mirrored)]
        right_reflection = right_part_mirrored[:len(left_part)]
        
        if left_reflection == right_reflection:
            return col
        
    return 0 # the other direction


def find_smudged_mirror(grid):
    for col in range(1, len(grid)):
        left_part = grid[col:]
        right_part = grid[:col][::-1]
        
        smudges_count = 0

        for mirror_l, mirror_r in zip(left_part, right_part):
            for l, r in zip(mirror_l,mirror_r):
                if l != r:
                    smudges_count += 1

        if smudges_count == 1:
            return col 
        
    return 0 # the other direction

def part1():
    sum = 0
    pattern = []
    for line in lines:
        if line == "":
                mirror_row = find_mirror(list(pattern))
                if mirror_row:
                    sum += mirror_row * 100
                else:
                    # transpose
                    mirror_col = find_mirror(list(zip(*pattern)))
                    sum += mirror_col
                pattern = []
        else:
            pattern.append(line)
    return sum # 32723

def part2():
    sum = 0
    pattern = []
    for line in lines:
        if line == "":
                mirror_row = find_smudged_mirror(pattern)
                if mirror_row:
                    sum += mirror_row * 100
                else:
                    # transpose
                    mirror_col = find_smudged_mirror(list(zip(*pattern)))
                    sum += mirror_col
                pattern = []
        else:
            pattern.append(line)
    return sum # 34536