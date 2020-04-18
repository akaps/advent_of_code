import re
import numpy as np
import utils

WIRE_INPUT_FORMAT = r'[a-z]{1,2}(?=$)'

class Wires:
    def __init__(self, file_name):
        self.registers = {}
        lines = utils.read_lines(file_name)
        self.run(lines)

    def inputs_defined(self, line):
        inputs = re.findall(WIRE_INPUT_FORMAT, line)
        print(inputs)
        for wire in inputs:
            if wire not in self.registers:
                return False
        return True

    def run(self, lines):
        while lines:
            next_generation = []
            while lines:
                next_line = lines.pop(0)
                try:
                    self.parse_line(next_line)
                except KeyError:
                    next_generation.append(next_line)
            lines = next_generation

    def parse_line(self, line):
        bitwise_op = r'^(\d+|\w+) (AND|OR) (\d+|\w+) -> (\w+)$'
        shift_op = r'^(\w+) (LSHIFT|RSHIFT) (\d+) -> (\w+)$'
        not_op = r'^NOT (\w+) -> (\w+)$'
        assignment_op = r'^(\d+|\w+) -> (\w+)$'
        if re.match(bitwise_op, line):
            self.do_bitwise_op(re.search(bitwise_op, line))
        elif re.match(shift_op, line):
            self.do_shift_op(re.search(shift_op, line))
        elif re.match(not_op, line):
            self.do_not_op(re.search(not_op, line))
        elif re.match(assignment_op, line):
            self.do_assignment_op(re.search(assignment_op, line))
        else:
            print('no match for {line}'.format(line=line))
            exit()

    def do_bitwise_op(self, vals):
        left, operator, right, store = vals.groups()
        if left.isdigit():
            left = np.uint16(int(left))
        else:
            left = self.registers[left]
        if operator == 'AND':
            self.registers[store] = np.uint16(left & self.registers[right])
        else:
            self.registers[store] = np.uint16(left | self.registers[right])

    def do_shift_op(self, vals):
        left, shift, val, store = vals.groups()
        if shift == 'LSHIFT':
            self.registers[store] = np.uint16(self.registers[left] << np.uint16(val))
        else:
            self.registers[store] = np.uint16(self.registers[left] >> np.uint16(val))

    def do_not_op(self, vals):
        val, store = vals.groups()
        self.registers[store] = ~self.registers[val]

    def do_assignment_op(self, vals):
        left, right = vals.groups()
        if left.isdigit():
            self.registers[right] = np.uint16(int(left))
        else:
            self.registers[right] = self.registers[left]

def main():
    problem = Wires('input.txt')
    utils.pretty_print_answer(1, problem.registers['a'])

if __name__ == '__main__':
    main()
