from aoc2015.utils.utils import read_input
import hashlib

def star1() -> int:
    data = read_input()
    # TODO: Implement star 1 solution
    secret_key=data[0]
    numerical_key = 0
    while True:
        text_to_hash = secret_key + str(numerical_key)
        hash_object = hashlib.md5(text_to_hash.encode()).hexdigest()
        if hash_object[:5] == "00000":
            break
        numerical_key += 1

    return numerical_key


def star2() -> int:
    data = read_input()
    # TODO: Implement star 2 solution
    secret_key=data[0]
    numerical_key = 117946
    while True:
        text_to_hash = secret_key + str(numerical_key)
        hash_object = hashlib.md5(text_to_hash.encode()).hexdigest()
        if hash_object[:6] == "000000":
            break
        numerical_key += 1

    return numerical_key
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
