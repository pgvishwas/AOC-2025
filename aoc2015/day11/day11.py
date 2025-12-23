from aoc2015.utils.utils import read_input
def increment(pw):
    pw = list(pw)
    i = len(pw) - 1

    while i >= 0:
        if pw[i] == 'z':
            pw[i] = 'a'
            i -= 1
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break

    return ''.join(pw)
def has_straight(pw):
    for i in range(len(pw) - 2):
        a, b, c = pw[i:i+3]
        if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
            return True
    return False
def has_no_forbidden(pw):
    return not any(c in pw for c in "iol")
def has_two_pairs(pw):
    pairs = set()
    i = 0
    while i < len(pw) - 1:
        if pw[i] == pw[i + 1]:
            pairs.add(pw[i])
            i += 2
        else:
            i += 1
    return len(pairs) >= 2
def next_valid_password(pw):
    while True:
        pw = increment(pw)
        if (
            has_straight(pw)
            and has_no_forbidden(pw)
            and has_two_pairs(pw)
        ):
            return pw


def star1() -> int:
    data = read_input()
    input_string = data[0]
    print(input_string)
    new_string = next_valid_password(input_string)
    return next_valid_password(new_string)


def star2() -> int:
    data = read_input()
    # TODO: Implement star 2 solution
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
