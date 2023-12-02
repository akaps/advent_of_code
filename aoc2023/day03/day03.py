def fn1(input_file):
    return 0

def main():
    assert fn1('aoc2023/day03/sample.txt') == -1
    print('Answer to Part 1:', fn1('aoc2023/day03/input.txt'))

if __name__ == '__main__':
    main()
