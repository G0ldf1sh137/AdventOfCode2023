import hashlib as hash
KEY = 'ckczppom'
num = 0

while True:
    test_input = KEY + str(num)
    result = hash.md5(test_input.encode()).hexdigest()
    if result[:5] == '00000':
        break
    num += 1
print(num)