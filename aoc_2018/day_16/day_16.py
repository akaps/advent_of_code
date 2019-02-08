from operator import methodcaller

def is_op(op_name, opcode, reg_bef, reg_aft):
    check = op_name(opcode, reg_bef)
    print('op: {op}\ncode:{code}\nbef:{bef}\nexp: {exp}\nact: {act}\nresult: {res}'.format(
        op=op_name,
        code=opcode,
        bef=reg_bef,
        exp=check,
        act=reg_aft,
        res=check==reg_aft
    ))
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
    print(matches)
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
        if possibilities == 3:
            total += 1

sample_code = [9, 2, 1, 2]
sample_reg_bef = [3, 2, 1, 1]
sample_reg_aft = [3, 2, 2, 1]
print(possibilities(sample_code, sample_reg_bef, sample_reg_aft))
assert 3 == possibilities(sample_code, sample_reg_bef, sample_reg_aft)
