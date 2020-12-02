import utils

REGEX = r'(\d+)-(\d+) (\w): (\w*)'

def is_valid_pt1(string):
    low, high, letter, password = utils.split_line(REGEX, string)
    low = int(low)
    high = int(high)
    count = 0
    for character in password:
        if character == letter:
            count += 1
    return high >= count >= low

def is_valid_pt2(string):
    low, high, letter, password = utils.split_line(REGEX, string)
    low = int(low) - 1
    high = int(high) - 1
    count = 0
    if password[low] == letter:
        count += 1
    if password[high] == letter:
        count += 1
    return count == 1

def part_1(lines):
    assert is_valid_pt1('1-3 a: abcde')
    assert not is_valid_pt1('1-3 b: cdefg')
    assert is_valid_pt1('2-9 c: ccccccccc')

    count = 0
    for line in lines:
        if is_valid_pt1(line):
            count += 1
    utils.pretty_print_answer(1, count)

def part_2(lines):
    assert is_valid_pt2('1-3 a: abcde')
    assert not is_valid_pt2('1-3 b: cdefg')
    assert not is_valid_pt2('2-9 c: ccccccccc')

    count = 0
    for line in lines:
        if is_valid_pt2(line):
            count += 1
    utils.pretty_print_answer(2, count)

def main():
    lines = utils.read_lines('input.txt')
    part_1(lines)
    part_2(lines)

if __name__ == "__main__":
    main()
