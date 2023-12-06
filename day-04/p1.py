INPUT_PATH = './input.txt'
GAME_START = 10     # test is 8, input is 10
GAME_END = 40       # test is 23, input is 40
WINNING_START = 42  # test is 25, input is 42

cards = []
result = 0

with open(INPUT_PATH) as INPUT_DATA:
  cards = INPUT_DATA.read().splitlines()

for card in cards:
  card_numbers = card[GAME_START:GAME_END].split()
  winning_numbers = card[WINNING_START:].split()
  card_total = 0

  for num in card_numbers:
    if num in winning_numbers and card_total == 0:
      card_total = 1
    elif num in winning_numbers:
      card_total *= 2

  result += card_total

print(result)