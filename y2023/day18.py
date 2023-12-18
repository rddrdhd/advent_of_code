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

def part1():
    corners = [(0,0)]
    border = 0
    for line in lines:
        direction, count, _= line.split(" ")
        dy, dx = NEIGHTBOURS[direction]
        count = int(count)
        border += count
        y,x = corners[-1]
        corners.append((y + dy * count, x + dx * count))

    crosses = 0

    for i in range(len(corners)):
        curr_x= corners[i][X]
        prev_y = corners[i - 1][Y]
        next_y = corners[(i + 1) % len(corners)][Y]
        
        crosses += curr_x * (prev_y - next_y)

    shoelace = abs(crosses) / 2
    area = shoelace - border / 2 

    return int(area + border + 1) # 36679
    
def part2():
    corners = [(0,0)]
    border = 0
    for line in lines:
        hex = line.split(" ")[-1][2:-1]
        dir_index = int(hex[-1])
        direction = [RIGHT,DOWN,LEFT,UP][dir_index]
        dy, dx = NEIGHTBOURS[direction]
        count_hex = hex[:-1]
        count = int(count_hex, 16)
        border += count
        y, x = corners[-1]
        corners.append((y + dy * count, x + dx * count))

    crosses = 0

    for i in range(len(corners)):
        curr_x= corners[i][X]
        prev_y = corners[i - 1][Y]
        next_y = corners[(i + 1) % len(corners)][Y]
        
        crosses += curr_x * (prev_y - next_y)

    shoelace = abs(crosses) / 2
    area = shoelace - border / 2 

    return int(area + border + 1) # 88007104020978