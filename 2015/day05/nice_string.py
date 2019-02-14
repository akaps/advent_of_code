vowels = 'aeiou'
forbidden = ['ab', 'cd', 'pq', 'xy']

def is_nice(input_string):
    return (has_three_vowels(input_string)
            and has_duplicate_letter(input_string)
            and not has_forbidden_pair(input_string))

def has_three_vowels(input_string):
    return len([c for c in input_string if c in vowels]) >= 3

def has_duplicate_letter(input_string):
    for i in range(len(input_string) - 1):
        pair  = input_string[i: i + 2]
        if pair[0] == pair[1]:
            return True
    return False

def has_forbidden_pair(input_string):
    for i in range(len(input_string) - 1):
        pair = input_string[i: i + 2]
        if pair in forbidden:
            return True
    return False

assert is_nice('ugknbfddgicrmopn')
assert is_nice('aaa')
assert not is_nice('jchzalrnumimnmhp')
assert not has_duplicate_letter('jchzalrnumimnmhp')
assert not has_forbidden_pair('jchzalrnumimnmhp')
assert has_three_vowels('jchzalrnumimnmhp')

assert not is_nice('haegwjzuvuyypxyu')
assert has_forbidden_pair('haegwjzuvuyypxyu')
assert has_duplicate_letter('haegwjzuvuyypxyu')
assert has_three_vowels('haegwjzuvuyypxyu')

assert not is_nice('dvszwmarrgswjxmb')
assert not has_three_vowels('dvszwmarrgswjxmb')
assert not has_forbidden_pair('dvszwmarrgswjxmb')
assert has_duplicate_letter('dvszwmarrgswjxmb')

FILE = open('input.txt')
lines = FILE.readlines()
FILE.close()
total = 0
for line in lines:
    if is_nice(line):
        total += 1

print('Answer to part 1: {ans}'.format(ans=total))
