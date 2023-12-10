#Task: https://adventofcode.com/2023/day/10

f = open('y2023/data/day10.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

Y = 0
X = 1

def points_up(char):
    return char in ['|','L','J', 'S']

def points_down(char):
    return char in ['|', '7', 'F', 'S']

def points_left(char):
    return char in ['-','7','J','S']

def points_right(char):
    return char in [ '-','L','F','S']


def get_start(lines):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            char = lines[y][x]
            if char == 'S':
                return [y, x]
    return None

def get_path(lines, start):
    path = []
    node = start
    first_step = True
    while True:
            if lines[node[Y]][node[X]] == 'S' and not first_step:
                break

            char = lines[node[Y]][node[X]]
            char_d = lines[node[Y]+1][node[X]] if node[Y] < (len(lines)-1) else None
            char_r = lines[node[Y]][node[X]+1] if node[X] < len(lines[0])-1 else None
            char_l = lines[node[Y]][node[X]-1]  if node[X] > 0 else None
            char_u = lines[node[Y]-1][node[X]] if  node[Y] > 0 else None
            
            pipe_d = [node[Y]+1,node[X]]
            pipe_r = [node[Y],node[X]+1]
            pipe_l = [node[Y],node[X]-1]
            pipe_u = [node[Y]-1,node[X]]
            
                
            if char_d and pipe_d not in path and points_down(char) and points_up(char_d):
                    node = pipe_d
            elif char_r and pipe_r not in path and points_right(char) and points_left(char_r):
                    node = pipe_r
            elif char_l and pipe_l not in path and points_left(char) and points_right(char_l):
                    node = pipe_l
            elif char_u and pipe_u not in path and points_up(char) and points_down(char_u):
                    node = pipe_u
            path.append(node)

            first_step = False
    return path

def replace_start(lines, start, first_step, last_step):
    arr = list(lines[start[Y]])
    if first_step[Y] > start[Y] and last_step[X] > start[X]: # fs down ls right
        arr[start[X]] = 'F'
    elif  first_step[Y] < start[Y] and last_step[X] < start[X]: # fs up a ls left
        arr[start[X]] = 'J'
    elif first_step[Y] > start[Y] and last_step[X] < start[X]: # fs down a ls left
        arr[start[X]] = '7'
    elif first_step[Y] < start[Y] and last_step[X] > start[X]: # fs up a ls right
        arr[start[X]] = 'L'
    elif first_step[Y] - last_step[Y] == 2: # up and down
        arr[start[X]] = '|'
    elif first_step[X] - last_step[X] == 2: # left and right
        arr[start[X]] = '-'
    lines[start[Y]] = "".join(arr)
    return lines
     
def part1():
    start = get_start(lines)
    path = get_path(lines, start)
    return int(len(path)/2) # 6870

def part2():
    count = 0
    start = get_start(lines)
    path = get_path(lines, start)
    grid = replace_start(lines, start,  path[0],  path[-2])
    grid_width = len(grid[0])
    grid_height = len(grid)
    inside = False

    y = 0
    while y < grid_height:
        x = 0
        while x < grid_width:
            if [y,x] in path and grid[y][x] =='|': # easy switch
               inside = not inside
            elif [y,x] in path and grid[y][x] in ['F','J','L','7']: # switching only if passing combo
                if grid[y][x] =='L':
                    while grid[y][x] not in ['7', 'J'] and x < grid_width-1: 
                        x+=1
                    if grid[y][x]=='7':     # L---7 => switch (border goes from up to down)
                        inside = not inside
                elif grid[y][x]=='F':
                    while grid[y][x] not in ['7', 'J'] and x < grid_width-1: 
                        x+=1
                    if grid[y][x]=='J':     # F---J => switch (border goes from down to up)
                        inside = not inside
            else:
                if inside:
                    count += 1
            x+=1
        y+=1

    return count # 287