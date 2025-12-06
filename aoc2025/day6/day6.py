from aoc2025.utils.utils import read_input
from itertools import zip_longest,groupby


def star1() -> int:
    lines = read_input
    columns = list(zip_longest(*lines, fillvalue=' '))
    problems = []
    current_problem_chars = []
    for col in columns:
        # Check if the entire column is spaces (the separator)
        is_separator = all(char == ' ' for char in col)
        if is_separator:
            # If we hit a separator and have data buffered, save it
            if current_problem_chars:
                problems.append(current_problem_chars)
                current_problem_chars = []
        else:
            # If not a separator, add this column to the current problem
            current_problem_chars.append(col)
    # Capture the final problem if the line didn't end with spaces
    if current_problem_chars:
        problems.append(current_problem_chars)
    # 4. Process each isolated problem block
    results = []
    for p_cols in problems:
        # p_cols is a list of tuples (columns). We need to re-assemble text.
        # Transpose BACK to get readable rows for this specific problem block
        p_rows = [''.join(row).strip() for row in zip(*p_cols)]
        # Filter out empty strings effectively
        content = [x for x in p_rows if x]
        # Based on your description: last item is operator, rest are numbers
        operator = content[-1]
        numbers = [int(n) for n in content[:-1]]
        # Calculate
        if operator == '+':
            res = sum(numbers)
        elif operator == '*':
            res = 1
            for n in numbers: res *= n
        # Add other operators as needed
        results.append(res)
    final_result = 0
    for values in results:
        final_result += values
    return final_result


def star2() -> int:
    data,operators = read_input()[:-1], read_input()[-1]
    data = list(zip_longest(*data, fillvalue=' '))
    ceph_operator = [list(g) for is_sep, g in groupby(operators, key=lambda x: all(c == ' ' for c in x)) if not is_sep]
    ceph_operator = [x[0] for x in reversed(ceph_operator)]
    ceph_data = [list(g) for is_sep, g in groupby(data, key=lambda x: all(c == ' ' for c in x)) if not is_sep]
    #reverse_ceph_list = [list(reversed(k)) for k in reversed(ceph_data)]
    reverse_ceph_list = [k[::-1] for k in ceph_data[::-1]]
    number_list,result_arr=[],[]
    for nums in reverse_ceph_list:
        num = [''.join(t).strip() for t in nums]
        number_list.append([int(n) for n in num])
    for i in range(len(number_list)):
        if ceph_operator[i] == '+':
            res = sum(number_list[i])
        else:
            res = 1
            for n in number_list[i]: res *= n
        result_arr.append(res)
    cephalopod_result = sum(result_arr)
    return cephalopod_result




    # TODO: Implement star 2 solution
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
