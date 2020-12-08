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


def puzzle1(onboarding_data):
    sum_ = 0
    for group in onboarding_data:
        sum_ = sum_ + len(set.union(*group))
    return sum_


def puzzle2(onboarding_data):
    sum_ = 0
    for group in onboarding_data:
        sum_ = sum_ + len(set.intersection(*group))
    return sum_


if __name__ == '__main__':
    onboarding_data = input_data()
    print('Solution of puzzle 1 is', puzzle1(onboarding_data))
    print('Solution of puzzle 2 is', puzzle2(onboarding_data))
