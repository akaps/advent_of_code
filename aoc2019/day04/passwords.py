import utils

def is_valid_password(num):
    assert len(num) == 6
    has_pair = False
    always_increasing = True
    for index in range(5):
        if num[index] == num[index + 1]:
            has_pair = True
        if num[index] > num[index + 1]:
            always_increasing = False
    return has_pair and always_increasing

def strictly_2_matches(num):
    assert len(num) == 6
    has_strictly_2 = False
    if num[0] == num[1] and num[1] != num [2]:
        has_strictly_2 = True
    for index in range(1, 4):
        if (num[index - 1] != num[index]
                and num[index] == num[index + 1]
                and num[index] != num[index + 2]):
            has_strictly_2 = True
    if num[4] != num[3] and num[4] == num[5]:
        has_strictly_2 = True
    return has_strictly_2

assert is_valid_password('111111')
assert not is_valid_password('223450')
assert not is_valid_password('123789')

assert strictly_2_matches('112233')
assert not strictly_2_matches('123444')
assert strictly_2_matches('111122')

assert not strictly_2_matches('578889')

#INPUT: 125730-579381
INPUT_RANGE = range(125730, 579381)
COUNT_VALID = 0
VALID = []

for i in INPUT_RANGE:
    if is_valid_password(str(i)):
        COUNT_VALID += 1
        VALID.append(str(i))

REPEATING_COUNT = 0
for value in VALID:
    if strictly_2_matches(value):
        REPEATING_COUNT += 1

utils.pretty_print_answer(1, COUNT_VALID)
utils.pretty_print_answer(2, REPEATING_COUNT)
