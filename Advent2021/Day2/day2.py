import itertools, math


def input_data():
    with open("Advent2021/Day2/day2_input.txt", 'r') as input_file:
        input_list = []
        for lines in input_file:
            elements = lines.split(' ')
            instruction = elements[0]
            count = int(elements[1].replace('\n', ''))
            new_list = [instruction, count]
            input_list.append(new_list)
        return input_list

def cal_position(input_list):

    depth = 0
    horizontal_position = 0

    for instructions_ in input_list:
        if instructions_[0] == 'forward':
            horizontal_position = horizontal_position + instructions_[1]
        if instructions_[0] == 'up':
            depth = depth - instructions_[1]
        if instructions_[0] == 'down':
            depth = depth + instructions_[1]

    return horizontal_position * depth

def puzzle1():
    input_list = input_data()    
    return cal_position(input_list)  

def cal_position_puzzle2(input_list):
    
    depth = 0
    horizontal_position = 0
    aim = 0

    for instructions_ in input_list:
        if instructions_[0] == 'forward':
            horizontal_position = horizontal_position + instructions_[1]
            depth = depth + (instructions_[1] * aim)
        if instructions_[0] == 'up':
            aim = aim - instructions_[1]
        if instructions_[0] == 'down':
            aim = aim + instructions_[1]
        # print(horizontal_position, depth)

    return horizontal_position * depth

def puzzle2():
    
    input_list = input_data()   
    return cal_position_puzzle2(input_list)


if __name__ == '__main__':
    print(f"Answer for puzzle 1: {puzzle1()}")
    print(f"Answer for puzzle 2: {puzzle2()}")
