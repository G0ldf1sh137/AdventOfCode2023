INPUT_PATH = './input.txt'
result = 0

with open(INPUT_PATH) as input_data:
    for line in input_data.readlines():
        nums = [char for char in line if char.isnumeric()]
        # print(f'{line} - {nums[0]+nums[-1]}')
        result += int(nums[0]+nums[-1])

print(result)