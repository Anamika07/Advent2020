
def input_data():
    with open("day2_input.txt", 'r') as input_file:
        input_list = []
        for lines in input_file:
            element_of_password_check = lines.split(' ')
            password = element_of_password_check[2].replace('\n', '')
            char_check = element_of_password_check[1].replace(':', '')
            char_limit = element_of_password_check[0].split('-')
            new_list = [password, char_check, char_limit]
            input_list.append(new_list)
        return input_list


def puzzle1():
    input_list = input_data()
    num_of_valid_pass = 0
    for item in input_list:
        password = item[0]
        char_check = item[1]
        char_limit = item[2]
        lower_limit = int(char_limit[0])
        upper_limit = int(char_limit[1])
        # print(password, char_check, lower_limit, upper_limit)
        count = password.count(char_check)
        if lower_limit <= count <= upper_limit:
            num_of_valid_pass = num_of_valid_pass + 1
    return num_of_valid_pass


def puzzle2():
    input_list = input_data()
    num_of_valid_pass = 0
    for item in input_list:
        password = item[0]
        char_check = item[1]
        char_limit = item[2]
        lower_limit = int(char_limit[0])
        upper_limit = int(char_limit[1])
        try:
            character_ll = password[lower_limit - 1]
            character_ul = password[upper_limit - 1]
            if character_ll == char_check or character_ul == char_check:
                if character_ll != character_ul:
                    num_of_valid_pass = num_of_valid_pass + 1
        except:
            print("one of the character was Out of bound")
    return num_of_valid_pass


print(f"Solution for Puzzle 1: {puzzle1()}")
print(f"Solution for Puzzle 2: {puzzle2()}")
