import utils
import re

CPY = r'cpy ([abcd]|\d+) ([abcd])'
INC = r'inc ([abcd])'
DEC = r'dec ([abcd])'
JNZ = r'jnz ([abcd]|\d+) (-?\d+)'

class Assembunny:
    def __init__(self, file_name):
        self.instructions = utils.read_lines(file_name)
        self.reset()

    def reset(self):
        self.registers = {
            'a' : 0,
            'b' : 0,
            'c' : 0,
            'd' : 0
        }
        self.instruction_pointer = 0

    def cpy(self, value, destination):
        if value.isnumeric():
            self.registers[destination] = int(value)
        else:
            self.registers[destination] = self.registers[value]

    def inc(self, destination):
        self.registers[destination] += 1

    def dec(self, destination):
        self.registers[destination] -= 1

    def jnz(self, value, offset):
        offset = int(offset)
        if value.isnumeric():
            self.jnz_for_value(int(value), offset)
        else:
            self.jnz_for_value(self.registers[value], offset)

    def jnz_for_value(self, value, offset):
        if value != 0:
            self.instruction_pointer += offset
        else:
            self.instruction_pointer += 1

    def run(self, debug=False):
        while self.instruction_pointer < len(self.instructions):
            self.step(debug)

    def step(self, debug=False):
        next_line = self.instructions[self.instruction_pointer]
        if debug:
            print(next_line)
        if re.match(JNZ, next_line):
            value, offset = re.match(JNZ, next_line).groups()
            self.jnz(value, offset)
        else:
            if re.match(CPY, next_line):
                value, destination = re.match(CPY, next_line).groups()
                self.cpy(value, destination)
            elif re.match(INC, next_line):
                destination = re.match(INC, next_line).groups()[0]
                self.inc(destination)
            elif re.match(DEC, next_line):
                destination = re.match(DEC, next_line).groups()[0]
                self.dec(destination)
            else:
                assert False, 'unsupported line {line}'.format(line=next_line)
            self.instruction_pointer += 1
        if debug:
            print(self.registers, self.instruction_pointer)

def main():
    sample = Assembunny('sample.txt')
    sample.run()
    assert sample.registers['a'] == 42
    problem = Assembunny('input.txt')
    problem.run()
    utils.pretty_print_answer(1, problem.registers['a'])
    problem.reset()
    problem.registers['c'] = 1
    problem.run()
    utils.pretty_print_answer(2, problem.registers['a'])

if __name__ == "__main__":
    main()