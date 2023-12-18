#Task: https://adventofcode.com/2023/day/18
# https://en.wikipedia.org/wiki/Shoelace_formula

f = open('y2023/data/day18.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

X = 1
Y = 0

RIGHT = 'R'
DOWN = 'D'
LEFT = 'L'
UP = 'U'

NEIGHTBOURS = {RIGHT:(0,1), DOWN:(1, 0), LEFT:(0,-1), UP:(-1, 0)}

def get_full_area(border, corners):
    crosses = 0
    for i in range(len(corners)):
        curr_x= corners[i][X]
        prev_y = corners[i - 1][Y]
        next_y = corners[(i + 1) % len(corners)][Y]
        crosses += curr_x * (prev_y - next_y)
    shoelace = abs(crosses) / 2
    area = shoelace - border / 2 
    return int(area + border + 1) 

def get_border_and_corners(lines, second_part=False):
    corners = [(0,0)]
    border = 0
    for line in lines:
        direction, count, hex= line.split()
        hex = hex[2:-1]
        if not second_part:
            dy, dx = NEIGHTBOURS[direction]
            count = int(count)
        else:
            direction = [RIGHT,DOWN,LEFT,UP][int(hex[-1])]
            dy, dx = NEIGHTBOURS[direction]
            count = int(hex[:-1], 16)
        border += count
        y,x = corners[-1]
        corners.append((y+ dy*count, x+dx*count))
    return border, corners

def part1():
    border, corners = get_border_and_corners(lines, second_part=False)
    return get_full_area(border, corners) # 36679
    
def part2():
    border, corners = get_border_and_corners(lines, second_part=True)
    return get_full_area(border, corners) # 88007104020978