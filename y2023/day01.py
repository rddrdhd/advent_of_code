#Task: https://adventofcode.com/2023/day/1
import re
f = open('y2023/data/day01.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

def part1():
    sum = 0
    return 0
    for line in lines:

        print(line)
        nums=re.findall(r'\d', line)
        print(nums)
        digit = [nums[0],nums[-1]]
        digit = ''.join(digit)
        print(digit)
        sum += int(digit)
    return sum # 54159
def get_last_digit_from_word(word):
    return '0' if word == 'zero' or word == 'ten' or word == 'twenty' or word == 'thirty' or word == 'fourty' or word == 'fifty' or word == 'sixty' or word == 'seventy' or word == 'eighty' or word == 'ninety'  else '1' if word == 'one' or word == 'eleven' else '2' if word == 'two' or word == 'twelve' else '3' if word == 'three' or word == 'thirteen' else '4' if word == 'four' or word == 'fourteen' else '5' if word == 'five' or word == 'fifteen' else '6' if word == 'six' or word == 'sixteen' else '7' if word == 'seven' or word == 'seventeen' else '8' if word == 'eight' or word == 'eighteen' else '9' 
       
def part2():
    #TODO
    sum = 0
    numbers = "(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|fourty|fifty|sixty|seventy|eighty|ninety\d)"
    for line in lines:
        nums=re.findall(numbers, line)
        digit = [nums[0],nums[-1]]
        
        print(digit, end="->")
        if not digit[0].isdigit():
            word = digit[0]
            digit[0] = get_last_digit_from_word(word)
        if not digit[1].isdigit():
            word = digit[1]
            digit[1] = get_last_digit_from_word(word)
        digit = ''.join(digit)
        
        print(digit)
        sum += int(digit)
    return sum # not 53201, not 53900
