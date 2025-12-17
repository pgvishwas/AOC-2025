from aoc2015.utils.utils import read_input
import re
escape_pattern = r'\\(?:[nrtbfv\\\'"]|x[0-9a-fA-F]{2}|[0-7]{1,3})'


def star1() -> int:
    data = read_input()
    string_length=[]
    char_length =[]
    string_sum,char_sum = 0,0
    result =0
    for expression in data:
        string_length.append(len(expression))
        check_escape = re.findall(escape_pattern, expression)
        res =0
        if  check_escape:
            for vals in check_escape:
                res += len(vals)
        result += 2+res-len(check_escape)

    return result



def star2() -> int:
    data = read_input()
    total_encoded_len = 0
    total_original_len = 0

    for line in data:
        line = line.strip()
        original_len = len(line)

        # New string starts with:
        # 2 (for outer quotes)
        # + length of original string
        # + count of backslashes (each \ becomes \\)
        # + count of quotes (each " becomes \")
        encoded_len = original_len + 2 + line.count('\\') + line.count('"')

        total_original_len += original_len
        total_encoded_len += encoded_len

    return total_encoded_len - total_original_len


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
