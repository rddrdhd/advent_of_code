#Task: https://adventofcode.com/2024/day/13
import re
# Reading input data
f = open('y2024/data/day13.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]



def solve(part_two=False):
    machines = ("\n".join(lines)).split("\n\n")
    coins = 0

    for machine in machines:
        line_a, line_b, prize = machine.split("\n")

        line_a = line_a.split(": ")[1].split(", ")
        btn_a = [int(item[2:]) for item in line_a]

        line_b = line_b.split(": ")[1].split(", ")
        btn_b = [int(item[2:]) for item in line_b]

        line_prize = prize.split(": ")[1].split(", ")
        
        if not part_two:
            prize = [int(item[2:]) for item in line_prize]
        else:
            prize = [int(item[2:])+10**13 for item in line_prize]
            
        # linear equatioooooooons 
        numerator_b = prize[1] * btn_a[0] - prize[0] * btn_a[1]
        denominator_b = btn_b[1] * btn_a[0] - btn_b[0] * btn_a[1]
        times_b = numerator_b / denominator_b

        numerator_a = prize[0] - btn_b[0] * times_b
        times_a = numerator_a / btn_a[0]
        
        # solution found
        if times_a.is_integer() and times_b.is_integer():
            coins += int(times_a) * 3 + int(times_b)

    return coins


def part1():
    return solve()


def part2():
    return solve(part_two=True)


if __name__ == "__main__":
    print()
    print("P1", part1()) # 29598
    print("P2", part2()) # 93217456941970
