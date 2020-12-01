def input():
    input_file = open("input.txt", 'r')
    input_list = []
    for number in input_file:
        input_list.append(int(number))
    return input_list


def puzzle1():
    input_list = input()
    for item in input_list:
        for item1 in input_list:
            a = item
            b = item1
            if a != b and a + b == 2020:
                return a * b
            else:
                continue


def puzzle2():
    input_list = input()
    for item in input_list:
        for item1 in input_list:
            a = item
            b = item1
            if a != b and a + b != 2020:
                for item2 in input_list:
                    c = item2
                    if c != a and c !=b and a + b + c ==2020:
                        return a*b*c
            else:
                continue


print(puzzle1())
print(puzzle2())
