import utils
from aoc2019.int_code import IntCode

NEWLINE = '\n'
EXIT = 'exit\n'

def main():
    program = IntCode('input.txt').load_program()
    output = program.send(None)
    input_string = None
    while input_string != EXIT:
        input_string = input(utils.translate_to_chars(output) + NEWLINE)
        input_string += NEWLINE
        try:
            for char in input_string:
                output = program.send(ord(char))
        except StopIteration:
            break
    file = open('answer_pt_1.txt', 'w')
    file.write(utils.translate_to_chars(output))
    file.close()

if __name__ == '__main__':
    main()
