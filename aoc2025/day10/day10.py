from aoc2025.utils.utils import read_input
import re
import itertools
from collections import deque
from z3 import Int, Optimize, Sum, sat
def parse_line(line: str):
    """
    Parse one line of your actual input into:
      buttons: list[list[int]]
      target:  list[int]
    """
    # Buttons: sequences inside parentheses (...)
    buttons = [
        [int(x.strip()) for x in item.split(',')]
        for item in re.findall(r'\(([^)]+)\)', line)
    ]

    # Joltage target: single block inside {...}
    joltage_strs = re.findall(r'\{([^}]+)\}', line)
    if len(joltage_strs) != 1:
        raise ValueError(f"Expected exactly one joltage block in line: {line}")
    target = [int(x.strip()) for x in joltage_strs[0].split(',')]

    return buttons, target


def parse_input(lines):
    """
    lines: list[str]
    returns:
      all_buttons: list[list[list[int]]]  (per machine)
      all_targets: list[list[int]]        (per machine)
    """
    all_buttons = []
    all_targets = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        buttons, target = parse_line(line)
        all_buttons.append(buttons)
        all_targets.append(target)
    return all_buttons, all_targets
def min_presses_z3(buttons, target):
    """
    buttons: list[list[int]] e.g. [[0,3,5,6], [1,3,4,5], ...]
    target:  list[int]        e.g. [37,65,17,38,73,53,58]

    Returns: minimum total presses (int), or None if unsat.
    """
    k = len(target)   # number of counters
    n = len(buttons)  # number of buttons

    opt = Optimize()

    # Variables: x_j = how many times to press button j
    x = [Int(f"x_{j}") for j in range(n)]

    for j, btn in enumerate(buttons):
        # x_j >= 0
        opt.add(x[j] >= 0)

        # Optional upper bound: cannot help to press a button more than
        # the smallest target among counters it touches
        if btn:
            ub = min(target[i] for i in btn)
            opt.add(x[j] <= ub)
        else:
            # button affects nothing → force to 0
            opt.add(x[j] == 0)

    # Constraints: for each counter i, sum of contributions == target[i]
    for i in range(k):
        opt.add(
            Sum(
                x[j] for j, btn in enumerate(buttons) if i in btn
            ) == target[i]
        )

    total_presses = Sum(x)
    opt.minimize(total_presses)

    if opt.check() != sat:
        return None

    model = opt.model()
    return model.eval(total_presses).as_long()
def get_all_combinations(iterable):
    result = []
    for r in range(len(iterable) + 1):  # Iterate through lengths from 0 to len(iterable)
        for combination in itertools.combinations(iterable, r):
            result.append(combination)
    return result

def flip_switches(target_pattern,switches):
    length=len(target_pattern)
    flip = lambda x: '1' if x=='0' else '0'
    initial_pattern = ['0']*length
    for switching in switches:
        for pos in switching:
            initial_pattern[pos] = flip(initial_pattern[pos])
    initial_pattern = "".join(x for x in initial_pattern)
    return initial_pattern

def create_lights(pattern, switches):
    all_switch_combinations = get_all_combinations(switches)
    result_count = []
    for combination in all_switch_combinations:
        result_pattern = flip_switches(pattern, list(combination))
        if result_pattern == pattern:
            result_count.append(len(combination))

    return result_count

def star1() -> int:
    data = read_input()
    result_pattern,switch_order,joltage = [],[],[]
    checkEven = lambda x: '1' if x == "#" else '0'
    for d in data:
        #list_a_raw = re.findall(r'\[([^\]]+)\]', d)
        #list_b_raw = re.findall(r'\(([^)]+)\)', d)
        #list_b_clean = [[int(x.strip()) for x in item.split(',')] for item in re.findall(r'\(([^)]+)\)', d)]
        #list_c_raw = re.findall(r'\{([^{]+)\}', d)
        result_pattern.append(["".join([checkEven(y) for x in re.findall(r'\[([^\]]+)\]', d) for y in x])])
        switch_order.append([[int(x.strip()) for x in item.split(',')] for item in re.findall(r'\(([^)]+)\)', d)])
        joltage.append(re.findall(r'\{([^{]+)\}', d))

    finalswitch_count = 0
    for i in range(len(joltage)):
        pattern = joltage[i][0]
        swtiches = switch_order[i]
        value = create_lights(pattern,swtiches)
        finalswitch_count+=min(value)
    return finalswitch_count

    # TODO: Implement star 1 solution
    return 0


def star2() -> int:
    lines = read_input(test=False)  # or your own file loader
    all_buttons, all_targets = parse_input(lines)

    total = 0
    for buttons, target in zip(all_buttons, all_targets):
        presses = min_presses_z3(buttons, target)
        if presses is None:
            raise RuntimeError(f"No solution for machine with target {target}")
        total += presses

    return total




if __name__ == "__main__":
    #print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
