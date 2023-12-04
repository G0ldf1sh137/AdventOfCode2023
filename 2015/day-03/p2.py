INPUT_PATH = './input.txt'
current_coord = (0, 0)
houses_visited = set()
houses_visited.add(current_coord)

with open(INPUT_PATH) as DATA:
    travel_path = DATA.read().rstrip()

santa_path = travel_path[::2]
robo_path = travel_path[1::2]

def calcRoute(travel_path:str):
    current_coord = (0, 0)
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

calcRoute(santa_path)
calcRoute(robo_path)
print(len(houses_visited))