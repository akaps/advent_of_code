from aoc2019.int_code import IntCode

def run_with_input(computer, input_val):
    program = computer.load_program()
    program.send(None)
    return program.send(input_val)[0]

def test_branch_sample_1():
    computer = IntCode('day05/branch_sample1.txt')
    assert run_with_input(computer, 8) == 1
    assert run_with_input(computer, 12) == 0

def test_branch_sample_2():
    computer = IntCode('day05/branch_sample2.txt')
    assert run_with_input(computer, 4) == 1
    assert run_with_input(computer, 12) == 0

def test_branch_sample_3():
    computer = IntCode('day05/branch_sample3.txt')
    assert run_with_input(computer, 8) == 1
    assert run_with_input(computer, 20) == 0

def test_branch_sample_4():
    computer = IntCode('day05/branch_sample4.txt')
    assert run_with_input(computer, -13) == 1
    assert run_with_input(computer, 26) == 0

def test_jump_sample_1():
    computer = IntCode('day05/jump_sample1.txt')
    assert run_with_input(computer, 31) == 1
    assert run_with_input(computer, 0) == 0

def test_jump_sample_2():
    computer = IntCode('day05/jump_sample2.txt')
    assert run_with_input(computer, 96) == 1
    assert run_with_input(computer, 0) == 0
