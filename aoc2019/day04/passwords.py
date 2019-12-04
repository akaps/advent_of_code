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
    has_strictly_2 = False
    assert len(num) == 6
    if num[0] == num[1] and num[1] != num [2]:
        has_strictly_2 = True
    for index in range(1, 4):
        if num[index - 1] != num[index] and num[index] == num[index + 1] and num[index] != num[index + 2]:
            has_strictly_2 = True
    if num[4] != num[3] and num[4] == num[5]:
        has_strictly_2 = True
    # if has_strictly_2:
    #     print(num)
    return has_strictly_2

assert is_valid_password('111111')
assert not is_valid_password('223450')
assert not is_valid_password('123789')

assert strictly_2_matches('112233')
assert not strictly_2_matches('123444')
assert strictly_2_matches('111122')

assert not strictly_2_matches('578889')

#125730-579381
input_range = range(125730, 579381)
count_valid = 0
valid = []

for i in input_range:
    if is_valid_password(str(i)):
        count_valid += 1
        valid.append(str(i))

repeating_count = 0
for value in valid:
    if strictly_2_matches(value):
        repeating_count += 1

utils.pretty_print_answer(1, count_valid)
utils.pretty_print_answer(2, repeating_count)
