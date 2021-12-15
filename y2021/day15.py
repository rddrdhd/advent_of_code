# Task: https://adventofcode.com/2021/day/15
import sys

f = open('y2021/data/day15.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]


class Cell:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance


def get_grid(lines):
    grid = []
    for line in lines:
        grid_line = []
        for number in line:
            grid_line.append(int(number))
        grid.append(grid_line)
    return grid


def get_bigger_grid(lines, scale=5):
    small_grid = get_grid(lines)
    big_grid = []
    for big_y in range(scale * len(lines)):
        big_line = []
        for big_x in range(scale * len(lines[0])):
            original_grid_value = small_grid[big_y % len(lines)][big_x % len(lines[0])]
            adding_scale = int(big_y / len(lines)) + int(big_x / len(lines[0])) # distance from first small grid
            scaled_value = (original_grid_value + adding_scale - 1) % 9
            scaled_value += 1 # we want values 1-9, not 0-8
            big_line.append(scaled_value)

            # 8 9 1 2 3
            # 9 1 2 3 4
            # 1 2 3 4 5
            # 2 3 4 5 6
            # 3 4 5 6 7
        #     if big_y % len(lines) == 0 and big_x % len(lines[0]) == 0:
        #         print(scaled_value, end=" ")
        # if big_y % len(lines) == 0 :
        #     print()

        big_grid.append(big_line)

    print("Wait for it...", end="\r")
    return big_grid


def is_inside_grid(i, j, max_i, max_j):
    return (max_i >= i >= 0) and (max_j >= j >= 0)


# moving up, right, down and left with Dijkstra
def cheapest_path_cost(grid):
    max_y = len(grid)
    max_x = len(grid[0])
    dist = [[sys.maxsize for __ in range(max_x)] for _ in range(max_y)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    st = [Cell(0, 0, 0)]
    dist[0][0] = grid[0][0]  # at the end we substract this, bc we did not enter it
    while len(st) != 0:
        smallest = Cell(0, 0, sys.maxsize)
        for i in st:
            if i.distance < smallest.distance:
                smallest = i
        k = st.pop(st.index(smallest))
        for i in range(4):  # for each neighbour
            x = k.x + dx[i]
            y = k.y + dy[i]

            if not is_inside_grid(x, y, len(grid[0]) - 1, len(grid) - 1):
                continue  # ignore

            if dist[x][y] > dist[k.x][k.y] + grid[x][y]:
                if dist[x][y] != sys.maxsize:
                    st.pop(st.index(Cell(x, y, dist[x][y])))
                dist[x][y] = dist[k.x][k.y] + grid[x][y]
                st.append(Cell(x, y, dist[x][y]))

    return dist[max_y - 1][max_x - 1] - grid[0][0]


def part1():
    grid = get_grid(lines)
    return cheapest_path_cost(grid)  # 626


def part2():
    grid = get_bigger_grid(lines)
    return cheapest_path_cost(grid)  # 2966
