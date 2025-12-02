from aoc2025.utils.utils import read_input
import re


def star1() -> int:
    data = read_input()
    data = data[0].split(',')
    range_data  = [list(map(int, item.split('-'))) for item in data]
    invalid_value = 0
    pattern = re.compile(r'^(\d+)\1$')
    for value in range_data:
        lower = value[0]
        higher = value[1]
        for number in range(lower, higher+1):
            str_value = str(number)
            if pattern.match(str_value):
                invalid_value += number
    return invalid_value

def star2() -> int:
    data = read_input()
    data = data[0].split(',')
    range_data = [list(map(int, item.split('-'))) for item in data]
    invalid_value = 0
    pattern = re.compile(r'^(\d+)\1+$')
    for value in range_data:
        lower = value[0]
        higher = value[1]
        for number in range(lower, higher + 1):
            str_value = str(number)
            if pattern.match(str_value):
                invalid_value += number
    return invalid_value


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
