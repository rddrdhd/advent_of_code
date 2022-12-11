# Task: https://adventofcode.com/2022/day/1
f = open('y2022/data/day11.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]
raw_data = []


def get_monkeys():
    monkeys = []
    monkey = {}
    raw_data = []
    for line in lines:
        if len(line):
            if line[0] == "M":
                if len(raw_data):
                    monkey['number'] = raw_data[0]
                    monkey["starting items"] = [int(i.strip(",")) for i in raw_data[1]]
                    monkey["operation"] = [raw_data[2][0], raw_data[2][1]]
                    monkey["test"] = raw_data[3]
                    monkey["true"] = raw_data[4]
                    monkey["false"] = raw_data[5]
                    monkeys.append(monkey)
                    monkey = {}
                    raw_data = []
                raw_data.append(line.split(" ")[1][0])
            elif line[0] == "S":
                raw_data.append(line.split(" ")[2:])

            elif line[0] == "O":
                raw_data.append(line.split(" ")[4:])

            elif line[0] == "T":
                raw_data.append(line.split(" ")[-1])  # divisible by

            elif line[3] == "t":
                raw_data.append(line.split(" ")[-1])
            elif line[3] == "f":
                raw_data.append(line.split(" ")[-1])
    # Last monkey
    if len(raw_data):
        monkey['number'] = raw_data[0]
        monkey["starting items"] = [int(i.strip(",")) for i in raw_data[1]]
        monkey["operation"] = [raw_data[2][0], raw_data[2][1]]
        monkey["test"] = raw_data[3]
        monkey["true"] = raw_data[4]
        monkey["false"] = raw_data[5]
        monkeys.append(monkey)
    return monkeys


def get_items(monkeys):
    items = {i: [] for i in range(len(monkeys))}
    for monkey in monkeys:
        for item in monkey["starting items"]:
            items[int(monkey["number"])].append(int(item))
    return items


def part1():
    monkeys = get_monkeys()
    monkeys_inspected = [0 for m in range(len(monkeys))]
    items = get_items(monkeys)
    round = 0
    m = 0
    monkey_number = m % len(monkeys)
    while round < 20:
        while True:
            try:
                item = items[monkey_number].pop(0)
            except IndexError:
                monkey_number += 1
                continue
            except KeyError:
                monkey_number = 0
                round += 1
                break
            stress_level = int(item)
            if monkeys[monkey_number]["operation"][1] == "old":
                if monkeys[monkey_number]["operation"][0] == "+":
                    stress_level *= 2
                elif monkeys[monkey_number]["operation"][0] == "*":
                    stress_level *= stress_level
            else:
                if monkeys[monkey_number]["operation"][0] == "+":
                    stress_level += int(monkeys[monkey_number]["operation"][1])
                elif monkeys[monkey_number]["operation"][0] == "*":
                    stress_level *= int(monkeys[monkey_number]["operation"][1])
            stress_level = stress_level // 3
            div = int(monkeys[monkey_number]["test"])
            if not stress_level % div:
                next_monkey = int(monkeys[monkey_number]["true"])
            else:
                next_monkey = int(monkeys[monkey_number]["false"])
            monkeys_inspected[monkey_number] += 1
            m += 1
            items[next_monkey].append(stress_level)
    monkeys_inspected.sort()

    return monkeys_inspected[-1]*monkeys_inspected[-2]


def part2():
    monkeys = get_monkeys()
    round = 0
    modulo_group = {}
    modulo_number = 1
    # WIP :(
    for i, m in enumerate(monkeys):
        monkeys[i]["inspected"] = len(monkeys[i]["starting items"])
        monkeys[i]["modulo items"] = [0 for _ in range(len(monkeys))]
        modulo_number *= int(monkeys[i]["test"])
    for i in range(modulo_number):
        modulo_group[i] = 0
    #print(modulo_group)
    return 0