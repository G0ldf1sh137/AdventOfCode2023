INPUT_FILE = './input.txt'
nice_count = 0

with open(INPUT_FILE) as DATA:
    strings = DATA.read().splitlines()

def vowelCheck(test_str: str) -> bool:
    # print(test_str)
    vowel_count = 0
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    for char in test_str:
        if char in VOWELS:
            vowel_count += 1
            if vowel_count >= 3:
                # print('VOWEL PASS')
                return True
    # print('VOWEL FAIL') 
    return False

def doubleCheck(test_str: str) -> bool:
    for i in range(len(test_str) - 1):
        if test_str[i] == test_str[i + 1]:
            # print("DOUBLE PASS")
            return True
    # print("DOUBLE FAIL")
    return False

def naughtySubCheck(test_str: str) -> bool:
    NAUGHTY = ['ab', 'cd', 'pq', 'xy']
    for sub in NAUGHTY:
        if test_str.find(sub) >= 0:
            # print("IS NAUGHTY")
            return True
    # print("NOT NAUGHTY")
    return False

for s in strings:
    if vowelCheck(s) and doubleCheck(s) and not naughtySubCheck(s):
        nice_count += 1

print(nice_count)