from aoc2015.utils.utils import read_input


def star1() -> int:
    data = read_input()[0]
    floor_value = 0
    for val in data:
        if val == '(':
            floor_value += 1
        else:
            floor_value -= 1
    # TODO: Implement star 1 solution
    return floor_value


def star2() -> int:
    data = read_input()[0]
    floor_value = 0
    position=0
    length = len(data)
    for i in range(length):
        if data[i] == '(':
            floor_value += 1
        else:
            floor_value -= 1
        if floor_value == -1:
            position = i+1
            break

    # TODO: Implement star 2 solution
    return position


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
