import re
import utils
import aoc2018.processor as processor

def is_command(opcode, code, reg, result):
    return result == processor.execute(opcode, reg, code[1], code[2], code[3])

def possibilities(code, reg, result):
    opcodes = []
    for opcode in processor.INSTRUCTIONS:
        if is_command(opcode, code, reg, result):
            opcodes.append(opcode)
    return opcodes

def find_triples(ops):
    total = 0
    for op in ops:
        if len(possibilities(op['command'], op['before'], op['after'])) >= 3:
            total += 1
    return total

def parse_before(line):
    return [int(d) for d in re.findall(r'\d', line)]

def parse_command(line):
    return [int(d) for d in re.split(r' ', line)]

def parse_after(line):
    return [int(d) for d in re.findall(r'\d', line)]

def determine_opcodes(commands):
    opcodes = {}
    while len(opcodes) < 16:
        command = commands.pop(0)
        possible_codes = possibilities(command['command'], command['before'], command['after'])
        for code in opcodes.values():
            if code in possible_codes:
                possible_codes.remove(code)
        if len(possible_codes) == 1:
            opcodes[command['command'][0]] = possible_codes[0]
        else:
            commands.append(command)
    assert len(opcodes) == 16
    return opcodes

def run_instructions(instructions, opcodes):
    registers = [0, 0, 0, 0]
    for instruction in instructions:
        cmd = parse_command(instruction)
        opcode = opcodes[cmd[0]]
        registers = processor.execute(opcode, registers, cmd[1], cmd[2], cmd[3])
    return registers[0]

#sample input
assert is_command('mulr', [9, 2, 1, 2], [3, 2, 1, 1], [3, 2, 2, 1])
assert is_command('addi', [9, 2, 1, 2], [3, 2, 1, 1], [3, 2, 2, 1])
assert is_command('seti', [9, 2, 1, 2], [3, 2, 1, 1], [3, 2, 2, 1])
assert 3 == len(possibilities([9, 2, 1, 2], [3, 2, 1, 1], [3, 2, 2, 1]))

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
utils.pretty_print_answer(1, ans)

opcodes = determine_opcodes(commands)
file = open('input_b.txt')
instructions = file.readlines()
file.close()
ans = run_instructions(instructions, opcodes)
utils.pretty_print_answer(2, ans)
