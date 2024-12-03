#Task: https://adventofcode.com/2024/day/3
import re
f = open('y2024/data/day03.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

def part1():
    sum = 0
    for line in lines:
        matches = re.findall(r'mul\((\d+),(\d+)\)', line)
        for match in matches:
            a,b = match
            sum += int(a)*int(b)
    return sum # 183669043

def part2():
    sum = 0
    reading = True  

    for line in lines:
        substrs = re.split(r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))', line)
        substrs = [s for s in substrs if s.strip()] 

        for str in substrs:
            if str == "do()":
                reading = True  
            elif str == "don't()":
                reading = False  
            elif str.startswith("mul(") and reading:
                # Extract numbers from `mul(a,b)`
                match = re.match(r'mul\((\d+),(\d+)\)', str)
                if match:
                    a, b = map(int, match.groups())
                    sum += a * b  
    return sum # 59097164

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())