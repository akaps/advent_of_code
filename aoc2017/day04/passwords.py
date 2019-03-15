import re

class Passwords:
    def __init__(self, file_name):
        file = open(file_name)
        self.words = [x.strip() for x in file.readlines()]
        file.close()

    def valid_words(self):
        total = 0
        for word in self.words:
            if is_valid(word):
                total += 1
        return total

    def valid_words_2(self):
        total = 0
        for word in self.words:
            if is_valid(word) and not has_anagrams(word):
                total += 1
        return total

def is_valid(password):
    words = re.split(' ', password)
    processed = set(words)
    return len(processed) == len(words)

def has_anagrams(password):
    words = re.split(' ', password)
    processed = [counts(word) for word in words]
    for i in enumerate(processed):
        for j in (j for j in enumerate(processed) if j[0] > i[0]):
            if i[1] == j[1]:
                return True
    return False

def counts(word):
    result = {}
    letters = set(word)
    for letter in letters:
        count = word.count(letter)
        result[letter] = count
    return result

assert is_valid('aa bb cc dd ee')
assert not is_valid('aa bb cc dd aa')
assert is_valid('aa bb cc dd aaa')

PROBLEM = Passwords('input.txt')
print('Answer to part 1: {ans}'.format(ans=PROBLEM.valid_words()))

assert not has_anagrams('abcde fghij')
assert has_anagrams('abcde xyz ecdab')
assert not has_anagrams('a ab abc abd abf abj')
assert not has_anagrams('iiii oiii ooii oooi oooo')
assert has_anagrams('oiii ioii iioi iiio')

print('Answer to part 2: {ans}'.format(ans=PROBLEM.valid_words_2()))
