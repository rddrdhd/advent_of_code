#Task: https://adventofcode.com/2023/day/4
f = open('y2023/data/day04.txt', 'r')
lines = f.readlines()
f.close()
import re

lines = [s.strip() for s in lines]


def part1():
    total_score = 0
    for card in lines:
        score = 0
        score_power = 0
        _, winning_numbers, my_numbers = re.split(":|\|", card)
        winning_numbers = [int(x.group()) for x in re.finditer('\d+',winning_numbers)]
        my_numbers = [int(x.group()) for x in re.finditer('\d+',my_numbers)]
        
        for my_num in my_numbers:
            if my_num in winning_numbers:
                score = pow(2, score_power)
                score_power += 1

        total_score += score

    return total_score # 23235


def part2():
    copies = {i:1 for i in range(len(lines)+1)}
    total_score = 0
    for i, cards in enumerate(lines):
        _, winning_numbers, my_numbers = re.split(":|\|", cards)
        winning_numbers = [int(x.group()) for x in re.finditer('\d+',winning_numbers)]
        my_numbers = [int(x.group()) for x in re.finditer('\d+',my_numbers)]
        score = 0
        
        for my_num in my_numbers:
            if my_num in winning_numbers:
                score += 1
        for card_id in range( i + 1 , i + score + 1 ):
            copies[card_id] += copies[i]
        total_score += copies[i]
    return total_score # 5920640