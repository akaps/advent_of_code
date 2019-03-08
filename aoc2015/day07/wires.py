import re
import numpy as np
import utils

class Wires:
    def __init__(self, file_name):
        self.registers = {}
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()
        self.run(lines)

    def run(self, lines):
        for line in lines:
            self.parse_line(line)

    def parse_line(self, line):
        bitwise_op = r'^(\w+) (AND|OR) (\w+) -> (\w+)$'
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
        for register in left, right:
            self.ensure_register(register)
        if operator == 'AND':
            self.registers[store] = np.uint16(self.registers[left] & self.registers[right])
        else:
            self.registers[store] = np.uint16(self.registers[left] | self.registers[right])

    def do_shift_op(self, vals):
        left, shift, val, store = vals.groups()
        self.ensure_register(left)
        if shift == 'LSHIFT':
            self.registers[store] = np.uint16(self.registers[left] << np.uint16(val))
        else:
            self.registers[store] = np.uint16(self.registers[left] >> np.uint16(val))

    def do_not_op(self, vals):
        val, store = vals.groups()
        self.ensure_register(val)
        self.registers[store] = ~self.registers[val]

    def do_assignment_op(self, vals):
        left, right = vals.groups()
        if left.isdigit():
            self.registers[right] = np.uint16(int(left))
        else:
            self.ensure_register(left)
            self.registers[right] = self.registers[left]

    def ensure_register(self, val):
        if val not in self.registers:
            self.registers[val] = np.uint16(0)

SAMPLE = Wires('sample.txt')
assert SAMPLE.registers['d'] == 72
assert SAMPLE.registers['e'] == 507
assert SAMPLE.registers['f'] == 492
assert SAMPLE.registers['g'] == 114
assert SAMPLE.registers['h'] == 65412
assert SAMPLE.registers['i'] == 65079
assert SAMPLE.registers['x'] == 123
assert SAMPLE.registers['y'] == 456

PROBLEM = Wires('input.txt')
print(PROBLEM.registers)
utils.pretty_print_answer(1, PROBLEM.registers['a'])
