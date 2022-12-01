# Task: https://adventofcode.com/2020/day/4

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


def part2():
    count = 0
    passport = {}
    passports = []
    for line in lines:
        if len(line) == 0:
            passports.append(passport)
            passport = {}
        else:
            line = line.replace("\n", " ").split(" ")
            for pair in line:
                key, value = pair.split(":")
                passport[key] = value

        try:
            byr = 2002 >= int(passport["byr"]) >= 1920
            iyr = 2020 >= int(passport["iyr"]) >= 2010
            eyr = 2030 >= int(passport["eyr"]) >= 2020
            hcl = passport["hcl"].startswith("#") and len(passport["hcl"]) == 7
            ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            pid = len(passport["pid"]) == 9 and passport["pid"].isnumeric()

            # Throw ValueError if not in correct format
            set(passport["hcl"][1:]).issubset(set('0123456789abcdef'))  # Convert to int from hex

            # hgt checks
            height = int(passport["hgt"][:-2])
            if passport["hgt"].endswith("cm"):
                hgt = 193 >= height >= 150

            elif passport["hgt"].endswith("in"):
                hgt = 76 >= height >= 59

            else:
                hgt = False

            if all((byr, iyr, eyr, hgt, hcl, ecl, pid)):
               # print("valid pass:", passport)  #
                count += 1

        except (KeyError, ValueError):  # Something isn't there
            pass
    # TODO: not working for my batch :(
    return count  # < 187, not 171
