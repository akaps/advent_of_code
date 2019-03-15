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

TOTAL = 0
for line1, line2, line3 in zip(*[iter(PROBLEM)]*3):
    a1, a2, a3 = re.split(r' +', line1)
    b1, b2, b3 = re.split(r' +', line2)
    c1, c2, c3 = re.split(r' +', line3)
    triangles = [(a1, b1, c1), (a2, b2, c2), (a3, b3, c3)]
    for i in range(3):
        a, b, c = triangles[i]
        if is_triangle(int(a), int(b), int(c)):
            TOTAL += 1
utils.pretty_print_answer(2, TOTAL)
