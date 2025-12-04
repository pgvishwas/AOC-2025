from aoc2015.utils.utils import read_input

directions = {
    "^": (1, 0),
    "v": (-1, 0),
    "<": (0, 1),
    ">": (0, -1)
}
def star1() -> int:
    data = read_input()[0]
    starting_point = (0, 0)
    houses = {starting_point}
    for move in data:
        dx,dy = directions[move]
        starting_point = (starting_point[0] + dx, starting_point[1] + dy)
        houses.add(starting_point)
    return len(houses)




def star2() -> int:
    data = read_input()[0]
    santa_road = data[::2]
    robot_santa_road = data[1::2]
    print(santa_road)
    print(robot_santa_road)
    santa_starting_point = (0, 0)
    robot_starting_point = (0, 0)
    santa_houses = {santa_starting_point}
    robot_santa_houses = {robot_starting_point}
    for move in santa_road:
        dx,dy = directions[move]
        santa_starting_point = (santa_starting_point[0] + dx, santa_starting_point[1] + dy)
        santa_houses.add(santa_starting_point)
    for move in robot_santa_road:
        dx,dy = directions[move]
        robot_starting_point = (robot_starting_point[0] + dx, robot_starting_point[1] + dy)
        robot_santa_houses.add(robot_starting_point)
    return len(robot_santa_houses | santa_houses)



if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
