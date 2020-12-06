def input_data():
    with open("day4_input.txt", 'r') as input_file:
        passengers_data = []
        raw_data = []
        passenger_data = []
        for line in input_file:
            raw_data.append(line)
        for item in raw_data:
            if item != '\n':
                if item.find(' '):
                    items = item.split(' ')
                    for a in items:
                        a = a.rstrip('\n')
                        if a.find(":"):
                            a = a.split(':')
                        passenger_data.append(a)
                else:
                    passenger_data.append(item.rstrip('\n'))
            else:
                passengers_data.append(dict(passenger_data))
                passenger_data = []
        if passenger_data:
            passengers_data.append(dict(passenger_data))
        return passengers_data


def birth_validation(byr):
    return 1920 <= int(byr) <= 2002


def issue_year_validation(iyr):
    return 2010 <= int(iyr) <= 2020


def exp_year(eyr):
    return 2020 <= int(eyr) <= 2030


def hgt_validation(hgt):
    if hgt.find('cm') != -1:
        hgt = hgt.rstrip('cm')
        return 150 <= int(hgt) <= 193
    if hgt.find('in'):
        hgt = hgt.rstrip('in')
        return 59 <= int(hgt) <= 76


def hcl_validation(hcl):
    return hcl[0] == '#' and len(hcl) == 7


def passport_id_validation(pid):
    return len(pid) == 9


def ecl_validation(ecl):
    matches = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in matches


def puz1():
    count = 0
    matches = {'iyr', 'eyr', 'hgt', 'hcl', 'byr', 'ecl', 'pid'}
    valid_participants = []
    passengers_info = input_data()
    for passenger in passengers_info:
        data_to_match = passenger.keys()
        if len(matches - set(data_to_match)) == 0:
            valid_participants.append(passenger)
            count = count + 1
    return count, valid_participants


def puz2():
    valid_user = puz1()[1]
    count = 0
    for p in valid_user:
        if birth_validation(p['byr']) and issue_year_validation(p['iyr']):
            if exp_year(p['eyr']) and hgt_validation(p['hgt']):
                if hcl_validation(p['hcl']) and passport_id_validation(p['pid']) and ecl_validation(p['ecl']):
                    count = count + 1
    return count


if __name__ == '__main__':
    print(f"Solution for Puzzle 1: {puz1()[0]}")
    print(f"Solution for Puzzle 1: {puz2()}")
