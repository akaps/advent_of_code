import re
from aoc_2018.computer import Computer

def is_command(command_name, command, reg_bef, reg_aft):
    check = command_name(command, reg_bef)
    return check == reg_aft

def possibilities(command, reg_bef, reg_aft):
    matches = 0
    for command_name in command_names:
        if is_command(command_name, command, reg_bef, reg_aft):
            matches += 1
    return matches

command_names = [Computer.addr,
                 Computer.addi,
                 Computer.mulr,
                 Computer.muli,
                 Computer.banr,
                 Computer.bani,
                 Computer.borr,
                 Computer.bori,
                 Computer.setr,
                 Computer.seti,
                 Computer.gtir,
                 Computer.gtri,
                 Computer.gtrr,
                 Computer.eqir,
                 Computer.eqri,
                 Computer.eqrr]

def find_triples(ops):
    total = 0
    for op in ops:
        if possibilities(op['command'], op['before'], op['after']) == 3:
            total += 1
    return total

def parse_before(line):
    return [int(d) for d in re.findall('\d', line)]

def parse_command(line):
    return [int(d) for d in re.split(' ', line)]

def parse_after(line):
    return [int(d) for d in re.findall('\d', line)]

#sample input
sample_code = [9, 2, 1, 2]
sample_reg_bef = [3, 2, 1, 1]
sample_reg_aft = [3, 2, 2, 1]
assert 3 == possibilities(sample_code, sample_reg_bef, sample_reg_aft)
assert is_command(Computer.mulr, sample_code, sample_reg_bef, sample_reg_aft)
assert is_command(Computer.addi, sample_code, sample_reg_bef, sample_reg_aft)
assert is_command(Computer.seti, sample_code, sample_reg_bef, sample_reg_aft)

#parsing tests
assert sample_code == parse_command('9 2 1 2')
assert sample_reg_bef == parse_before('Before: [3, 2, 1, 1]')
assert sample_reg_aft == parse_after('After:  [3, 2, 2, 1]')

#arithmetic ops tests
assert is_command(Computer.addr, [-1, 0, 1, 2], [1, 3, 0, -1], [1, 3, 4, -1])
assert is_command(Computer.addi, [-1, 0, 8, 2], [3, -1, -1, -1], [3, -1, 11, -1])
assert is_command(Computer.mulr, [-1, 0, 1, 2], [3, 2, -1, -1], [3, 2, 6, -1])
assert is_command(Computer.muli, [-1, 3, 18, 0], [-1, -1, -1, 2], [36, -1, -1, 2])
assert is_command(Computer.banr, [-1, 2, 1, 0], [-1, 13, 60, -1], [12, 13, 60, -1])
assert is_command(Computer.bani, [-1, 1, 13, 0], [-1, 60, -1, -1], [12, 60, -1, -1])
assert is_command(Computer.borr, [-1, 2, 1, 0], [-1, 13, 60, -1], [61, 13, 60, -1])
assert is_command(Computer.bori, [-1, 1, 13, 0], [-1, 60, -1, -1], [61, 60, -1, -1])
assert is_command(Computer.setr, [-1, 3, -92, 2], [-1, -1, -1, 96], [-1, -1, 96, 96])
assert is_command(Computer.seti, [-1, 200, 10000, 3], [-1, -1, -1, -1], [-1, -1, -1, 200])

#comparison ops tests
assert is_command(Computer.gtir, [-1, 19, 0, 3], [-1, -1, -1, -1], [-1, -1, -1, 1])
assert is_command(Computer.gtir, [-1, -19, 0, 3], [-1, -1, -1, -1], [-1, -1, -1, 0])
assert is_command(Computer.gtri, [-1, 2, 2, 0], [-1, -3, 3, -1], [1, -3, 3, -1])
assert is_command(Computer.gtri, [-1, 1, 2, 0], [-1, -3, 3, -1], [0, -3, 3, -1])
assert is_command(Computer.gtrr, [-1, 1, 2, 3], [-1, 1, 2, -1], [-1, 1, 2, 0])
assert is_command(Computer.gtrr, [-1, 1, 2, 3], [-1, 2, 1, -1], [-1, 2, 1, 1])
assert is_command(Computer.eqri, [-1, 0, 19, 3], [19, -1, -1, -1], [19, -1, -1, 1])
assert is_command(Computer.eqri, [-1, 0, 19, 3], [20, -1, -1, -1], [20, -1, -1, 0])
assert is_command(Computer.eqrr, [-1, 1, 2, 3], [-1, 1, 1, -1], [-1, 1, 1, 1])
assert is_command(Computer.eqrr, [-1, 1, 2, 3], [-1, 420, 69, -1], [-1, 420, 69, 0])

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
