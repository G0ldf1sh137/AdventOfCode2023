INPUT_PATH = './input.txt'
current_coord = (0, 0)
houses_visited = set(current_coord)

with open(INPUT_PATH) as DATA:
    travel_path = DATA.read().rstrip()

for step in travel_path:
    if step == '<':
        current_coord = (current_coord[0] - 1, current_coord[1])
    elif step == '>':
        current_coord = (current_coord[0] + 1, current_coord[1])
    elif step == '^':
        current_coord = (current_coord[0], current_coord[1] - 1)
    elif step == 'v':
        current_coord = (current_coord[0], current_coord[1] + 1)
    houses_visited.add(current_coord)


print(len(houses_visited))