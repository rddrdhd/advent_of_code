# https://adventofcode.com/2021/day/3

f = open('y2021/data/day3.txt', 'r')
lines = f.readlines()
f.close()


def is_zero_most_common(lines, position, or_equal=True):
    count = 0
    for line in lines:
        if line[position] == "0":
            count += 1
    if count < (len(lines) - count):
        return True
    elif count == (len(lines) - count):
        return or_equal
    return False


def part1():
    row_length = len(lines[0].strip())
    gamma_rate = ""
    consumption_rate = ""

    for column in range(row_length):
        gamma_rate += "0" if is_zero_most_common(lines, column, False) else "1"
        consumption_rate += "1" if is_zero_most_common(lines, column, True) else "0"
    return int(gamma_rate, 2) * int(consumption_rate, 2)  # 3549854


def part2():
    oxygen = lines
    oxygen_rating = 0

    for i in range(len(lines[0].strip())):
        bit_counter = {'0': 0, '1': 0}

        for number in oxygen:
            bit_counter[number[i]] += 1

        if bit_counter['1'] >= bit_counter['0']:
            most_common = '1'

        else:
            most_common = '0'

        oxygen = [n for n in oxygen if n[i] == most_common]

        if len(oxygen) == 1:
            oxygen_rating = int(oxygen[0], 2)

    co2 = lines
    co2_rating = 0

    for i in range(len(lines[0].strip())):
        bit_counter = {'0': 0, '1': 0}

        for number in co2:
            bit_counter[number[i]] += 1

        if bit_counter['1'] < bit_counter['0']:
            least_common = '1'

        else:
            least_common = '0'

        co2 = [n for n in co2 if n[i] == least_common]

        if len(co2) == 1:
            co2_rating = int(co2[0], 2)
    return int(oxygen_rating) * int(co2_rating)  # 3765399
