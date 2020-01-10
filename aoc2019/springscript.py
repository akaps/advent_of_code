import utils
from aoc2019.int_code import IntCode

NEWLINE = '\n'

class SpringScript:

    def __init__(self, computer_file, program_file):
        self.computer = IntCode(computer_file)
        self.program = utils.read_lines(program_file)

    def run(self):
        program = self.computer.load_program()
        program.send(None)
        result = None
        for line in self.program:
            for char in line:
                program.send(ord(char))
            result = program.send(ord(NEWLINE))
        last_output = result[-1]
        if last_output in range(0x110000):
            return utils.translate_to_chars(result)
        return last_output
