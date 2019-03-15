import re
import utils

GROUP_START = '('
GROUP_END = ')'
GROUP_DELIMETER = 'x'

def decompress(line):
    length = 0
    to_process = list(line)
    while to_process:
        next_char = to_process.pop(0)
        if next_char == GROUP_START:
            end_index = to_process.index(GROUP_END)
            expand = ''.join(to_process[:end_index])
            num_characters, num_times = [int(d) for d in re.split(GROUP_DELIMETER, expand)]
            length += num_characters * num_times
            to_process = to_process[end_index + 1 + num_characters:]
        else:
            length += 1
    return length

def recursive_decompress(line):
    return -1

assert decompress('ADVENT') == 6
assert decompress('A(1x5)BC') == 7
assert decompress('(3x3)XYZ') == 9
assert decompress('(6x1)(1x3)A') == 6
assert decompress('X(8x2)(3x3)ABCY') == 18

file = open('input.txt')
line = file.readline().strip()
file.close()

utils.pretty_print_answer(1, decompress(line))

assert recursive_decompress('(3x3)XYZ') == 9
assert recursive_decompress('X(8x2)(3x3)ABCY') == 20
assert recursive_decompress('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
assert recursive_decompress('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445

utils.pretty_print_answer(2, recursive_decompress(line))
