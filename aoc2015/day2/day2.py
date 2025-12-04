from aoc2015.utils.utils import read_input


def star1() -> int:
    data = read_input()
    dimensions=[]
    for d in data:
        dimensions.append([int(x) for x in d.split('x')])
    required_wrapper = 0
    for vals in dimensions:
        l,w,h = vals
        surface_area = 2*((l*w)+(w*h)+(h*l))
        slack = min(l*w,w*h,h*l)
        required_wrapper += (surface_area+slack)

    # TODO: Implement star 1 solution
    return required_wrapper


def star2() -> int:
    data = read_input()
    # TODO: Implement star 2 solution
    dimensions = []
    for d in data:
        dimensions.append([int(x) for x in d.split('x')])
    required_wrapper = 0
    for vals in dimensions:
        l,w,h = vals
        vals.sort()
        min_one,min_two = vals[0],vals[1]
        perimeter = 2*(min_one+min_two)
        ribbon = l*w*h
        required_wrapper += (perimeter+ribbon)


    return required_wrapper


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
