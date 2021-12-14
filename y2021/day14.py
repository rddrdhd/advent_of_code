# Task: https://adventofcode.com/2021/day/14
from collections import defaultdict

f = open('y2021/data/day14.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]


def get_data():
    template, _ = lines[:2]
    insertion_rules = lines[2:]
    rules = {}
    for line in insertion_rules:
        key, value = line.strip().split(" -> ")
        rules[key] = value
    return template, rules


def make_steps(steps, rules, template):
    pairs_counter = defaultdict(int)
    for i in range(1, len(template)):
        pairs_counter[str(template[i - 1]) + str(template[i])] += 1

    # get pairs in final string
    for _ in range(steps):
        new_pairs = defaultdict(int)
        for pair in pairs_counter:
            for i in rules[pair]:
                new_pairs[pair[0] + i] += pairs_counter[pair]
                new_pairs[i + pair[1]] += pairs_counter[pair]
        pairs_counter = new_pairs

    # get result
    char_counter = defaultdict(int)
    for p in pairs_counter:
        for char in list(p):
            char_count = 0
            for pair, count in pairs_counter.items():
                if char == pair[0]:
                    char_count += count
            char_counter[char] = char_count

    # last char
    char_counter[template[-1]] += 1

    # return
    max_key = max(char_counter, key=char_counter.get)
    min_key = min(char_counter, key=char_counter.get)
    return char_counter[max_key] - char_counter[min_key]


def part1(steps=10):
    template, rules = get_data()
    return make_steps(steps, rules, template)  # 2899


def part2(steps=40):
    template, rules = get_data()
    return make_steps(steps, rules, template)  # 3528317079545
