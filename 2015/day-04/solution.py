import hashlib as hash
KEY = 'ckczppom'

def test(key:str, target:str):
    num = 0
    while True:
        test_input = KEY + str(num)
        result = hash.md5(test_input.encode()).hexdigest()
        if result[:len(target)] == target:
            break
        num += 1
    print(num)

def main():
    print("PART 1")
    test(KEY, '00000')

    print("PART 2")
    test(KEY, '000000')

if __name__ == "__main__":
    main()