INPUT_FILE = './input.txt'
nice_count = 0

with open(INPUT_FILE) as DATA:
    strings = DATA.read().splitlines()

def repeatBetween(test_str: str) -> bool:
    for i in range(len(test_str) - 2):
        if test_str[i] == test_str[i + 2]:
            # print("REPEAT BETWEEN")
            return True
    # print("NO REPEAT BETWEEN")
    return False

def doubleCheck(test_str: str) -> bool:
    # the range needs to be up to len -1 to prevent overflow, but can be updated to -3
    # since we don't want to count overlaps, and can save cycles
    for i in range(len(test_str) - 3):
        # print("DOUBLE TEST", test_str[i:i+2])
        if test_str.rfind(test_str[i:i+2]) > i + 1:
            # print("DOUBLE PASS", test_str[i:i+2])
            return True
    # print("DOUBLE FAIL")
    return False

for s in strings:
    # print(s)
    if repeatBetween(s) and doubleCheck(s):
        nice_count += 1

print(nice_count)