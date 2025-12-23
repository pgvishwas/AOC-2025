from aoc2025.utils.utils import read_input
import re

# The 6 shapes provided in the input and their calculated areas (# counts)
SHAPE_AREAS = [5, 6, 7, 7, 7, 7]


def solve_christmas_packing(data):
    lines = data
    fit_count = 0

    for line in lines:
        # Extract width, height, and the 6 quantities
        # Example format: 50x45: 40 43 39 39 40 39
        match = re.match(r"(\d+)x(\d+):\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", line)

        if match:
            width = int(match.group(1))
            height = int(match.group(2))
            quantities = [int(match.group(i)) for i in range(3, 9)]

            # Calculate total available area
            grid_area = width * height

            # Calculate total required area for the presents
            presents_area = sum(q * a for q, a in zip(quantities, SHAPE_AREAS))

            # Check if it fits
            if presents_area <= grid_area:
                fit_count += 1

    return fit_count


def star1() -> int:
    data = read_input(test = False)



def star2() -> int:
    data = read_input()
    # TODO: Implement star 2 solution
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
