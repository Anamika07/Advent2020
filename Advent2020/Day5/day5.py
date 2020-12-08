def input_data():
    with open("day5_input.txt", 'r') as input_file:
        seat_ids = []
        for lines in input_file:
            seat_ids.append(lines.replace('\n', ''))
        return seat_ids


def get_row(row):
    row_ = []
    start = 0
    end = 127
    for a in row:
        if a == 'F':
            start = start
            end = int((start + end) / 2)
            row_ = [start, end]
        elif a == 'B':
            start = int((start + end) / 2) + 1
            end = end
            row_ = [start, end]
    return row_[0]


def get_col(col):
    start = 0
    end = 7
    col_ = []
    for a in col:
        if a == 'L':
            start = start
            end = int((start + end) / 2)
            col_ = [start, end]
        elif a == 'R':
            start = int((start + end) / 2) + 1
            end = end
            col_ = [start, end]
    return col_[0]


def get_seat_info():
    p = input_data()
    seats = []
    for a in p:
        r = get_row(a[:7])
        c = get_col(a[7:])
        seat = (r * 8) + c
        seats.append(seat)
    return seats


// why find_your_seat() is needed ? Could max be used ? 

def find_your_seat():
    a = sorted(get_seat_info())
    for seat in range(a[0], a[-1]+1):
        if seat not in a:
            return seat
    # return [seat for seat in range(a[0], a[-1] + 1) if seat not in a]


if __name__ == '__main__':
    print(f"Solution for Puzzle 1: {max(get_seat_info())}")
    print(f"Solution for Puzzle 2: {find_your_seat()}")
