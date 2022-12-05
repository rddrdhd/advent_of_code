# Task: https://adventofcode.com/2022/day/5
import re

f = open('y2022/data/day05.txt', 'r')
lines = f.readlines()
f.close()


def get_stacks_and_moves():
    divider = lines.index("\n")
    number_of_stacks = int(max(lines[divider - 1]))
    init_stack_rows = [s[:-1] for s in lines[:divider - 1]]  # trim the \n
    init_stack_rows = [s.ljust(number_of_stacks * 4 + 1) for s in init_stack_rows]
    highest_stack_len = int(len(init_stack_rows))
    stacks = [[] for _ in range(number_of_stacks)]
    moves = [s.strip() for s in lines[divider + 1:]]  # empty line

    for s in range(len(stacks)):
        stack = []
        for i in range(highest_stack_len - 1, -1, -1):
            stack.append(init_stack_rows[i][s * 4 + 1])
        while " " in stack:
            stack.remove(" ")
        stacks[s] = stack

    return [stacks, moves]


def part1():
    stacks, moves = get_stacks_and_moves()
    for move in moves:
        count, stack_from, stack_to = re.findall(r'\d+', move)
        for i in range(int(count)):
            stacks[int(stack_to) - 1].append(stacks[int(stack_from) - 1].pop())
    result = "".join([s[-1] for s in stacks])
    return result  # HBTMTBSDC


def part2():
    stacks, moves = get_stacks_and_moves()
    for move in moves:
        count, stack_from, stack_to = re.findall(r'\d+', move)
        tmp_stack = []
        for i in range(int(count)):
            tmp_stack.append(stacks[int(stack_from) - 1].pop())
        for i in range(int(count)):
            stacks[int(stack_to) - 1].append(tmp_stack.pop())
    result = "".join([s[-1] for s in stacks])
    return result  #  PQTJRSHWS
