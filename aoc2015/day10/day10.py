from aoc2015.utils.utils import read_input
from itertools import groupby

def look_and_say(s: str) -> str:
    return "".join(
        f"{len(list(group))}{digit}"
        for digit, group in groupby(s)
    )
def run_look_and_say(start: str, n: int) -> str:
    s = start
    for _ in range(n):
        s = look_and_say(s)
    return s

def star1() -> int:
    data = read_input()
    return len(run_look_and_say("1113122113", 40))



def star2() -> int:
    data = read_input()
    string = data[0]
    return len(run_look_and_say(string, 50))



if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
