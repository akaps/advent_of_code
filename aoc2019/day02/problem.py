import re
import utils

ADD = 1
MULTIPLY = 2
STOP = 99

def run_program(registers):
    ip = 0
    while registers[ip] != STOP:
        next_instr = registers[ip]
        left = registers[ip + 1]
        right = registers[ip + 2]
        store = registers[ip + 3]
        if next_instr == ADD:
            registers[store] = registers[left] + registers[right]
        elif next_instr == MULTIPLY:
            registers[store] = registers[left] * registers[right]
        ip += 4
    return registers[0]

def solve_for_answer(registers):
    for noun in range(100):
        for verb in range(100):
            candidate = [x for x in registers]
            candidate[1] = noun
            candidate[2] = verb
            if run_program(candidate) == 19690720:
                return 100 * noun + verb
    return -1

def initialize(input_file):
    file = open(input_file, 'r')
    registers = [int(x) for x in re.split(r',', file.readline().strip())]
    file.close()
    return registers

REGISTERS = initialize('input.txt')
REGISTERS[1] = 12
REGISTERS[2] = 2
ANSWER = run_program(REGISTERS)
utils.pretty_print_answer(1, ANSWER)

REGISTERS = initialize('input.txt')
ANSWER = solve_for_answer(REGISTERS)
utils.pretty_print_answer(2, ANSWER)
