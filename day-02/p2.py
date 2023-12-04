INPUT_PATH = './input.txt'
result = 0

with open(INPUT_PATH) as INPUT_DATA:
  lines = INPUT_DATA.readlines()

def checkPulls(pulls: str, game_mins: dict) -> dict:
  pull = pulls.split(',')
  for colors in pull:
    count_color = colors.split()
    # print(count_color)
    if count_color[1] not in game_mins:
      # print("Adding new")
      game_mins[count_color[1]] = int(count_color[0])
    if int(game_mins[count_color[1]]) < int(count_color[0]):
      # print("updating")
      game_mins[count_color[1]] = int(count_color[0])

  return game_mins

def parseGame(line: str) -> int:
  game_end = line.find(':')
  game_mins = dict()
  
  pulls = line[game_end+2:].split(';')
  for pull in pulls:
      game_mins = checkPulls(pull, game_mins)
  
  result = 1
  for color_min in game_mins:
    result *= game_mins[color_min]
  return result

# parseGame(lines[0])
for line in lines:
  result += parseGame(line)

print(result)