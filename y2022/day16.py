# Task: https://adventofcode.com/2022/day/1
import re
from collections import defaultdict

f = open('y2022/data/day16.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


class Cave:
    closed_valves = []
    open_valves = []
    queue = []
    starting_valve = "AA"
    remaining_minutes = 30
    total_flow = 0
    current_valve = {}

    def print_stats(self, current_valve, neighbours=[]):
        print("-- Minute", 30 - self.remaining_minutes, "--")
        # print("CV:", current_valve)
        # for n in neighbours:
        #    print("N:", n)
        print("Valves", ", ".join([d['valve'] if d["flow"] > 0 else "" for d in self.open_valves]),
              "are open, releasing", sum([d['flow'] for d in self.open_valves]), "pressure")
        # print("I am in valve",self.current_valve["valve"])

    def __init__(self, lines):
        for line in lines:
            valve = [j for j in re.findall(r'[A-Z][A-Z]', line)]
            rate = int([j for j in re.findall(r'\d+', line)][0])
            self.closed_valves.append(
                {"valve": valve[0], "flow": rate, "neighbours": valve[1:]})
            if valve[0] == self.starting_valve:
                self.current_valve = self.closed_valves.pop()
                self.queue.append(self.current_valve)
                self.open_valves.append(self.current_valve)

    def pokus2(self):
        neighbours = []
        while self.remaining_minutes > 0 or len(self.queue):

            self.print_stats(self.current_valve, neighbours)
            try:
                current_valve = self.queue.pop(-1)
                neighbours = [d for d in self.closed_valves if d['valve'] in current_valve["neighbours"]]
                sub_queue = []
                # if self.current_valve["valve"] != self.starting_valve:
                # TODO mmmm I need totally new approach. I can skip opening if it's not worth it.
                if (current_valve["valve"] != self.starting_valve):
                    self.move(current_valve)
                for n in neighbours:
                    if n not in self.open_valves:
                        sub_queue.append(n)
                sub_queue = sorted(sub_queue, key=lambda d: d['flow'])
                self.remaining_minutes -= 1
                self.queue = sub_queue + self.queue
            except IndexError:
                self.total_flow += sum([d['flow'] for d in self.open_valves])
                self.remaining_minutes -= 1

        self.print_stats([])
        self.total_flow += sum([d['flow'] for d in self.open_valves])
        return self.total_flow

    def move(self, valve):
        # MOVE

        print("Moving to valve", valve["valve"])
        self.current_valve = valve
        self.total_flow += sum([d['flow'] for d in self.open_valves])
        self.remaining_minutes -= 1
        self.print_stats(valve)

        # OPEN
        if valve in self.closed_valves:
            print("Opening valve", valve["valve"])
            self.closed_valves.remove(valve)
            self.open_valves.append(valve)
            self.total_flow += sum([d['flow'] for d in self.open_valves])
            self.remaining_minutes -= 1
            self.print_stats(valve)

    def update(self, valve, key, new_value):
        for d in self.closed_valves + self.open_valves:
            d.update((key, new_value) for k, v in d.items() if v == valve)


def part1():
    c = Cave(lines)
    print(c.pokus2())
    return 0


def part2():
    return 0
