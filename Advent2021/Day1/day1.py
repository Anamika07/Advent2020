import itertools, math


def input_data():
    with open("Advent2021/Day1/day1_input.txt", 'r') as input_file:
        input_list = []
        for number in input_file:
            input_list.append(int(number))
        return input_list

def cal_measurements(input_list):
    measurements = 0
    for i in range(len(input_list) - 1):
        if input_list[i]< input_list[i + 1]:
            measurements = measurements + 1
    return measurements

def puzzle1():
    input_list = input_data()    
    return cal_measurements(input_list)  

def puzzle2():
    
    input_list = input_data()   
    new_list = []   
    
    for i in range(len(input_list) - 2):
        item = input_list[i] + input_list[i+1] + input_list[i+2]
        new_list.append(item)

    return cal_measurements(new_list) 


if __name__ == '__main__':
    print(f"Answer for puzzle 1: {puzzle1()}")
    print(f"Answer for puzzle 2: {puzzle2()}")
