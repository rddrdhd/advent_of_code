#Task: https://adventofcode.com/2023/day/1
import re
f = open('y2023/data/day01.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

def part1():
    sum = 0
    for line in lines:
        nums=re.findall(r'\d', line)
        digit = [nums[0],nums[-1]]
        digit = ''.join(digit)
        sum += int(digit)
    return sum # 54159

def part2():
    sum = 0
    for line in lines:
        # to include "oneight" = "one","eight"
        line=line.replace('one','one1one')
        line=line.replace('two','two2two')
        line=line.replace('three','three3three')
        line=line.replace('four','four4four')
        line=line.replace('five','five5five')
        line=line.replace('six','six6six')
        line=line.replace('seven','seve7seven')
        line=line.replace('eight','eight8eight')
        line=line.replace('nine','nine9nine')

        nums=re.findall(r'\d', line)
        digit = [nums[0],nums[-1]]
        digit = ''.join(digit)
        sum += int(digit)
    return sum # 53866