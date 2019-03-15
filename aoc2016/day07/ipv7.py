import re
import utils

def supports_tls(address):
    pieces = re.split(r'\[|\]', address)
    untagged_pair = False
    for piece in enumerate(pieces):
        reverse_pair = has_reverse_pair(piece[1])
        if not piece[0] % 2 and reverse_pair:
            untagged_pair = True
        if piece[0] % 2 and reverse_pair:
            return False
    return untagged_pair

def has_reverse_pair(piece):
    for i in range(len(piece) - 3):
        if (piece[i] == piece[i + 3] and
                piece[i + 1] == piece[i + 2] and
                piece[i] != piece[i + 1]):
            return True
    return False

assert supports_tls('abba[mnop]qrst')
assert not supports_tls('abcd[bddb]xyyx')
assert not supports_tls('aaaa[qwer]tyui')
assert supports_tls('ioxxoj[asdfgh]zxcvbn')

LINES = utils.read_lines('input.txt')
TOTAL = 0
for line in LINES:
    if supports_tls(line):
        TOTAL += 1
utils.pretty_print_answer(1, TOTAL)
