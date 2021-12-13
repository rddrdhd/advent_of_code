# Task: https://adventofcode.com/2021/day/12
from collections import defaultdict

f = open('y2021/data/day12.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

graph = defaultdict(list)

for line in lines:
    node1, node2 = line.strip().split("-")
    graph[node1].append(node2)
    graph[node2].append(node1)


def get_all_paths(graph, start, end, path=[], repeats=False):
    path = path + [start]
    if start == end:
        return [path]
    paths = []

    for node in graph[start]:
        new_paths = []

        if node.isupper() or node not in path:
            new_paths += get_all_paths(graph, node, end, path, repeats)

        elif node.islower() and node in path and repeats and node not in ('start', 'end'):
            new_paths += get_all_paths(graph, node, end, path, False)

        for new_path in new_paths:
            paths.append(new_path)

    return paths


def part1():
    paths = get_all_paths(graph, "start", "end", repeats=False)
    return len(paths)  # 4241


def part2():
    paths = get_all_paths(graph, "start", "end", repeats=True)
    return len(paths)  # 122134
