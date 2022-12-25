def snafu_to_decimal(value):
    total = 0
    power = 0
    for digit in value[::-1]:
        if digit.isdigit():
            total += int(digit) * 5 ** power
        elif digit == '-':
            total += -1 * 5 ** power
        elif digit == '=':
            total += -2 * 5 ** power
        else:
            assert False, 'unsupported digit {digit}'.format(digit=digit)
        power += 1
    return total

def decimal_to_snafu(value):
    result = []
    while value:
        quintuple = value % 5
        if quintuple == 3:
            result.append('=')
            value += 2
        elif quintuple == 4:
            result.append('-')
            value += 1
        else:
            result.append(str(quintuple))
        value //= 5
    result.reverse()
    print(result)
    return ''.join(result)

def decimal_sum(file_name):
    file_input = open(file_name, 'r')
    lines = [line.strip() for line in file_input.readlines()]
    file_input.close()

    sum = 0
    for line in lines:
        sum += snafu_to_decimal(line)
    return sum

def snafu_sum(file_name):
    return decimal_to_snafu(decimal_sum(file_name))

def main():
    assert snafu_to_decimal('1=-0-2') == 1747
    assert snafu_to_decimal('12111') == 906
    assert snafu_to_decimal('2=0=') == 198
    assert snafu_to_decimal('21') == 11
    assert snafu_to_decimal('2=01') == 201
    assert snafu_to_decimal('111') == 31
    assert snafu_to_decimal('20012') == 1257
    assert snafu_to_decimal('112') == 32
    assert snafu_to_decimal('1=-1=') == 353
    assert snafu_to_decimal('1-12') == 107
    assert snafu_to_decimal('12') == 7
    assert snafu_to_decimal('1=') == 3
    assert snafu_to_decimal('122') == 37

    assert decimal_to_snafu(1) == '1'
    assert decimal_to_snafu(2) == '2'
    assert decimal_to_snafu(3) == '1='
    assert decimal_to_snafu(4) == '1-'
    assert decimal_to_snafu(5) == '10'
    assert decimal_to_snafu(6) == '11'
    assert decimal_to_snafu(7) == '12'
    assert decimal_to_snafu(8) == '2='
    assert decimal_to_snafu(9) == '2-'
    assert decimal_to_snafu(10) == '20'
    assert decimal_to_snafu(15) == '1=0'
    assert decimal_to_snafu(20) == '1-0'
    assert decimal_to_snafu(2022) == '1=11-2'
    assert decimal_to_snafu(12345) == '1-0---0'
    assert decimal_to_snafu(314159265) == '1121-1110-1=0'

    assert decimal_sum('aoc2022/day25/sample.txt') == 4890
    assert snafu_sum('aoc2022/day25/sample.txt') == '2=-1=0'

    print('Part 1:', snafu_sum('aoc2022/day25/input.txt'))

if __name__ == '__main__':
    main()
