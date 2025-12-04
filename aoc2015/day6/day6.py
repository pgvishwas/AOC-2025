from aoc2015.utils.utils import read_input
import numpy as np
import copy
def switch_lights(light_arr,row1,col1,row2,col2,to_switch):
    lights_array = copy.deepcopy(light_arr)
    for row in range(row1,row2+1):
        for col in range(col1,col2+1):
            if to_switch:
                if lights_array[row][col] == 0:
                    lights_array[row][col] = 1
            else:
                if lights_array[row][col] == 1:
                    lights_array[row][col] = 0
    return lights_array
def toggle_lights(light_arr,row1,col1,row2,col2):
    lights_array = copy.deepcopy(light_arr)
    for row in range(row1,row2+1):
        for col in range(col1,col2+1):
            if lights_array[row][col] == 0:
                lights_array[row][col] = 1
            else:
                lights_array[row][col] = 0
    return lights_array

def increase_switch_lights(light_arr,row1,col1,row2,col2,to_switch):
    lights_array = copy.deepcopy(light_arr)
    for row in range(row1, row2 + 1):
        for col in range(col1, col2 + 1):
            if to_switch:
                lights_array[row][col] += 1
            else:
                if lights_array[row][col] >= 1:
                    lights_array[row][col] -=1
    return lights_array
def increase_toggle_lights(light_arr,row1,col1,row2,col2):
    lights_array = copy.deepcopy(light_arr)
    for row in range(row1,row2+1):
        for col in range(col1,col2+1):
            lights_array[row][col] += 2
    return lights_array

def star1() -> int:
    data = read_input()
    lights = np.zeros((1000,1000),dtype=int)
    count_lit_light=0
    for instructions in data:
        switch_instructions = instructions.split(" ")
        if switch_instructions[0] == "turn":
            r1,c1,r2,c2 = int(switch_instructions[2].split(",")[0]) ,int(switch_instructions[2].split(",")[1]),int(switch_instructions[4].split(",")[0]),int(switch_instructions[4].split(",")[1])
            if switch_instructions[1] == "on":
                to_switch = True
            else:
                to_switch = False
            lights = switch_lights(lights,r1,c1,r2,c2,to_switch)
        else:
            r1, c1, r2, c2 = int(switch_instructions[1].split(",")[0]), int(switch_instructions[1].split(",")[1]), int(
                switch_instructions[3].split(",")[0]), int(switch_instructions[3].split(",")[1])
            lights = toggle_lights(lights,r1,c1,r2,c2)

    for i in range(1000):
        for j in range(1000):
            if lights[i][j] == 1:
                count_lit_light += 1


    return count_lit_light

def star2() -> int:
    data = read_input()
    lights = np.zeros((1000, 1000), dtype=int)
    count_lit_light = 0
    for instructions in data:
        switch_instructions = instructions.split(" ")
        if switch_instructions[0] == "turn":
            r1, c1, r2, c2 = int(switch_instructions[2].split(",")[0]), int(switch_instructions[2].split(",")[1]), int(
                switch_instructions[4].split(",")[0]), int(switch_instructions[4].split(",")[1])
            if switch_instructions[1] == "on":
                to_switch = True
            else:
                to_switch = False
            lights = increase_switch_lights(lights, r1, c1, r2, c2, to_switch)
        else:
            r1, c1, r2, c2 = int(switch_instructions[1].split(",")[0]), int(switch_instructions[1].split(",")[1]), int(
                switch_instructions[3].split(",")[0]), int(switch_instructions[3].split(",")[1])
            lights = increase_toggle_lights(lights, r1, c1, r2, c2)

    for i in range(1000):
        for j in range(1000):
            count_lit_light += lights[i][j]

    return count_lit_light


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
