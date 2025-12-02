#Task: https://adventofcode.com/2025/day/2
import re
f = open('y2025/data/day02.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]
ranges = lines[0].split(",")

def part1():
    sum = 0
    for r in ranges:
        x,y = r.split("-")
        for num in range(int(x),int(y)+1):
            num_str = str(num)
            num_len = len(num_str)
            if num_len%2 == 0:
                half_num = num_len//2
                if num_str[:half_num] == num_str[half_num:]:
                    sum += num
    return sum


def part2():
    sum = 0
    for r in ranges:
        x,y = r.split("-")
        for num in range(int(x),int(y)+1):
            num_str = str(num)
            if re.fullmatch(r"(.+)\1+", num_str):
                sum += num
    return sum

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())