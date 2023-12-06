INPUT_PATH = './input.txt'
GAME_START = 10
GAME_END = 40

WINNING_START = 42

cards = []

with open(INPUT_PATH) as INPUT_DATA:
  cards = INPUT_DATA.read().splitlines()

result = 0

for card in cards:
  card_numbers = card[GAME_START:GAME_END].split()
  # print(card_numbers)

  winning_numbers = card[WINNING_START:].split()
  # print(winning_numbers)

  card_total = 0

  for num in card_numbers:
    if num in winning_numbers and card_total == 0:
      card_total = 1
    elif num in winning_numbers:
      card_total *= 2

  result += card_total

print(result)