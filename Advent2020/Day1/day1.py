import itertools, math


def input_data():
    with open("Advent2020/Day1/day1_input.txt", 'r') as input_file:
        input_list = []
        for number in input_file:
            input_list.append(int(number))
        return input_list


def puzzle(n):
    input_list = input_data()
    for num in itertools.combinations(input_list, n):
        if sum(num) == 2020:
            return math.prod(num)


if __name__ == '__main__':
    print(f"Answer for puzzle 1: {puzzle(2)}")
    print(f"Answer for puzzle 2: {puzzle(3)}")
