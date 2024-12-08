#Task: https://adventofcode.com/2024/day/1
f = open('y2024/data/day08.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

Y, X = 0, 1

def print_city(antinodes):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (y,x) in antinodes:
                print("#",end="")
            else:
                print(lines[y][x],end="")
        print()


def location_in_bounds(xy):
    return 0 <= xy[Y] < len(lines) and 0 <= xy[X] < len(lines[0])


def get_antennas():
    antennas = {}
    for y,line in enumerate(lines):
        for x,char in enumerate(line):
            if char != '.':
                if char in antennas.keys():
                    antennas[char].append((y,x))
                else:
                    antennas[char] = [(y,x)]
    return antennas


def get_antinodes(antennas, second_part = False):
    antinodes = []
    for a,values in antennas.items():
        i = 0
        while i < len(values):
            if second_part: 
                antinodes.append(values[i])
            j = i
            while j < len(values)-1:
                a1 = antennas[a][i]
                a2 = antennas[a][j+1]
                diff = (-(a1[Y]-a2[Y]), -(a1[X]-a2[X]))

                an1 = (a1[Y]-diff[Y], a1[X]-diff[X])
                an2 = (a2[Y]+diff[Y], a2[X]+diff[X])

                if not second_part:
                    if location_in_bounds(an1):
                        antinodes.append((an1))
                    if location_in_bounds(an2):
                        antinodes.append((an2))
                else: # only for second part
                    while location_in_bounds(an1):
                        antinodes.append((an1))
                        an1 = (an1[Y]-diff[Y], an1[X]-diff[X])
                    while location_in_bounds(an2):
                        antinodes.append((an2))
                        an2 = (an2[Y]+diff[Y], an2[X]+diff[X])
                j += 1
            i += 1
    return antinodes


def part1():
    antennas = get_antennas()
    antinodes = get_antinodes(antennas, second_part=False)
    return len(list(set(antinodes)))


def part2():
    antennas = get_antennas()
    antinodes = get_antinodes(antennas, second_part=True)
    return len(list(set(antinodes)))


if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())
