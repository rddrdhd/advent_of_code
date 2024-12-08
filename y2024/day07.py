#Task: https://adventofcode.com/2024/day/1
f = open('y2024/data/day07.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

def get_numbers(line):
    numbers = line.split()
    numbers[0] = numbers[0][:-1]
    numbers = [int(n) for n in numbers]
    result = numbers[0]
    numbers = numbers[1:]
    return result, numbers


def get_combinations(operators, num_slots):
    combinations = [""]
    for _ in range(num_slots):
        new_combinations = []
        for comb in combinations:
            for op in operators:
                new_combinations.append(comb + op)
        combinations = new_combinations
    return combinations


def is_equation_valid(combinations, numbers, test_value, operators):
    valid = False
    for operators in combinations:
        result = numbers[0]
        for i, op in enumerate(operators):
            if op == '+':
                result += numbers[i + 1]
            elif op == '*':
                result *= numbers[i + 1]
            elif op == '|':
                result = int(str(result)+str(numbers[i+1]))

        if result == test_value:
            valid = True
            break
    return valid


def get_result(operators):
    sum = 0
    for line in lines:
        test_value, numbers = get_numbers(line)
        num_slots = len(numbers) - 1
        combinations = get_combinations(operators, num_slots)
        valid = is_equation_valid(combinations, numbers, test_value, operators)
        if valid:
            sum += test_value
    return sum

def part1():
    return get_result('+*')


def part2():
    return get_result('+*|')


if __name__ == "__main__":
    print()
    print("P1",part1()) # 4555081946288
    print("P2",part2()) # 227921760109726
    