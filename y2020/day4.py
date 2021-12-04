# Task: https://adventofcode.com/2020/day/4
import re

f = open('y2020/data/day4.txt', mode='r')
lines = f.read().split('\n\n')
f.close()


def part1():
    valid = 0
    for line in lines:
        data = line.replace("\n", " ").split(" ")
        this_line_keys = []
        if len(data) == 8:
            valid += 1
        elif len(data) == 7:
            for l in data:
                key, value = l.split(":")
                this_line_keys.append(key)
            if "cid" not in this_line_keys:
                valid += 1

    return valid  # 230


def validate(data):
    valid = True
    for d in data:
        key, value = d.split(":")
        if key == "byr":  # 1920-2002
            if int(value) < 1920: valid = False
            elif int(value) > 2002: valid = False
        elif key == "iyr":  # 2010-2020
            if int(value) < 2010: valid = False
            elif int(value) > 2020: valid = False
        elif key == "eyr":  # 2020-2030
            if int(value) < 2020: valid = False
            elif int(value) > 2030: valid = False
        elif key == "hgt":  # has to ends with "cm" or "in"
            if value[-2:] == "cm":  # 150-193
                if int(value[:-2]) < 150: valid = False
                elif int(value[:-2]) > 193: valid = False
            elif value[-2:] == "in":  # 59-76
                if int(value[:-2]) < 59: valid = False
                elif int(value[:-2]) > 76: valid = False
        elif key == "hcl":
            if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value): valid = False
        elif key == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: valid = False

        elif key == "pid":
            if not re.search("[0-9]{9}", value):
                valid = False
            else:
                print(key, value, valid)

                TODOOO

        elif key == "cid":
            valid = True
        else:
            valid = False

    return valid  # 158 too high


def part2():
    valid = 0
    for line in lines:
        data = line.replace("\n", " ").split(" ")
        this_line_keys = []
        if len(data) == 8:
            if validate(data):
                valid += 1
        elif len(data) == 7:
            for l in data:
                key, value = l.strip().split(":")
                this_line_keys.append(key)
            if "cid" not in this_line_keys:
                if validate(data) :
                    valid += 1

    return valid  # 230
