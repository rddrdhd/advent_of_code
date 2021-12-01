# Task: https://adventofcode.com/2020/day/2

f = open('y2020/data/day2.txt', 'r')
lines = f.readlines()
f.close()

def part1():
    count = 0
    for line in lines:
        policy, letter, password = line.strip().split(' ')
        min_char, max_char = map(int,policy.split('-'))
        letter = letter[:-1]
        
        if (min_char <= password.count(letter) and password.count(letter) <= max_char):
            count += 1
    return count #548




def part2():
    count = 0
    for line in lines:
        policy, letter, password = line.strip().split(' ')
        first_pos, second_pos = map(int,policy.split('-'))
        letter = letter[:-1]
        
        if( (password[first_pos-1]==letter) != (password[second_pos-1]==letter)):
            count += 1
    return count #502

