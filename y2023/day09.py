#Task: https://adventofcode.com/2023/day/9
import re
f = open('y2023/data/day09.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]


def get_next_level(numbers):
    next_level = []
    for i in range(len(numbers)-1):
            next_level.append(int(numbers[i+1])-int(numbers[i]))
    return next_level


def get_prediction(list_of_levels):
    sum = 0
    for i in range(len(list_of_levels)-1,0,-1):
        sum = list_of_levels[i][-1]+list_of_levels[i-1][-1]
        list_of_levels[i-1].append(sum)
    return sum


def get_history(list_of_levels):
    sum = 0
    for i in range(len(list_of_levels)-1,0,-1):
        sum = list_of_levels[i-1][0]-list_of_levels[i][0]
        list_of_levels[i-1] = [sum] + list_of_levels[i-1] 
    return sum


def get_list_of_levels(original_numbers):
    list_of_levels = []
    nums = original_numbers
    list_of_levels.append(nums)
    while list(set(nums)) != [0]:
        nums = get_next_level(nums)
        list_of_levels.append(nums)
    return list_of_levels
     

def part1():
    sum = 0
    for line in lines:
        original_numbers = line.split(" ")
        original_numbers = [int(x) for x in original_numbers]
        list_of_levels = get_list_of_levels(original_numbers)
        sum += get_prediction(list_of_levels)
    return sum # 1834108701


def part2():
    sum = 0
    for line in lines:
        original_numbers = line.split(" ")
        original_numbers = [int(x) for x in original_numbers]
        list_of_levels = get_list_of_levels(original_numbers)
        sum += get_history(list_of_levels)
    return sum # 993