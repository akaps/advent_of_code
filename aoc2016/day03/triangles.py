import re
import utils

def is_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0] + sides[1] > sides[2]

assert not is_triangle(5, 10, 25)
assert not is_triangle(25, 5, 10)
assert not is_triangle(10, 25, 5)

PROBLEM = utils.read_lines('input.txt')
TOTAL = 0
for line in PROBLEM:
    a, b, c = re.split(r' +', line)
    if is_triangle(int(a), int(b), int(c)):
        TOTAL += 1
utils.pretty_print_answer(1, TOTAL)
