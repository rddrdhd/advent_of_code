# Task: https://adventofcode.com/2022/day/10
f = open('y2022/data/day10.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def get_signal_strength_values():
    cycle = 0
    carry = 0
    signal_strength = [1]
    for line in lines:
        i = line.split(" ")[0]
        signal_strength.append(carry + signal_strength[-1])

        if i == "addx":
            cycle += 1
            signal_strength.append(signal_strength[-1])
            cycle += 1
            carry = int(line.split(" ")[1])
        elif i == "noop":
            cycle += 1
            carry = 0

    signal_strength.append(carry + signal_strength[-1])
    return signal_strength


def get_display(width, height):
    display = []
    for row in range(height):
        r = []
        for cell in range(width):
            r.append(".")
        display.append(r)
    return display


def print_display(display):
    print()
    for r in display:
        print("".join(r))


def part1():
    signal = get_signal_strength_values()
    final_signal_strength = 0
    for i in range(len(signal)):
        if (i != 0) and ((i - 20) % 40 == 0):
            final_signal_strength += i * int(signal[i])
    return final_signal_strength


def part2():
    display = get_display(40, 6)
    signal = get_signal_strength_values()
    for cycle, sprite in enumerate(signal):
        if cycle != 0 and cycle != len(signal) - 1:  # ignore 0 and -1
            position = cycle - 1
            row = position // 40
            pixel = position % 40
            sprite_position = [signal[cycle] % 40 - 1, signal[cycle] + 1 % 40 - 1, signal[cycle] + 2 % 40 - 1]
            if pixel in sprite_position:
                display[row][pixel] = "█"
            else:
                display[row][pixel] = "."
    print_display(display)
    return "^^^ visual output ^^^"
