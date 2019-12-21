import utils
from aoc2019.int_code import IntCode

def translate_to_chars(ascii_vals):
    result = [chr(i) for i in ascii_vals]
    return ''.join(result)

def translate_to_ascii(chars):
    return [ord(c) for c in chars]

class SpringScript:

    def __init__(self, int_code_file, program_file):
        self.int_code = IntCode(int_code_file)
        self.program = utils.read_lines(program_file)

    def run(self):
        instructions = []
        for line in self.program:
            instructions.extend(translate_to_ascii(line + '\n'))
        result = self.int_code.run_program(instructions)
        last_output = result[-1]
        if last_output in range(0x110000):
            return translate_to_chars(result)
        return result[-1]
