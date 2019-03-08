import collections
import utils

class Signal:
    def __init__(self, file_name):
        lines = utils.read_lines(file_name)
        self.letters = []
        self.populate(lines)

    def most_frequent(self):
        res = ''
        for char_index in self.letters:
            res += collections.Counter(char_index).most_common(1)[0][0]
        return res

    def least_frequent(self):
        res = ''
        for char_index in self.letters:
            res += collections.Counter(char_index).most_common()[-1][0]
        return res

    def populate(self, lines):
        for char_index in range(len(lines[0])):
            letters = []
            for j in range(len(lines)):
                letters.append(lines[j][char_index])
            self.letters.append(letters)

SAMPLE = Signal('sample.txt')
assert SAMPLE.most_frequent() == 'easter'
assert SAMPLE.least_frequent() == 'advent'

PROBLEM = Signal('input.txt')
utils.pretty_print_answer(1, PROBLEM.most_frequent())
utils.pretty_print_answer(2, PROBLEM.least_frequent())
