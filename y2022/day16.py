# Task: https://adventofcode.com/2022/day/1
import re
from collections import defaultdict

f = open('y2022/data/day16.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]



def part1(): 
    time_remaining = 30 #minutes
    start_valve = 'AA'
    valves = {} # flow, children, opened   
    open_valves_pressures = []
    pressure_released = 0
    for line in lines:
        parts = line.split(' ')
        valve = parts[1]
        flow = int(parts[4][5:-1])
        leads_to = parts[9:]
        leads_to = [x[:-1] if ',' == x[-1] else x for x in leads_to]
        valves[valve] = [flow, leads_to]
    print(valves)
    current_valve_name = start_valve
    while time_remaining:
        print("== Minute",29-time_remaining,"==")
        # do the best thing: move/open
        current_valve = valves[current_valve_name]
        for child in current_valve[1]:
            print(child)
            if valves[child][0] > current_valve[0] and valves[child][0] not in open_valves_pressures:
                # move
                time_remaining -= 1
                current_valve_name = child
                print("You move to value",current_valve_name)
            else:
                # open
                time_remaining -= 1
                print("You open the valve",current_valve_name)
                open_valves_pressures.append(current_valve[0])
        pressure_released += sum(open_valves_pressures)
    return pressure_released


def part2():
    return 0
