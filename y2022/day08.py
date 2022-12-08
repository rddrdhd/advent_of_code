# Task: https://adventofcode.com/2022/day/8
f = open('y2022/data/day08.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]
forest_height = len(lines)
forest_length = len(lines[0])


def get_forest():
    forest = []
    for y, line in enumerate(lines):
        for x, tree_height in enumerate(line):
            if y in [0, forest_height - 1] or x in [0, forest_length - 1]:
                tree_height = {"height": int(tree_height), "coord_y": y, "coord_x": x}
                forest.append(tree_height)
            else:
                forest.append({"height": int(tree_height), "coord_y": y, "coord_x": x})
    return forest


def get_blocking_tree(direction, forest, the_tree):
    x = the_tree["coord_x"]
    y = the_tree["coord_y"]
    try:
        if direction == "d":
            path = [d for d in forest if d["coord_x"] == x and d["coord_y"] > y]
            for p in range(len(path)):
                if path[p]["height"] >= the_tree["height"]:
                    return path[p]
        if direction == "u":
            path = [d for d in forest if d["coord_x"] == x and d["coord_y"] < y]
            for p in range(len(path) - 1, -1, -1):
                if path[p]["height"] >= the_tree["height"]:
                    return path[p]
        if direction == "r":
            path = [d for d in forest if d["coord_x"] > x and d["coord_y"] == y]
            for p in range(len(path)):
                if path[p]["height"] >= the_tree["height"]:
                    return path[p]
        if direction == "l":
            path = [d for d in forest if d["coord_x"] < x and d["coord_y"] == y]
            for p in range(len(path) - 1, -1, -1):
                if path[p]["height"] >= the_tree["height"]:
                    return path[p]
    except ValueError:  # border == no path
        return None


def how_far_can_see(direction, from_tree, blocking_tree):
    try:
        if blocking_tree["height"] >= from_tree["height"]:
            if direction == "l" or direction == "r":
                return [abs(blocking_tree["coord_x"] - from_tree["coord_x"]), False]
            else:  # direction == "u" or direction == "d":
                return [abs(blocking_tree["coord_y"] - from_tree["coord_y"]), False]

    except TypeError:  # can see to the border
        if direction == "l":
            return [from_tree["coord_x"], True]
        elif direction == "r":
            return [forest_length - from_tree["coord_x"] - 1, True]
        elif direction == "u":
            return [from_tree["coord_y"], True]
        else:  # direction == "d"
            return [forest_height - from_tree["coord_y"] - 1, True]


def part1():
    forest = get_forest()
    score = 0
    for tree in forest:
        visible = False
        for direction in ["u", "d", "r", "l"]:
            blocking_tree = get_blocking_tree(direction, forest, tree)
            if blocking_tree:
                if blocking_tree["height"] < tree["height"]:
                    visible = True
            else:
                visible = True

        if visible:
            score += 1
    return score  # 1816


def part2():
    forest = get_forest()
    max_score = 0
    for tree in forest:
        new_score = 1
        for direction in ["u", "d", "r", "l"]:
            blocking_tree = get_blocking_tree(direction, forest, tree)
            new_score *= how_far_can_see(direction, tree, blocking_tree)[0]
        if new_score > max_score:
            max_score = new_score
    return max_score  # 383520
