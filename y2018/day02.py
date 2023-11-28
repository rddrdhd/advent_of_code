#Task: https://adventofcode.com/2018/day/2
f = open('y2018/data/day02.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

def part1():
    double_letter=0
    tripple_letter=0
    for line in lines:
        hist={}
        for char in line:
            if char in hist:
                hist[char]+=1
            else:
                hist[char]=1
        try:
            if list(hist.keys())[list(hist.values()).index(3)]:
                tripple_letter+=1
        except ValueError: # nothing tripple
            pass
        try:
            if list(hist.keys())[list(hist.values()).index(2)]:
                double_letter+=1
        except ValueError: # nothing double
            pass
    return double_letter*tripple_letter

def almost_match(word1, word2):
    found = False
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            if found:
                return False
            else:
                found = True

    return found

def part2():
    i = 0
    j = i+1
    res=""
    while True:
        word1 = lines[i]
        word2 = lines[j]
        if almost_match(word1, word2):
            # get the result
            for k in range(0,len(word1)):
                if word1[k] == word2[k]:
                    res+=word1[k]
                else:
                    pass
            return res
        else:
            # try another combination
            j+=1
            if j >= len(lines):
                j = 0
                i = i+1
                if i >= len(lines):
                    return 0
