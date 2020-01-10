import re
from aoc2019.int_code import IntCode
import aoc2019.springscript as springscript

NEWLINE = '\n'
EXIT = 'exit'
SAVE = 'save'
LOAD = 'load'
SAVE_FILE = 'state.txt'
INPUT_FILE = 'input.txt'

COMPUTER = IntCode('input.txt')

PROGRAM = COMPUTER.load_program()
RESULT = PROGRAM.send(None)
while isinstance(RESULT, list):
    input_string = input(springscript.translate_to_chars(RESULT) + NEWLINE)
    if input_string == EXIT:
        break
    input_string += NEWLINE
    for char in input_string:
        RESULT = PROGRAM.send(ord(char))
FILE = open('answer_pt_1.txt', 'w')
FILE.write(springscript.translate_to_chars(RESULT))
FILE.close()
