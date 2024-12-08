#Task: https://adventofcode.com/2024/day/5
f = open('y2024/data/day05.txt', 'r')
lines = f.readlines()
f.close()
from collections import defaultdict, deque

lines = [s.strip() for s in lines]


def parse_input():
    rules = []
    updates = []
    parsing_rules = True

    for line in lines:
        if not line:
            parsing_rules = False
            continue

        if parsing_rules:
            nums = tuple(map(int, line.split("|")))
            rules.append(nums)
        else:
            nums = list(map(int, line.split(",")))
            updates.append(nums)

    return updates, rules


def apply_rules(update, rules):
    needs_check = True
    while needs_check:
        needs_check = False
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                a = update.index(rule[0])
                b = update.index(rule[1])
                if a > b:  # Rule violated, swap
                    update[a], update[b] = update[b], update[a]
                    needs_check = True
    return update


def get_passing_middle_pages_sum(second_part=False):
    sum = 0
    updates, rules = parse_input()
        
    for i, update in enumerate(updates):
        update_passing = True
        for j, rule in enumerate(rules):
            try:
                a = update.index(rule[0])
                b = update.index(rule[1])
                if a >= b:  
                    update_passing = False
            except:
                pass
        
        if update_passing and not second_part:
            center = (len(update) - 1)//2
            middle_page_num = update[int(center)]
            sum += middle_page_num
        elif not update_passing and second_part:
            new_order = apply_rules(update, rules)
            center = (len(new_order) - 1)//2
            middle_page_num = new_order[int(center)]
            sum += middle_page_num
    return sum


def part1():
    return get_passing_middle_pages_sum(second_part=False)


def part2():
    return get_passing_middle_pages_sum(second_part=True)


if __name__ == "__main__":
    print()
    print("P1",part1()) # 4662
    print("P2",part2()) # 5900