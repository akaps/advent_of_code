from aoc2019.int_code import IntCode

def test_copy():
    computer = IntCode('sample1.txt')
    program = computer.load_program()
    assert program.send(None) == [109,
                                  1,
                                  204,
                                  -1,
                                  1001,
                                  100,
                                  1,
                                  100,
                                  1008,
                                  100,
                                  16,
                                  101,
                                  1006,
                                  101,
                                  0,
                                  99]

def test_16_digits():
    computer = IntCode('sample2.txt')
    program = computer.load_program()
    result = program.send(None)[0]
    assert len(str(result)) == 16

def test_middle_val():
    computer = IntCode('sample3.txt')
    program = computer.load_program()
    assert program.send(None)[0] == 1125899906842624
