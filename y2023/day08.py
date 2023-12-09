#Task: https://adventofcode.com/2023/day/8
import re
f = open('y2023/data/day08.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]


# Use the insert method to add nodes

def part1():
    steps = 0
    instructions = lines[0]
    nodes = {}
    root = 'AAA'
    finish = 'ZZZ'
    finished = False
    for line in lines[2:]:
        data, children = line.split(" = ")
        left, right = children[1:-1].split(", ")
        nodes[data] = [left, right]
    print("init done")
    curr_children = nodes[root]
    i = 0
    while True:
        steps += 1
        inst = instructions[i%len(instructions)]
        if(inst) == 'L':
            if curr_children[0] == finish:
                break
            else:
                curr_children = nodes[curr_children[0]]
        else:
            if curr_children[1] == finish:
                break
            else:
                curr_children = nodes[curr_children[1]]
        i+=1
    return steps #11911

from itertools import cycle
from math import gcd

def math_gcd_lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // gcd (a, b)
    return a

def part2():
    steps, _, *nodes = lines
    instructions = cycle(steps)

    tree = {}
    for ghost in nodes:
        data, children = ghost.split(" = ")
        left, right = children[1:-1].split(", ")
        tree[data] = [left, right]

    curr_ghosts = [node for node in tree if node.endswith("A")]
    steps = []

    for ghost in curr_ghosts:
        required_steps = 0
        curr_node = ghost

        while True:
            required_steps += 1

            if next(instructions) == "L":
                new_node = tree[curr_node][0]
            else:
                new_node = tree[curr_node][1]

            if new_node.endswith("Z"):
                break

            curr_node = new_node
        steps.append(required_steps)
    return math_gcd_lcm(*steps) # 10151663816849