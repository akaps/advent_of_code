FIRST_LETTERS = 'otfsen'

LITERALS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def sum_of_values(input_file: str, literals=False):
    lines = open(input_file).readlines()
    return sum([parse_value(line, literals) for line in lines])

def parse_value(input_str: str, literals=False):
    first_val = last_val = None
    for index, char in enumerate(input_str):
        if char.isdigit():
            if not first_val:
                first_val = char
            last_val = char
        if literals and char in FIRST_LETTERS:
            for literal in LITERALS.keys():
                if input_str[index:].startswith(literal):
                    if not first_val:
                        first_val = literal
                    last_val = literal

    return int(parse_number(first_val) + parse_number(last_val))

def parse_number(input_str: str):
    if input_str.isdigit():
        return input_str
    return LITERALS[input_str]

def main():
    assert parse_value('1abc2') == 12
    assert parse_value('pqr3stu8vwx') == 38
    assert parse_value('a1b2c3d4e5f') == 15
    assert parse_value('treb7uchet') == 77

    assert sum_of_values('aoc2023/day01/sample.txt') == 142
    print('Answer to Part 1: ', sum_of_values('aoc2023/day01/input.txt'))

    assert parse_value('two1nine', literals=True) == 29
    assert parse_value('eightwothree', literals=True) == 83
    assert parse_value('abcone2threexyz', literals=True) == 13
    assert parse_value('xtwone3four', literals=True) == 24
    assert parse_value('4nineeightseven2', literals=True) == 42
    assert parse_value('zoneight234', literals=True) == 14
    assert parse_value('7pqrstsixteen', literals=True) == 76
    assert sum_of_values('aoc2023/day01/part2_sample.txt', literals=True) == 281
    print('Answer to Part 1: ', sum_of_values('aoc2023/day01/input.txt', literals=True))

if __name__ == '__main__':
    main()
