import re
from collections import defaultdict

def find_numbers():
  with open('3.txt', 'r', encoding='utf-8') as parts_file:
    row = 0
    numbers_list = []
    for line in parts_file:
      matches = [{'number': match.group(), 'position': [row, match.start()]} for match in re.finditer(r'\b\d+\b', line)]
      numbers_list += matches
      row += 1
    return numbers_list

def get_2d_list():
  with open('3.txt', 'r', encoding='utf-8') as parts_file:
      return [line.strip() for line in parts_file] 

numbers_list = find_numbers()
actual_list = get_2d_list()

# def is_adjacent_part(row, col):  # 140 x 140
#   if row > -1 and row < 140 and col > -1 and col < 140:
#     return actual_list[row][col].isdigit() == False and actual_list[row][col] != '.'

# def check_adjacency(dictionary):
#     number_length = len(dictionary['number'])
#     row, col = dictionary['position']

#     for row_diff in range(-1, 2):
#       for col_diff in range(-1, number_length+1):
#         if is_adjacent_part(row+row_diff, col+col_diff) == True:
#           return True
#     return False

# def add_part_numbers():
#   sum_of_parts = 0
#   for number_dict in numbers_list:
#     if check_adjacency(number_dict):
#       sum_of_parts += int(number_dict['number'])
#   return sum_of_parts

# print(add_part_numbers())

def check_adjacency(dictionary):
    number_length = len(dictionary['number'])
    row, col = dictionary['position']

    for row_diff in range(-1, 2):
      for col_diff in range(-1, number_length+1):
        if is_adjacent_gear(row+row_diff, col+col_diff) == True:
          return (row+row_diff, col+col_diff)
    return False

def is_adjacent_gear(row, col):  # 140 x 140
  if row > -1 and row < 140 and col > -1 and col < 140:
    return actual_list[row][col] == '*'

def get_gear_adjacencies():
  gear_adjacencies = defaultdict(lambda: [0, []])
  for number_dict in numbers_list:
    position_of_gear = check_adjacency(number_dict)
    if position_of_gear:
      count, parts_positions = gear_adjacencies[position_of_gear]
      parts_positions.append(int(number_dict['number']))
      gear_adjacencies[position_of_gear] = [count+1, parts_positions]
  return gear_adjacencies

def add_parts_adjacent_to_two_gears(gears):
  parts_sum = 0
  for gear_position, parts in gears.items():
    if (parts[0] == 2):
      parts_sum += parts[1][0] * parts[1][1]
  return (parts_sum)

print(add_parts_adjacent_to_two_gears(get_gear_adjacencies()))



