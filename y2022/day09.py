# Task: https://adventofcode.com/2022/day/9
f = open('y2022/data/day09.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def print_grid(positions):
    padding = 2
    min_y = min([pos[0] for pos in positions])
    max_y = max([pos[0] for pos in positions])
    max_x = max([pos[1] for pos in positions])
    min_x = min([pos[1] for pos in positions])
    grid = []
    for row in range(max_y + padding, min_y - padding, -1):
        r = []
        for cell in range(min_x - padding, max_x + padding):
            if [row, cell] in positions:
                r.append("#")
            else:
                r.append(".")
        grid.append(r)
    for row in grid:
        print("".join(row))


def get_new_knot_position(head, tail):
    diff_x = abs(head[1] - tail[1])
    diff_y = abs(head[0] - tail[0])

    if diff_x:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    if diff_y:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1

    return tail


def get_new_head_position(direction, head):
    if direction == "U":
        head[0] += 1
    elif direction == "D":
        head[0] -= 1
    elif direction == "R":
        head[1] += 1
    elif direction == "L":
        head[1] -= 1
    return head


def count_tail_positions(rope_length):
    rope = [[0, 0] for _ in range(rope_length)]
    tail_visited = []
    for line in lines:
        direction, count = line.split(" ")
        for i in range(int(count)):
            # head
            rope[0] = get_new_head_position(direction, rope[0])

            # other knots
            for knot in range(1, len(rope)):

                # do I need to move the knot or not
                moving_knot = abs(rope[knot - 1][0] - rope[knot][0]) > 1 \
                              or abs(rope[knot - 1][1] - rope[knot][1]) > 1
                if moving_knot:
                    rope[knot] = get_new_knot_position(rope[knot - 1], rope[knot])

            if rope[rope_length - 1] not in tail_visited:
                tail_visited.append([rope[rope_length - 1][0], rope[rope_length - 1][1]])

    # print_grid(tail_visited)
    return len(tail_visited)


def part1():
    return count_tail_positions(2)


def part2():
    return count_tail_positions(10)
