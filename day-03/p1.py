INPUT_PATH = './test.txt'

DIRS = [
  [[-1, -1], [-1, 0], [-1, 1]],
  [[0, -1],           [0, 1]],
  [[1, -1],  [1, 0],  [1, 1]]
]

lines = []

with open(INPUT_PATH) as INPUT_DATA:
  lines = INPUT_DATA.read().splitlines()


nums = [char.isdigit() for char in lines[0]]
symbols = [char != '.' and not char.isdigit() for char in lines[8]]

print(nums)
print(symbols)