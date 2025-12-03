from aoc2025.utils.utils import read_input


def get_max_subsequence_value(s, k=12):
    """
    Finds the largest number of length k from string s
    preserving relative order of digits.
    """
    # Calculate how many characters we can afford to skip/delete
    drop_count = len(s) - k

    # If the string is too short, return 0 or handle error
    if drop_count < 0:
        return 0

    stack = []

    for digit in s:
        # Greedy Logic:
        # If current digit > top of stack, AND we have drops left,
        # pop the stack to make the number bigger.
        while drop_count > 0 and stack and stack[-1] < digit:
            stack.pop()
            drop_count -= 1
        stack.append(digit)

    # Take exactly k digits and convert to integer
    # (stack might be longer if we didn't use all drops)
    max_subsequence_str = "".join(stack[:k])
    return int(max_subsequence_str)


def calculate_total_max_sum(string_list):
    total_sum = 0

    for s in string_list:
        # 1. Find max number for this specific string
        max_num = get_max_subsequence_value(s, 12)

        # 2. Add to total
        total_sum += max_num

        # Optional: Print progress
        print(f"String: {s} -> Max: {max_num}")

    return total_sum

def star1() -> int:
    data = read_input()
    #joltage = [int(x) for x in data]
    max_joltage=0
    for jolts in data:
        max_value = 0
        position=0
        length = len(jolts)
        for j in range(0,length-1):
            if int(jolts[j]) > max_value:
                max_value = int(jolts[j])
                position = j
        second_max=0
        for i in range(position+1,length):
            if int(jolts[i]) > second_max:
                second_max = int(jolts[i])
        max_joltage += int(str(max_value)+str(second_max))
    # TODO: Implement star 1 solution
    return max_joltage


def star2() -> int:
    data = read_input()
    target_length =12
    result = int(calculate_total_max_sum(data))
    # TODO: Implement star 2 solution
    return result


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
