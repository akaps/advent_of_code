import re
from aoc2018.computer import INSTRUCTIONS

def is_command(cmd_name, code, reg, result):
    output = list(result)
    output[code[3]] = INSTRUCTIONS[cmd_name](reg, code[1], code[2])
    return output == result

def possibilities(code, reg, result):
    total = 0
    for cmd_name in INSTRUCTIONS:
        if is_command(cmd_name, code, reg, result):
            total += 1
    return total

def find_triples(ops):
    total = 0
    for op in ops:
        if possibilities(op['command'], op['before'], op['after']) >= 3:
            total += 1
    return total

def parse_before(line):
    return [int(d) for d in re.findall(r'\d', line)]

def parse_command(line):
    return [int(d) for d in re.split(r' ', line)]

def parse_after(line):
    return [int(d) for d in re.findall(r'\d', line)]

#sample input
assert is_command('mulr', [9, 2, 1, 2], [3, 2, 1, 1], [3, 2, 2, 1])
assert is_command('addi', [9, 2, 1, 2], [3, 2, 1, 1], [3, 2, 2, 1])
assert is_command('seti', [9, 2, 1, 2], [3, 2, 1, 1], [3, 2, 2, 1])
assert 3 == possibilities([9, 2, 1, 2], [3, 2, 1, 1], [3, 2, 2, 1])

#parsing tests
assert [9, 2, 1, 2] == parse_command('9 2 1 2')
assert [3, 2, 1, 1] == parse_before('Before: [3, 2, 1, 1]')
assert [3, 2, 2, 1] == parse_after('After:  [3, 2, 2, 1]')

#arithmetic ops tests
assert is_command('addr', [-1, 0, 1, 2], [1, 3, 0, -1], [1, 3, 4, -1])
assert is_command('addi', [-1, 0, 8, 2], [3, -1, -1, -1], [3, -1, 11, -1])
assert is_command('mulr', [-1, 0, 1, 2], [3, 2, -1, -1], [3, 2, 6, -1])
assert is_command('muli', [-1, 3, 18, 0], [-1, -1, -1, 2], [36, -1, -1, 2])
assert is_command('banr', [-1, 2, 1, 0], [-1, 13, 60, -1], [12, 13, 60, -1])
assert is_command('bani', [-1, 1, 13, 0], [-1, 60, -1, -1], [12, 60, -1, -1])
assert is_command('borr', [-1, 2, 1, 0], [-1, 13, 60, -1], [61, 13, 60, -1])
assert is_command('bori', [-1, 1, 13, 0], [-1, 60, -1, -1], [61, 60, -1, -1])
assert is_command('setr', [-1, 3, -92, 2], [-1, -1, -1, 96], [-1, -1, 96, 96])
assert is_command('seti', [-1, 200, 10000, 3], [-1, -1, -1, -1], [-1, -1, -1, 200])

#comparison ops tests
assert is_command('gtir', [-1, 19, 0, 3], [-1, -1, -1, -1], [-1, -1, -1, 1])
assert is_command('gtir', [-1, -19, 0, 3], [-1, -1, -1, -1], [-1, -1, -1, 0])
assert is_command('gtri', [-1, 2, 2, 0], [-1, -3, 3, -1], [1, -3, 3, -1])
assert is_command('gtri', [-1, 1, 2, 0], [-1, -3, 3, -1], [0, -3, 3, -1])
assert is_command('gtrr', [-1, 1, 2, 3], [-1, 1, 2, -1], [-1, 1, 2, 0])
assert is_command('gtrr', [-1, 1, 2, 3], [-1, 2, 1, -1], [-1, 2, 1, 1])
assert is_command('eqri', [-1, 0, 19, 3], [19, -1, -1, -1], [19, -1, -1, 1])
assert is_command('eqri', [-1, 0, 19, 3], [20, -1, -1, -1], [20, -1, -1, 0])
assert is_command('eqrr', [-1, 1, 2, 3], [-1, 1, 1, -1], [-1, 1, 1, 1])
assert is_command('eqrr', [-1, 1, 2, 3], [-1, 420, 69, -1], [-1, 420, 69, 0])

#real input
commands = []
with open('input_a.txt', 'r') as file:
    while True:
        cmd = {}
        #before line
        cmd['before'] = parse_before(file.readline())
        #command line
        cmd['command'] = parse_command(file.readline())
        #after line
        cmd['after'] = parse_after(file.readline())
        commands.append(cmd)
        empty_line = file.readline()
        if not empty_line:
            break
assert len(commands) == 809
ans = find_triples(commands)
assert ans < 809
print('Answer to part 1: {ans}'.format(ans=ans))
