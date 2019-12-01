#import utils #TODO: import utils for pretty print

def calculate_fuel(mass):
    return mass //3 - 2

def calculate_log_fuel(mass):
    total = 0
    current = calculate_fuel(mass)
    while current >= 0:
        total += current
        current = calculate_fuel(current)
    return total

def part_1(mass_list):
    total = 0
    for mass in mass_list:
        total += calculate_fuel(int(mass))

    #utils.pretty_print_answer(1, total)
    assert total == 3295539
    print('part 1: {ans}'.format(ans=total))

def part_2(mass_list):
    total = 0
    for mass in mass_list:
        total += calculate_log_fuel(int(mass))

    print('part 2: {ans}'.format(ans=total))

file = open('input.txt', 'r')
mass_list = file.readlines()
file.close()

part_1(mass_list)

assert calculate_log_fuel(14) == 2
assert calculate_log_fuel(1969) == 966
assert calculate_log_fuel(100756) == 50346

part_2(mass_list)
