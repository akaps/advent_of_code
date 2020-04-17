import utils

vowels = 'aeiou'
forbidden = ['ab', 'cd', 'pq', 'xy']

def is_nice(input_string):
    return (has_three_vowels(input_string)
            and has_duplicate_letter(input_string)
            and not has_forbidden_pair(input_string))

def is_nice_pt2(input_string):
    return (two_pairs(input_string)
            and letter_sandwich(input_string))

def two_pairs(input_string):
    for i in range(len(input_string) - 1):
        pair = input_string[i: i + 2]
        print(pair)
        if pair in input_string[i + 2:]:
            return True
    return False

def letter_sandwich(input_string):
    for i in range(len(input_string) - 2):
        first, second, third = input_string[i: i + 3]
        if first == third and first != second:
            return True
    return False

def has_three_vowels(input_string):
    return len([c for c in input_string if c in vowels]) >= 3

def has_duplicate_letter(input_string):
    for i in range(len(input_string) - 1):
        pair = input_string[i: i + 2]
        if pair[0] == pair[1]:
            return True
    return False

def has_forbidden_pair(input_string):
    for i in range(len(input_string) - 1):
        pair = input_string[i: i + 2]
        if pair in forbidden:
            return True
    return False

def part1():
    file = open('input.txt')
    lines = file.readlines()
    file.close()
    total = 0
    for line in lines:
        if is_nice(line):
            total += 1
    return total

def part2():
    file = open('input.txt')
    lines = file.readlines()
    file.close()
    total = 0
    for line in lines:
        if is_nice_pt2(line):
            total += 1
    return total

def main():
    utils.pretty_print_answer(1, part1())
    utils.pretty_print_answer(2, part2())

if __name__ == '__main__':
    main()
