# Task: https://adventofcode.com/2021/day/13
f = open('y2021/data/day13.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]
print("Wait for it...", end="\r")

def get_data(lines):
    max_x = 0
    max_y = 0
    dots_coords, instructions = lines[:lines.index("")], lines[lines.index(""):]
    instructions.remove("")
    fold_instructions = []
    for i in instructions:
        _, _, fold = i.split(" ")
        if "x" in fold:
            _, x = fold.split("=")
            fold_instructions.append([int(x), 0])
        if "y" in fold:
            _, y = fold.split("=")
            fold_instructions.append([0, int(y)])

    for c in dots_coords:
        x, y = c.split(",")
        x = int(x)
        y = int(y)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    return dots_coords, fold_instructions, max_x, max_y


def get_folded_dots(dots_coords, fold_instruction, max_x, max_y):
    fold_x, fold_y = fold_instruction
    new_coords = []
    new_max_x = max_x
    new_max_y = max_y
    if fold_y:
        new_max_y = fold_y
        for y in range(max_y + 1):
            # first half
            if y < fold_y:
                for x in range(max_x + 1):
                    if str(x) + "," + str(y) in dots_coords:
                        new_coords.append(str(x) + "," + str(y))
            # mirroring bottom half
            if y > fold_y:
                upper_y = fold_y - (y - fold_y)
                for x in range(max_x + 1):
                    if str(x) + "," + str(y) in dots_coords:
                        if str(x) + "," + str(upper_y) not in dots_coords:
                            new_coords.append(str(x) + "," + str(upper_y))

    if fold_x:
        new_max_x = fold_x
        for x in range(max_x + 1):
            # left half
            if x < fold_x:
                for y in range(max_y + 1):
                    if str(x) + "," + str(y) in dots_coords:
                        new_coords.append(str(x) + "," + str(y))
            # mirroring right half
            if x > fold_x:
                for y in range(max_y + 1):
                    new_x = fold_x - (x - fold_x)
                    if str(x) + "," + str(y) in dots_coords:
                        if str(new_x) + "," + str(y) not in dots_coords:
                            new_coords.append(str(new_x) + "," + str(y))
    return new_coords, new_max_x, new_max_y


def part1():
    dots_coords, fold_instructions, max_x, max_y = get_data(lines)
    new_coords, max_x, max_y = get_folded_dots(dots_coords, fold_instructions[0], max_x, max_y)

    return len(new_coords)  # 710


def part2():
    dots_coords, fold_instructions, max_x, max_y = get_data(lines)
    new_coords = dots_coords.copy()
    for i in fold_instructions:
        new_coords, max_x, max_y = get_folded_dots(new_coords, i, max_x, max_y)
    print("2021, Day 13 solution is a picture:")
    for y in range(max_y):
        for x in range(max_x):
            if str(x) + "," + str(y) in new_coords:
                print("#", end="")
            else:
                print(" ", end="")
        print()

    return None
"""
#### ###  #     ##  ###  #  # #    ###
#    #  # #    #  # #  # #  # #    #  #
###  #  # #    #    #  # #  # #    #  #
#    ###  #    # ## ###  #  # #    ###
#    #    #    #  # # #  #  # #    # #
#### #    ####  ### #  #  ##  #### #  #
"""
