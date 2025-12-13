from aoc2015.utils.utils import read_input

OPERATORS = ['AND','OR','NOT','RSHIFT','LSHIFT']
def get_val(item, wires):
    if item.isdigit():
        return int(item)
    return wires.get(item)

def star1() -> int:
    data = read_input()
    value = []
    digit = lambda x : int(x) if x.isdigit() else wires[x]
    for v in data:
        value.append(v.split(" "))
    wires = {}

    # Loop until all instructions are resolved
    # Note: This checks if we have a signal for every unique wire found in "-> target"
    while True:
        progress_made = False  # Detect infinite loops

        for val in value:
            target_wire = val[-1]

            # If we already know this wire, skip it
            if target_wire in wires:
                continue

            # 1. Handle Simple Assignment: "123 -> x" or "lx -> x"
            # Structure: [Source, "->", Target] (Length 3)
            if len(val) == 3:
                v = get_val(val[0], wires)
                if v is not None:
                    wires[target_wire] = v
                    progress_made = True

            # 2. Handle NOT: "NOT x -> y"
            # Structure: ["NOT", Source, "->", Target] (Length 4)
            elif len(val) == 4:
                v = get_val(val[1], wires)
                if v is not None:
                    wires[target_wire] = ~v & 65535
                    progress_made = True

            # 3. Handle Gates: "x AND y -> z", "x LSHIFT 2 -> z"
            # Structure: [Left, Op, Right, "->", Target] (Length 5)
            elif len(val) == 5:
                left = get_val(val[0], wires)
                right = get_val(val[2], wires)
                op = val[1]

                # CHECK FOR NONE, NOT FALSE (Fixes the "0" bug)
                if left is not None and right is not None:
                    res = 0
                    if op == 'AND':
                        res = left & right
                    elif op == 'OR':
                        res = left | right
                    elif op == 'LSHIFT':
                        res = left << right
                    elif op == 'RSHIFT':
                        res = left >> right

                    wires[target_wire] = res & 65535  # Ensure 16-bit safety
                    progress_made = True

        # Break if we solve everything (or get stuck)
        # Checking if 'a' is found is usually enough for AoC
        if 'a' in wires:
            break

   # print(wires.get('a'))





    # TODO: Implement star 1 solution
    return wires.get('a')


def star2(part_a) -> int:
    data = read_input()
    value = []
    digit = lambda x: int(x) if x.isdigit() else wires[x]
    for v in data:
        value.append(v.split(" "))
    wires = {'b': part_a}
    while True:
        progress_made = False  # Detect infinite loops

        for val in value:
            target_wire = val[-1]

            # If we already know this wire, skip it
            if target_wire in wires:
                continue

            # 1. Handle Simple Assignment: "123 -> x" or "lx -> x"
            # Structure: [Source, "->", Target] (Length 3)
            if len(val) == 3:
                v = get_val(val[0], wires)
                if v is not None:
                    wires[target_wire] = v
                    progress_made = True

            # 2. Handle NOT: "NOT x -> y"
            # Structure: ["NOT", Source, "->", Target] (Length 4)
            elif len(val) == 4:
                v = get_val(val[1], wires)
                if v is not None:
                    wires[target_wire] = ~v & 65535
                    progress_made = True

            # 3. Handle Gates: "x AND y -> z", "x LSHIFT 2 -> z"
            # Structure: [Left, Op, Right, "->", Target] (Length 5)
            elif len(val) == 5:
                left = get_val(val[0], wires)
                right = get_val(val[2], wires)
                op = val[1]

                # CHECK FOR NONE, NOT FALSE (Fixes the "0" bug)
                if left is not None and right is not None:
                    res = 0
                    if op == 'AND':
                        res = left & right
                    elif op == 'OR':
                        res = left | right
                    elif op == 'LSHIFT':
                        res = left << right
                    elif op == 'RSHIFT':
                        res = left >> right

                    wires[target_wire] = res & 65535  # Ensure 16-bit safety
                    progress_made = True

        # Break if we solve everything (or get stuck)
        # Checking if 'a' is found is usually enough for AoC
        if 'a' in wires:
            break
    return wires.get('a')



if __name__ == "__main__":
    part1_a = star1()
    part2_a = star2(part1_a)
    print(f"Star 1: {star1()}")
    print(f"Star 2: {part2_a}")
