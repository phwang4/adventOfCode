import re

def check_valid(pull_str):
  pull, color = pull_str.split(' ')
  match color:
    case 'red':
      return int(pull) <= 12
    case 'green':
      return int(pull) <= 13
    case 'blue':
      return int(pull) <= 14

def find_games():
  bad_game_sums = 0
  with open('2.txt', 'r', encoding='utf-8') as cubes_file:
    for line in cubes_file:
      game = int(line.split(':')[0][5:])
      pulls = re.split(r'[;,]', line.split(':')[1])
      for pull in pulls:
        if check_valid(pull.strip()) == False:
          print(f'Game {game} is not valid because {pull.strip()}')
          bad_game_sums += game
          break;
  return 5050 - bad_game_sums

# print(find_games())

# r,g,b
def get_min_cubes(pulls):
  min_cubes = [0, 0, 0]
  for pull in pulls:
    num_cubes, color = pull.strip().split(' ')
    match color:
      case 'red':
        min_cubes[0] = max(min_cubes[0], int(num_cubes))
      case 'green':
        min_cubes[1] = max(min_cubes[1], int(num_cubes))
      case 'blue':
        min_cubes[2] = max(min_cubes[2], int(num_cubes))
  return min_cubes

def get_power_sums():
  power_sums = 0
  with open('2.txt', 'r', encoding='utf-8') as cubes_file:
    for line in cubes_file:
      pulls = re.split(r'[;,]', line.split(':')[1])
      min_cubes = get_min_cubes(pulls)
      print(f'min_cubes is {min_cubes}')
      power_sums += min_cubes[0] * min_cubes[1] * min_cubes[2]
  return power_sums

print(get_power_sums())
