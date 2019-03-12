import utils

DOUBLE = '"'
BACKSLASH = '\\'
HEX = 'x'

class Strings:
    def __init__(self, file_name):
        file = open(file_name)
        self.strings = [s.strip() for s in file.readlines()]
        file.close()

    def count_literals(self, s_index):
        return len(self.strings[s_index])

    def count_characters(self, s_index):
        to_process = list(self.strings[s_index])
        total = 0
        while to_process:
            next_char = to_process.pop(0)
            if next_char != DOUBLE:
                if next_char == BACKSLASH:
                    following_char = to_process.pop(0)
                    if following_char == HEX:
                        to_process.pop(0)
                        to_process.pop(0)
                total += 1
        return total

    def count_encoded(self, s_index):
        to_process = list(self.strings[s_index])
        total = 0
        while to_process:
            val = to_process.pop(0)
            if val in [DOUBLE, BACKSLASH]:
                total += 2
            else:
                total += 1
        return total + 2

    def character_diff(self):
        total = 0
        for s_index, _ in enumerate(self.strings):
            total += self.count_literals(s_index) - self.count_characters(s_index)
        return total

    def encoded_diff(self):
        total = 0
        for s_index, _ in enumerate(self.strings):
            total += self.count_encoded(s_index) - self.count_literals(s_index)
        return total

SAMPLE = Strings('sample.txt')
assert SAMPLE.count_literals(0) == 2
assert SAMPLE.count_characters(0) == 0

assert SAMPLE.count_literals(1) == 5
assert SAMPLE.count_characters(1) == 3

assert SAMPLE.count_literals(2) == 10
assert SAMPLE.count_characters(2) == 7

assert SAMPLE.count_literals(3) == 6
assert SAMPLE.count_characters(3) == 1

PROBLEM = Strings('input.txt')
utils.pretty_print_answer(1, PROBLEM.character_diff())

assert SAMPLE.count_encoded(0) == 6
assert SAMPLE.count_encoded(1) == 9
assert SAMPLE.count_encoded(2) == 16
assert SAMPLE.count_encoded(3) == 11

utils.pretty_print_answer(2, PROBLEM.encoded_diff())
