import utils
from aoc2019.int_code import IntCode

NEWLINE = '\n'
EXIT = 'exit'

def main():
    program = IntCode('input.txt').load_program()
    output = program.send(None)
    input_string = None
    while input_string != EXIT:
        input_string = input(utils.translate_to_chars(output) + NEWLINE)
        try:
            for char in input_string + NEWLINE:
                output = program.send(ord(char))
        except StopIteration:
            break

if __name__ == '__main__':
    main()
