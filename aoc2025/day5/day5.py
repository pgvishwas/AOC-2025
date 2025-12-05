from aoc2025.utils.utils import read_input
from itertools import groupby

def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]
    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged[-1]
        if current_start <= last_end + 1:
            new_end = max(last_end, current_end)
            merged[-1] = (last_start, new_end)
        else:
            merged.append((current_start, current_end))
    return merged

def star1() -> int:
    data = read_input()
    ingredient_lists = [list(g) for k, g in groupby(data, key=bool) if k]
    ingredient_ids,ingredients = ingredient_lists[0],ingredient_lists[1]
    ranges,ingredient_list=[],[]
    for ids in ingredient_ids:
        data = ids.split('-')
        ranges.append((int(data[0]), int(data[1])))
    merged = merge_ranges(ranges)
    ingredient_list = [int(x) for x in ingredients]
    fresh_ingredient=0
    for ing in ingredient_list:
        for range in merged:
            if range[0] <= ing <= range[1]:
                fresh_ingredient+=1
                break
    return fresh_ingredient

def star2() -> int:
    data = read_input()
    ingredient_ids = [list(g) for k, g in groupby(data, key=bool) if k][0]
    ranges,fresh_ingredients = [],0
    for ids in ingredient_ids:
        data = ids.split('-')
        ranges.append((int(data[0]), int(data[1])))
    merged = merge_ranges(ranges)
    for ids in merged:
        fresh_ingredients+=(ids[1]-ids[0]+1)
    return fresh_ingredients

if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
