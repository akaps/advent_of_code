import utils

def calculate_fuel(mass):
    return mass //3 - 2

def calculate_log_fuel(mass):
    total = 0
    current = calculate_fuel(mass)
    while current >= 0:
        total += current
        current = calculate_fuel(current)
    return total

def simple_fuel(mass_list):
    total = 0
    for mass in mass_list:
        total += calculate_fuel(mass)
    assert total == 3295539
    utils.pretty_print_answer(1, total)

def realistic_fuel(mass_list):
    total = 0
    for mass in mass_list:
        total += calculate_log_fuel(mass)
    assert total == 4940441
    utils.pretty_print_answer(2, total)

assert calculate_fuel(12) == 2
assert calculate_fuel(14) == 2
assert calculate_fuel(1969) == 654
assert calculate_fuel(100756) == 33583

assert calculate_log_fuel(14) == 2
assert calculate_log_fuel(1969) == 966
assert calculate_log_fuel(100756) == 50346

mass_list = [int(x) for x in utils.read_lines('input.txt')]
simple_fuel(mass_list)
realistic_fuel(mass_list)
