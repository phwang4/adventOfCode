import re
def part1():
  with open('1.txt', 'r', encoding='utf-8') as calibration_file:
    sums = 0
    for line in calibration_file:
      matches = re.findall(r'\d', line)
      sums += 10 * int(matches[0]) + int(matches[-1])
    print(sums)

number_words = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9,
}

def part2():
  with open('1.txt', 'r', encoding='utf-8') as calibration_file:
    sums = 0
    for line in calibration_file:
      matches = re.findall(r'(?=(one))|(?=(two))|(?=(three))|(?=(four))|(?=(five))|(?=(six))|(?=(seven))|(?=(eight))|(?=(nine))|(?=(\d))', line)
      print(matches)
      sums += 10 * number_words[list(filter(None, matches[0]))[0]] + number_words[list(filter(None, matches[-1]))[0]]
    print(sums)

part2()