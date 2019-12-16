import utils

PATTERN = [0, 1, 0, -1]
REPEAT = 10000

def pattern_val(pattern, element_index, position):
    transform = ((element_index + 1) // (position + 1)) % len(pattern)
    return pattern[transform]

def fft(num, pattern):
    result = []
    for i in range(len(num)):
        total = 0
        for index in range(i, (len(num))):
            val = num[index]
            total += int(val) * pattern_val(pattern, index, i)
        result.append(abs(total) % 10)
    return ''.join([str(x) for x in result])

def pad(num, repeats):
    result = []
    for _ in range(repeats):
        result.append(num)
    return ''.join(result)

def message(signal, offset):
    result = []
    for i in range(8):
        result.append(signal[(offset + i) % len(signal)])
    return ''.join(result)

INPUT = '12345678'
assert pattern_val(PATTERN, 0, 0) == 1
assert pattern_val(PATTERN, 1, 0) == 0
assert pattern_val(PATTERN, 2, 0) == -1
assert pattern_val(PATTERN, 3, 0) == 0
assert pattern_val(PATTERN, 4, 0) == 1
assert pattern_val(PATTERN, 5, 0) == 0
assert pattern_val(PATTERN, 6, 0) == -1
assert pattern_val(PATTERN, 7, 0) == 0

assert pattern_val(PATTERN, 0, 1) == 0
assert pattern_val(PATTERN, 1, 1) == 1
assert pattern_val(PATTERN, 2, 1) == 1
assert pattern_val(PATTERN, 3, 1) == 0
assert pattern_val(PATTERN, 4, 1) == 0
assert pattern_val(PATTERN, 5, 1) == -1
assert pattern_val(PATTERN, 6, 1) == -1
assert pattern_val(PATTERN, 7, 1) == 0

assert pattern_val(PATTERN, 0, 2) == 0
assert pattern_val(PATTERN, 1, 2) == 0
assert pattern_val(PATTERN, 2, 2) == 1
assert pattern_val(PATTERN, 3, 2) == 1
assert pattern_val(PATTERN, 4, 2) == 1
assert pattern_val(PATTERN, 5, 2) == 0
assert pattern_val(PATTERN, 6, 2) == 0
assert pattern_val(PATTERN, 7, 2) == 0

INPUT = fft(INPUT, PATTERN)
assert INPUT == '48226158'
INPUT = fft(INPUT, PATTERN)
assert INPUT == '34040438'
INPUT = fft(INPUT, PATTERN)
assert INPUT == '03415518'
INPUT = fft(INPUT, PATTERN)
assert INPUT == '01029498'

assert message('98765432109876543210', 7) == '21098765'
assert len(pad('1', REPEAT)) == REPEAT

INPUT = '80871224585914546619083218645595'
for _ in range(100):
    INPUT = fft(INPUT, PATTERN)
assert INPUT[:8] == '24176176'

INPUT = '19617804207202209144916044189917'
for _ in range(100):
    INPUT = fft(INPUT, PATTERN)
assert INPUT[:8] == '73745418'

INPUT  = '69317163492948606335995924319873'
for _ in range(100):
    INPUT = fft(INPUT, PATTERN)
assert INPUT[:8] == '52432133'

FILE = open('input.txt')
PROBLEM = FILE.readline().strip()
FILE.close()
print('solving for a {n} digit number'.format(n=len(PROBLEM)))
for _ in range(100):
    PROBLEM = fft(PROBLEM, PATTERN)
utils.pretty_print_answer(1, PROBLEM[:8])

print('checking padding cases')
INPUT = pad('03036732577212944063491565474664', REPEAT)
OFFSET = INPUT[:7]
for _ in range(100):
    INPUT = fft(INPUT, PATTERN)
assert message(INPUT, OFFSET) == '84462026'

print('checking second padding case')
INPUT = pad('02935109699940807407585447034323', REPEAT)
OFFSET = INPUT[:7]
for _ in range(100):
    INPUT = fft(INPUT, PATTERN)
assert message(INPUT, OFFSET) == '78725270'

INPUT = pad('03081770884921959731165446850517', REPEAT)
OFFSET = INPUT[:7]
for _ in range(100):
    INPUT = fft(INPUT, PATTERN)
assert message(INPUT, OFFSET) == '53553731'

print('solving for an even bigger number')
FILE = open('input.txt')
PROBLEM = FILE.readline().strip()
FILE.close()
PROBLEM = pad(PROBLEM, REPEAT)
OFFSET = PROBLEM[:7]
for _ in range(100):
    PROBLEM = fft(PROBLEM, PATTERN)
utils.pretty_print_answer(1, message(PROBLEM, OFFSET))
