def boot_input():
    command_info = []
    with open("day8_input.txt", 'r') as input_file:
        for lines in input_file:
            lines.rstrip('\n')
            input = lines.split(' ')
            command = input[0]
            cmd_run_times = input[1].rstrip('\n')
            info = (command, int(cmd_run_times))
            command_info.append(info)
    return command_info


def run_instructions(data):
    executed = set()
    # acc_value = 5
    acc_value = 0
    line_number = 0

    while True:
        if line_number in executed:
            return acc_value, False

        cmd, run_count = data[line_number]
        executed.add(line_number)

        if cmd == 'acc':
            acc_value = acc_value + run_count
            line_number = line_number + 1

        elif cmd == 'jmp':
            line_number = line_number + run_count

        elif cmd == 'nop':
            line_number += 1


def part1(data):
    return run_instructions(data)


if __name__ == '__main__':
    boot_info = boot_input()
    print('Solution of puzzle 1 is', part1(boot_info))
