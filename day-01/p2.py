INPUT_PATH = './input.txt'
result = 0

TEXT_DIGITS = [
    'one', '1',
    'two', '2',
    'three', '3',
    'four', '4',
    'five', '5',
    'six', '6',
    'seven', '7',
    'eight', '8',
    'nine', '9'
]

with open(INPUT_PATH) as input_data:
    for line in input_data.readlines():
        # (POS, DIGIT, VAL)
        first_digit = None
        last_digit = None

        for i in range(len(TEXT_DIGITS)):
            first_index = line.find(TEXT_DIGITS[i])
            if first_index >= 0 and (first_digit is None or first_index <= first_digit[0]):
                first_digit = (first_index, TEXT_DIGITS[i], ((i//2)+1)*10)

            last_index = line.rfind(TEXT_DIGITS[i])
            if last_index >= 0 and (last_digit is None or last_index >= last_digit[0]):
                last_digit = (last_index, TEXT_DIGITS[i], (i//2)+1)

        # print(line, first_digit[1], first_digit[2], last_digit[1], last_digit[2])
        result += first_digit[2] + last_digit[2]

print(result)