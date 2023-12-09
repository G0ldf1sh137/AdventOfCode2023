INPUT_PATH = './input.txt'

with open(INPUT_PATH) as DATA:
    instructions = DATA.read().splitlines()

lights_on = set()

def parse(s: str):
    inst_type = s[6]
    inst = [char for char in s if char.isdigit() or char in [',','g']]
    parsed = "".join(inst).strip('g')
    split_idx = parsed.find('g')
    range1 = parsed[:split_idx]
    range2 = parsed[split_idx+1:]
    return inst_type, range1, range2

def turnOn(r1: str, r2: str):
    start_x, start_y = r1.split(',')
    end_x, end_y = r2.split(',')

    for i in range(int(start_x), int(end_x) + 1):
        for j in range(int(start_y), int(end_y) + 1):
            lights_on.add((i,j))

def turnOff(r1, r2):
    start_x, start_y = r1.split(',')
    end_x, end_y = r2.split(',')

    for i in range(int(start_x), int(end_x) + 1):
        for j in range(int(start_y), int(end_y) + 1):
            if (i, j) in lights_on:
                lights_on.remove((i,j))

def toggle(r1, r2):
    start_x, start_y = r1.split(',')
    end_x, end_y = r2.split(',')

    for i in range(int(start_x), int(end_x) + 1):
        for j in range(int(start_y), int(end_y) + 1):
            if (i, j) in lights_on:
                lights_on.remove((i,j))
            else:
                lights_on.add((i,j))

for instruction in instructions:
    inst_type, r1, r2 = parse(instruction)

    if inst_type == 'n':
        turnOn(r1, r2)
    elif inst_type == 'f':
        turnOff(r1, r2)
    elif inst_type == ' ':
        toggle(r1, r2)
    
print(len(lights_on))

