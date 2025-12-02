from aoc2025.utils.utils import read_input

# This could be optimized so much but works... glad there are no massive ranges
def star1() -> int:
    # data = read_input(split=True, split_by=",", test=True)
    data = read_input(split=True, split_by=",")
    ids = []
    for d in data:
        start, end = d.split("-")
        # print(start, end)
        for n in range(int(start), int(end) + 1):
            s = str(n)
            if len(s) % 2 == 0:
                if s[: len(s)//2] == s[len(s)//2:]:
                    ids.append(n)
                
    return sum(ids)

# Glad it still works here. Triple for loop never hurt no one...
def star2() -> int:
    # data = read_input(split=True, split_by=",", test=True)
    data = read_input(split=True, split_by=",")
    ids = []
    for d in data:
        start, end = d.split("-")
        for n in range(int(start), int(end) + 1):
            s = str(n)
            l = len(s)
            for i in range(1, l):
                if l % i == 0:
                    part = s[:i]
                    if part * (l // i) == s:
                        ids.append(n)
                        break

    return sum(ids)


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
