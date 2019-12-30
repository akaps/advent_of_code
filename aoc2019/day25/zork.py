import re
from int_code import IntCode, MissingInputError

NEWLINE = '\n'
EXIT = 'exit'
SAVE = 'save'
LOAD = 'load'
SAVE_FILE = 'state.txt'
INPUT_FILE = 'input.txt'

def translate_to_chars(ascii_vals):
    result = [chr(i) for i in ascii_vals]
    return ''.join(result)

def translate_to_ascii(chars):
    return [ord(c) for c in chars]

def save(file_name):
    file = open(file_name, 'w')
    file.write(','.join([str(i) for i in PROBLEM.registers]))
    file.write(NEWLINE)
    file.write(str(PROBLEM.instruction_pointer))
    file.write(NEWLINE)
    file.write(str(PROBLEM.relative_base))
    file.write(NEWLINE)
    file.close()

def load(computer, file_name):
    file = open(file_name, 'r')
    registers, ip, relative_base = file.readlines()
    file.close()
    computer.registers = [int(x) for x in re.split(r',', registers.strip())]
    computer.instruction_pointer = int(ip) - 3
    computer.relative_base = int(relative_base)
    computer.output = []

PROBLEM = IntCode('input.txt')

input_string = None
input_list = []
while input_string != EXIT:
    try:
        print(PROBLEM.run_program(input_list))
    except MissingInputError:
        result = PROBLEM.output
        PROBLEM.output = []
        input_string = input(translate_to_chars(result))
        if input_string == SAVE:
            save(SAVE_FILE)
            input_list = []
            print('save handled. Still expecting Zork commands')
        elif input_string == LOAD:
            load(PROBLEM, SAVE_FILE)
            input_list = []
            continue
        else:
            input_list = translate_to_ascii(input_string + NEWLINE)
