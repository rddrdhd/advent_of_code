#Task: https://adventofcode.com/2023/day/3
import re
f = open('y2023/data/day03.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]
height = len(lines)
width = len(lines[0])


def part1():
    sum = 0
    y = 0
    # for each row
    for y in range(0,height):
        row = lines[y]

        # for each number
        for match in re.finditer('[0-9]+',row):
            has_neighbours = False
            span = match.span()

            # 8 neighbouring coordinates
            neighbours_coords=[ [y+0,span[0]-1], [y+0,span[1]] ]
            for i in range(span[0]-1, span[1]+1):
                neighbours_coords.append([y+1,i])
                neighbours_coords.append([y-1,i])

            # for each neighbour coords check if there is something
            for n in neighbours_coords:
                if 0<=n[0]<width and 0<=n[1]<height: 
                    if lines[n[0]][n[1]] != ".":
                        has_neighbours = True 
            if has_neighbours:
                sum += int(match.group())
    return sum # 560670

def part2():
    sum = 0
    y = 0
    # for each row
    for y in range(0,height):

        # for each star
        for match in re.finditer('\*',lines[y]):
            neighbours = []
            x = match.start()

            # for each neighbour row
            nums_in_row = [re.finditer('\d+',lines[y-1]),
                       re.finditer('\d+',lines[y]),
                       re.finditer('\d+',lines[y+1]),]
            for nums in nums_in_row:

                # for each number
                for num in nums:
                    is_neighbour = (num.start() in (x-1,x,x+1)) or (num.end()-1 in (x-1,x,x+1))
                    
                    # check if neighbour
                    if is_neighbour:
                        neighbours.append(int(num.group()))
            if len(neighbours) == 2:
                sum += neighbours[0]*neighbours[1]
    return sum # 91622824