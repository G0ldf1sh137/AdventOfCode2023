INPUT_PATH = './input.txt'
MAX_COUNT = {
  'red': 12,
  'green': 13,
  'blue': 14
}
result = 0

with open(INPUT_PATH) as INPUT_DATA:
  lines = INPUT_DATA.readlines()

def checkPulls(pulls: str) -> bool:
  pull = pulls.split(',')
  for colors in pull:
    count_color = colors.split()
    print(count_color)
    if int(count_color[0]) > MAX_COUNT[count_color[1]]:
      print("NOT POSSIBLE")
      return False
  return True

def parseLine(line: str) -> int:
  game_end = line.find(':')
  game_id = int(line[5:game_end])
  # print('ID:', game_id)
  pulls = line[game_end+2:].split(';')
  valid = True
  for pull in pulls:
      valid = checkPulls(pull)
      if not valid:
        return 0
  return game_id

# parseLine(lines[0])
for line in lines:
  result += parseLine(line)

print(result)