from aoc2025.utils.utils import read_input

def count_zero_hits(commands, start=50, N=100):
    """
    Count how many times the dial points at 0 during or at the end of each rotation.
    commands: iterable of "Lk" / "Rk" strings
    start: starting dial position (0..N-1)
    N: dial size (100 here)
    Returns: (total_hits, final_position)
    """
    p = start % N
    total = 0
    for cmd in commands:
        cmd = cmd.strip()
        if not cmd:
            continue
        dir_char = cmd[0].upper()
        k = int(cmd[1:])
        # For a right rotation (increasing): hits when (p + t) % N == 0 -> t_first = (-p) % N
        # For a left rotation (decreasing): hits when (p - t) % N == 0 -> t_first = p % N
        if dir_char == 'R':
            dir_sign = 1
            t_first = (-p) % N
        elif dir_char == 'L':
            dir_sign = -1
            t_first = p % N
        else:
            raise ValueError(f"Bad command: {cmd}")
        # only t in 1..k count; treat t_first == 0 as N (i.e., next wrap)
        if t_first == 0:
            t_first = N

        if t_first <= k:
            hits = 1 + (k - t_first) // N
        else:
            hits = 0

        total += hits
        p = (p + dir_sign * k) % N

    return total

def star1() -> int:
    data = []
    input_data = read_input()
    for d in input_data:
        data.append(d.split('\n')[0])
    move_data = [[item[0], int(item[1:])] for item in data]
    pointer,password,safe_length = 50,0,100
    for moves in move_data:
        move_value = moves[1]%safe_length
        if moves[0]=='L':
            move_value = move_value*-1
        pointer+=move_value
        if pointer>=safe_length:
            pointer = pointer%safe_length
        elif pointer<0:
            pointer+=safe_length
        if pointer == 0:
            password+=1
    return password


def star2() -> int:
    data = []
    input_data = read_input()
    for d in input_data:
        data.append(d.split('\n')[0])
    safe_length = 100
    pointer = 50
    password = count_zero_hits(data,pointer,safe_length)
    return password


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
