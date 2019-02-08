import re

def is_op(op_name, opcode, reg_bef, reg_aft):
    check = op_name(opcode, reg_bef)
    return check == reg_aft

def addr(opcode, reg):
    res = list(reg)
    res[opcode[3]] = res[opcode[1]] + res[opcode[2]]
    return res

def addi(opcode, reg):
    res = list(reg)
    res[opcode[3]] = res[opcode[1]] + opcode[2]
    return res

def mulr(opcode, reg):
    res = list(reg)
    res[opcode[3]] = res[opcode[1]] * res[opcode[2]]
    return res

def muli(opcode, reg):
    res = list(reg)
    res[opcode[3]] = res[opcode[1]] * opcode[2]
    return res

def banr(opcode, reg):
    res = list(reg)
    res[opcode[3]] = res[opcode[1]] & res[opcode[2]]
    return res

def bani(opcode, reg):
    res = list(reg)
    res[opcode[3]] = res[opcode[1]] & opcode[2]
    return res

def borr(opcode, reg):
    res = list(reg)
    res[opcode[3]] = res[opcode[1]] | res[opcode[2]]
    return res

def bori(opcode, reg):
    res = list(reg)
    res[opcode[3]] = res[opcode[1]] | opcode[2]
    return res

def setr(opcode, reg):
    res = list(reg)
    res[opcode[3]] = res[opcode[1]]
    return res

def seti(opcode, reg):
    res = list(reg)
    res[opcode[3]] = opcode[1]
    return res

def gtir(opcode, reg):
    res = list(reg)
    res[opcode[3]] = 1 if opcode[1] > res[opcode[2]] else 0
    return res

def gtri(opcode, reg):
    res = list(reg)
    res[opcode[3]] = 1 if res[opcode[1]] > opcode[2] else 0
    return res

def gtrr(opcode, reg):
    res = list(reg)
    res[opcode[3]] = 1 if res[opcode[1]] > res[opcode[2]] else 0
    return res

def eqir(opcode, reg):
    res = list(reg)
    res[opcode[3]] = 1 if opcode[1] == res[opcode[2]] else 0
    return res

def eqri(opcode, reg):
    res = list(reg)
    res[opcode[3]] = 1 if res[opcode[1]] == opcode[2] else 0
    return res

def eqrr(opcode, reg):
    res = list(reg)
    res[opcode[3]] = 1 if res[opcode[1]] == res[opcode[2]] else 0
    return res

def possibilities(op_code, reg_bef, reg_aft):
    matches = 0
    for op_name in op_names:
        if is_op(op_name, op_code, reg_bef, reg_aft):
            matches += 1
    return matches

op_names = [addr,
            addi,
            mulr,
            muli,
            banr,
            bani,
            borr,
            bori,
            setr,
            seti,
            gtir,
            gtri,
            gtrr,
            eqir,
            eqri,
            eqrr]

def find_triples(ops):
    total = 0
    for op in ops:
        if possibilities(op['opcode'], op['before'], op['after']) == 3:
            total += 1
    return total

def parse_before(line):
    return [int(d) for d in re.findall('\d', line)]

def parse_opcode(line):
    return [int(d) for d in re.split(' ', line)]

def parse_after(line):
    return [int(d) for d in re.findall('\d', line)]

sample_code = [9, 2, 1, 2]
sample_reg_bef = [3, 2, 1, 1]
sample_reg_aft = [3, 2, 2, 1]
assert 3 == possibilities(sample_code, sample_reg_bef, sample_reg_aft)
assert sample_code == parse_opcode('9 2 1 2')
assert sample_reg_bef == parse_before('Before: [3, 2, 1, 1]')
assert sample_reg_aft == parse_after('After:  [3, 2, 2, 1]')

ops = []
with open('day_16_input_a.txt', 'r') as file:
    while True:
        op = {}
        #before line
        op['before'] = parse_before(file.readline())
        #opcode line
        op['opcode'] = parse_opcode(file.readline())
        #after line
        op['after'] = parse_after(file.readline())
        ops.append(op)
        empty_line = file.readline()
        if not empty_line:
            break
print(ops[0])
assert len(ops) == 809
ans = find_triples(ops)
assert ans < 809
print('Answer to part 1: {ans}'.format(ans=ans))