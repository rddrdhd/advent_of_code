# Task: https://adventofcode.com/2022/day/1
import re
from collections import defaultdict

f = open('y2022/data/day16.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


class Cave:
    valves = []
    queue = []
    starting_valve = "AA"

    def __init__(self, lines):
        for line in lines:
            valves = [j for j in re.findall(r'[A-Z][A-Z]', line)]
            rate = int([j for j in re.findall(r'\d+', line)][0])
            self.valves.append(
                {"valve": valves[0], "flow": rate, "neighbours": valves[1:], "open": False, "max_flow": 0})
            if valves[0] == self.starting_valve:
                self.queue.append(self.valves.pop())

    def find_most_pressure_path(self, remaining_minutes=30):

        max_flow = 0
        total_flow = 0
        while remaining_minutes:
            while len(self.queue):
                print("-- Minute", 30 - remaining_minutes, "--")
                current_valve = self.queue.pop(-1)
                current_valve["max_flow"] = max_flow + current_valve["flow"]

                neighbours = [d for d in self.valves if d['valve'] in current_valve["neighbours"]]

                for n in neighbours:
                    # TODO add to queue ordered by flow
                    if not n["open"]:
                        self.queue.append(n)
                        self.update(n["valve"], "open", True)
                        self.update(n["valve"], "max_flow", max_flow + n["flow"])
                    else:
                        print("\tOpening valve",n["valve"])
                max_flow = current_valve["max_flow"]
                remaining_minutes -= 1
                print("\treleasing", max_flow, "pressure")
            # after we run out of valves we can open

            print("-- Minute", 30 - remaining_minutes, "--")
            total_flow += max_flow
            remaining_minutes -= 1
            print("\treleasing", max_flow, "pressure")
        return total_flow

    def update(self, valve, key, new_value):
        for d in self.valves:
            d.update((key, new_value) for k, v in d.items() if v == valve)


def part1():
    c = Cave(lines)
    print(c.find_most_pressure_path())
    return 0


def part2():
    return 0
