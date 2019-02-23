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

def is_valid(password):
    words = re.split(' ', password)
    processed = set(words)
    return len(processed) == len(words)

assert is_valid('aa bb cc dd ee')
assert not is_valid('aa bb cc dd aa')
assert is_valid('aa bb cc dd aaa')

PROBLEM = Passwords('input.txt')
print('Answer to par 1: {ans}'.format(ans=PROBLEM.valid_words()))
