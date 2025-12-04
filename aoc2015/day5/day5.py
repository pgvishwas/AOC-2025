from aoc2015.utils.utils import read_input

def check_rules(string):
    vowel_count=0
    double_count=False
    bad_pair = False
    banned_pair = ['ab','cd','pq','xy']
    for char in string:
        if char in 'aeiou':
            vowel_count += 1
    for i in range(len(string)-1):
        if string[i]==string[i+1] and not double_count:
            double_count=True
        if string[i:i+2]  in banned_pair:
            bad_pair = True

    return vowel_count>=3 and double_count and not bad_pair

def new_check_rules(string):
    pair_appears_twice = False
    repeat_middle = False
    for i in range(len(string)-1):
        if string.count(string[i:i+2]) >= 2:
            pair_appears_twice = True
            break

    for i in range(len(string)-2):
        if string[i]==string[i+2] and not repeat_middle:
            repeat_middle = True
            break

    return pair_appears_twice and repeat_middle

def star1() -> int:
    data = read_input()
    nice_strings=0
    # TODO: Implement star 1 solution
    for strings in data:
        if check_rules(strings):
            nice_strings += 1

    return nice_strings


def star2() -> int:
    data = read_input()
    nice_strings=0
    # TODO: Implement star 2 solution
    for strings in data:
        if new_check_rules(strings):
            nice_strings+=1
    return nice_strings


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
