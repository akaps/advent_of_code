vowels = 'aeiou'
forbidden = ['ab, cd', 'pq', 'xy']

def is_nice(input_string):
    return False

assert is_nice('ugknbfddgicrmopn')
assert is_nice('aaa')
assert not is_nice('jchzalrnumimnmhp')
assert not is_nice('haegwjzuvuyypxyu')
assert not is_nice('dvszwmarrgswjxmb')

FILE = open('input.txt')
lines = FILE.readlines()
FILE.close()
total = 0
for line in lines:
    if is_nice(line):
        total += 1
print(total)
