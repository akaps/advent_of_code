import utils
from aoc2019.int_code import IntCode

def main():
    computer = IntCode('input.txt')
    program = computer.load_program()
    program.send(None)
    result = program.send(1)
    assert len(result) == 1, 'opcodes failed according to results {res}'.format(res=result)
    utils.pretty_print_answer(1, result[0])

    program = computer.load_program()
    program.send(None)
    result = program.send(2)
    assert len(result) == 1, 'unexpected additional output {res}'.format(res=result)
    utils.pretty_print_answer(2, result[0])

if __name__ == '__main__':
    main()
