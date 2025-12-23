from aoc2015.utils.utils import read_input
import json
def extract_numbers(obj):
    nums = []
    if isinstance(obj, int):
        nums.append(obj)
    elif isinstance(obj, list):
        for item in obj:
            nums.extend(extract_numbers(item))
    elif isinstance(obj, dict):
        for value in obj.values():
            nums.extend(extract_numbers(value))
    return nums
def sum_numbers(obj):
    # If it's an int, count it
    if isinstance(obj, int):
        return obj

    # If it's a list, sum all elements
    if isinstance(obj, list):
        return sum(sum_numbers(x) for x in obj)

    # If it's a dict, ignore it completely if any value is "red"
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(sum_numbers(v) for v in obj.values())

    # Ignore everything else (strings, etc.)
    return 0
def star1() -> int:
    data = read_input()
    input_data = data[0]
    value = json.loads(input_data)
    numbers = extract_numbers(value)
    return sum(numbers)



def star2() -> int:
    data = read_input()
    input_data = json.loads(data[0])
    result = sum_numbers(input_data)
    return result



if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
