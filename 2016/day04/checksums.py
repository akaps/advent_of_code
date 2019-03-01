import re
import utils

def is_real_room(room):
    return False

assert is_real_room('aaaaa-bbb-z-y-x-123[abxyz]')
assert is_real_room('a-b-c-d-e-f-g-h-987[abcde]')
assert is_real_room('not-a-real-room-404[oarel]')
assert not is_real_room('totally-real-room-200[decoy]')

TOTAL = 0
LINES = utils.read_lines('input.txt')
for line in LINES:
    if is_real_room(line):
        TOTAL += 1
utils.pretty_print_answer(1, TOTAL)
