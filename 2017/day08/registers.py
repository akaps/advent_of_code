import re

class Registers:
    def __init__(self):
        self.registers = {}
        self.largest_val=0

    def run_instruction(self, instruction):
        action, condition = re.split(r' if ', instruction)
        if self.parse_condition(condition):
            self.parse_action(action)

    def parse_action(self, action):
        register, act, val = re.split(r' (inc|dec) ', action)
        val = int(val)
        if act == 'dec':
            val = -val
        if register in self.registers:
            self.registers[register] += val
        else:
            self.registers[register] = val
        if self.registers[register] > self.largest_val:
            self.largest_val = self.registers[register]

    def parse_condition(self, condition):
        register, comparator, val = re.split(r' (>|<|>=|<=|==|!=) ', condition)
        val = int(val)
        if not register in self.registers:
            self.registers[register] = 0
        if comparator == '>':
            return self.registers[register] > val
        if comparator == '>=':
            return self.registers[register] >= val
        if comparator == '<':
            return self.registers[register] < val
        if comparator == '<=':
            return self.registers[register] <= val
        if comparator == '==':
            return self.registers[register] == val
        if comparator == '!=':
            return self.registers[register] != val
        return False

def run(file_name, registers):
    file = open(file_name)
    instructions = [line.strip() for line in file.readlines()]
    file.close()
    for instruction in instructions:
        registers.run_instruction(instruction)

SAMPLE = Registers()
run('sample.txt', SAMPLE)
assert max(SAMPLE.registers.values()) == 1

PROBLEM = Registers()
run('input.txt', PROBLEM)
largest = max(PROBLEM.registers.values())
print('Answer to part 1: {ans}'.format(ans=largest))
assert SAMPLE.largest_val == 10
print('Answer to part 2: {ans}'.format(ans=PROBLEM.largest_val))
