INPUT_DATA = ""
instruction_count = 0
floor_count = 0
with open("./input.txt") as INPUT:
  INPUT_DATA = INPUT.read()

for char in INPUT_DATA:
  instruction_count += 1
  if char == "(":
    floor_count += 1
  else:
    floor_count -= 1

  if floor_count < 0:
    print("Basement Step:", instruction_count)
    break

print(floor_count)