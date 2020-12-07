def input_data():
    data = []
    group = []
    with open('day6_input.txt', 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line == '':
                data.append(group)
                group = []
            else:
                group.append(set(line))
            line = file.readline()
        data.append(group)
    return data


def puzzle1():
    onboarding_data = input_data()
    sum_ = 0
    for group in onboarding_data:
        answers = set.union(*group)
        answer_count = len(answers)
        sum_ = sum_ + answer_count
    return sum_


def puzzle2():
    onboarding_data = input_data()
    sum_ = 0
    for group in onboarding_data:
        answers = set.intersection(*group)
        answer_count = len(answers)
        sum_ = sum_ + answer_count
    return sum_


if __name__ == '__main__':
    print('Solution of puzzle 1 is', puzzle1())
    print('Solution of puzzle 2 is', puzzle2())
