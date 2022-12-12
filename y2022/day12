#Task: https://adventofcode.com/2022/day/12
f = open('y2022/data/day12.txt', 'r')
lines = f.readlines()
f.close()
lines = [l.strip() for l in lines]


def print_grid(nodes):
    for row in nodes:
        print("".join(row))


def get_nodes():
    nodes = []
    for y in range(len(lines)):
        row = []
        for x in range(len(lines[y])):
            row.append(lines[y][x])
        nodes.append(row)
    return nodes


def get_shortest_path(from_chars):
    nodes = get_nodes()
    queue = []
    neighbours = [[-1, 0], [+1, 0], [0, -1], [0, +1]]
    for y in range(len(nodes)):
        for x in range(len(nodes[0])):
            if nodes[y][x] in from_chars:
                starting_node = [y, x, "a", 0]  # y, x coords, value, path length from start
                queue.append(starting_node)
                nodes[y][x] = "-"
    p = 0
    while len(queue):
        node = queue.pop(0)
        y, x, v, p = node  # y, x coords, value, and path length from start

        for direction in neighbours:  # for each direction (just up/down/left/right)
            newy = y + direction[0]
            newx = x + direction[1]
            # if not over the edge
            if 0 <= newy < len(nodes) and 0 <= newx < len(nodes[0]):
                neighbour = nodes[newy][newx]
                if neighbour in "abcdefghijklmnopqrstuvwxyz":  # if not visited yet
                    if ord(neighbour) - ord(v) <= 1:
                        queue.append([newy, newx, nodes[newy][newx], p + 1])  # add to end of the queue
                        nodes[newy][newx] = "-"  # make it visited
                elif neighbour == "E" and (v == "y" or v == "z"):  # PROFIT
                    return p + 1
    return 0  # Something went wrong


def part1():
    return get_shortest_path(["S"])


def part2():
    return get_shortest_path(["a", "S"])
