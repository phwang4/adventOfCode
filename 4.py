import re

def get_winnings(actual, winning_map):
    num_winnings = 0
    for actual_number in actual:
        if winning_map.get(actual_number) == 1:
            num_winnings += 1
    return num_winnings 

def format_card(line):
    winning, actual = line.split('|')
    winning = re.split(r'\s{1,2}', winning.split(':')[1].strip())
    actual = re.split(r'\s{1,2}', actual.strip())
    winning_map = {}
    for winning_number in winning:
        winning_map.update({winning_number: 1})
    return actual, winning_map

with open('4.txt') as scratch_cards:
    winnings_list = []
    total_cards = 0
    for line in scratch_cards:
        actual, winning_map = format_card(line)
        num_winnings = get_winnings(actual, winning_map)
        winnings_list.append([num_winnings, 1])
    
    for idx, [num_winnings, amt] in enumerate(winnings_list):
        total_cards += amt
        for x in range(num_winnings):
            winnings_list[x+idx+1][1] += amt
    print(total_cards)