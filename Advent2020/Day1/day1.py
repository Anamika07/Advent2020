
def input_data():
    with open("Advent2020/Day1/day1_input.txt", 'r') as input_file:
        input_list = []
        for number in input_file:
            input_list.append(int(number))
        return input_list


def puzzle1():
    input_list = input_data()
    for a in input_list:
        for b in input_list:
            if a != b and a + b == 2020:
                return f"Answer for puzzle one {a * b}"
            else:
                continue


def puzzle2():
    input_list = input_data()
    for a in input_list:
        for b in input_list:
            if a != b and a + b != 2020:
                for c in input_list:
                    if c != a and c != b and a + b + c == 2020:
                        return f"Answer for puzzle one {a * b * c}"
            else:
                continue


print(puzzle1())
print(puzzle2())
