# Task: https://adventofcode.com/2021/day/X
from collections import Counter

f = open('y2021/data/test.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

def make_steps(steps, rules, template):
    done = []
    todo = [x for x in template]
    for step in range(steps):
        while len(todo) - 1:
            first = todo.pop(0)
            second = todo[0]
            if len(done) == 0:
                done.append(first)

            if str(first + second) in rules:
                done.append(rules[str(first + second)])
                done.append(second)

        if step+1 == steps:
            return done
        todo = done.copy()
        done = []

def part1(steps=10):
    template, _ = lines[:2]
    insertion_rules = lines[2:]
    rules = {}
    for line in insertion_rules:
        key, value = line.strip().split(" -> ")
        rules[key] = value

    done = make_steps(steps, rules, template)
    x = Counter(done)

    max_key = max(x, key=x.get)
    min_key = min(x, key=x.get)

    return x[max_key]-x[min_key]


def part2():
    # TODO only with counting
    return 0
