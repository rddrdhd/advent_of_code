# Task: https://adventofcode.com/2021/day/10
f = open('y2021/data/day10.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]


def part1():
    opening_brackets = ['(', '[', '{', '<']
    closing_brackets = [')', ']', '}', '>']
    brackets_score = [3, 57, 1197, 25137]
    score = [0, 0, 0, 0]
    score_sum = 0
    for line in lines:
        stack = []
        for bracket in line:
            if bracket in opening_brackets:
                stack.append(bracket)
            else:
                popped = stack.pop()
                if closing_brackets.index(bracket) == opening_brackets.index(popped):
                    continue
                else:  # wrong closing
                    score[closing_brackets.index(bracket)] += 1
                    break

    for i in range(len(score)):
        score_sum += score[i] * brackets_score[i]

    return score_sum














def part2():
    brackets = {"open" : ['(', '[', '{', '<'],
                "close": [')', ']', '}', '>'],
                "score": [1, 2, 3, 4]}
    correct_lines = []
    line_scores = []

    for i in range(len(lines)):
        corrupted_line = False
        stack = []
        for bracket in lines[i]:
            if bracket in brackets["open"]:
                stack.append(bracket)
            else:
                opening_b = stack.pop()
                closing_b = bracket
                if brackets["close"].index(closing_b) == brackets["open"].index(opening_b):
                    if lines[i].index(bracket) == len(lines[i])-1:
                        correct_lines.append(lines[i])
                else:
                    corrupted_line = True
        if not corrupted_line:
            alone_opening_b = list(reversed(stack))
            line_score = 0
            for opening_b in alone_opening_b:
                index_b = brackets["open"].index(opening_b)
                line_score *= 5
                line_score += brackets["score"][index_b]
            line_scores.append(line_score)

    line_scores.sort()
    middle = int((len(line_scores))/2)
    return line_scores[middle]
