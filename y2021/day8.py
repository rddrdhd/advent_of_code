# Task: https://adventofcode.com/2021/day/8
f = open('y2021/data/day8.txt', 'r')
lines = f.readlines()
f.close()


def part1():
    count = 0
    for line in lines:
        combinations, output_values = line.split(" | ")
        output_values = output_values.strip().split(" ")
        for ov in output_values:
            if len(ov) in (2, 3, 4, 7):
                count += 1
    return count


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def check_if_equal(list_1, list_2):  # if list(string) is equal, like "asdf" and "fads"
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

def part2():
    result = []
    for line in lines:
        combinations, output_combinations = line.split(" | ")
        output_combinations = output_combinations.strip().split(" ")
        combinations = combinations.strip().split(" ")

        decoder = ["" for _ in range(10)]  # saving combinations in number's index
        to_solve = []  # for display numbers 0, 2, 3, 5, 6, 9

        # solve display numbers 1, 4, 7, 8 by unique length
        for combination in combinations:
            if len(combination) == 2:
                decoder[1] = combination
            elif len(combination) == 3:
                decoder[7] = combination
            elif len(combination) == 4:
                decoder[4] = combination
            elif len(combination) == 7:
                decoder[8] = combination
            else:
                to_solve.append(combination)

        for segments in to_solve:
            # intersections with known numbers
            is_two =   len(intersection(decoder[4], segments)) == 2 and \
                       len(segments) == 5

            is_three = len(intersection(decoder[1], segments)) == 2 and \
                       len(segments) == 5

            is_five =  len(intersection(decoder[4], segments)) == 3 and \
                       len(segments) == 5

            is_six =   len(intersection(decoder[7], segments)) == 2 and \
                       len(intersection(decoder[4], segments)) == 3 and \
                       len(segments) == 6

            is_nine =  len(intersection(decoder[7], segments)) == 3 and \
                       len(intersection(decoder[4], segments)) == 4 and \
                       len(segments) == 6

            is_zero =  len(intersection(decoder[7], segments)) == 3 and \
                       len(intersection(decoder[4], segments)) == 3 and \
                       len(segments) == 6

            if is_two:
                decoder[2] = segments
            elif is_three:
                decoder[3] = segments
            elif is_five:
                decoder[5] = segments
            elif is_six:
                decoder[6] = segments
            elif is_nine:
                decoder[9] = segments
            elif is_zero:
                decoder[0] = segments
            else:
                print("Something went wrong")

        # add the display numbers to line result
        arr_line_result = []
        for combination in output_combinations:
            for display_number, segments in enumerate(decoder):
                if check_if_equal(list(combination), list(segments)):
                    arr_line_result.append(display_number)

        int_line_result = int( str(arr_line_result[0]) +
                               str(arr_line_result[1]) +
                               str(arr_line_result[2]) +
                               str(arr_line_result[3]) )

        result.append(int_line_result)

    return sum(result)
