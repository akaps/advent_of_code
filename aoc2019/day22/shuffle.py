import re
import utils

DEAL = r'deal into new stack'
CUT = r'cut (-?\d+)'
INCREMENT = r'deal with increment (\d+)'

def parse_match(match):
    #for cut and increment, we care about the first match group
    #this element is an int
    return int(match.groups()[0])

class Deck:
    def __init__(self, num_cards):
        self.deck = [x for x in range(num_cards)]

    def shuffle(self, instruction_file):
        lines = utils.read_lines(instruction_file)
        for line in lines:
            if re.match(DEAL, line):
                self.deal_stack()
            elif re.match(CUT, line):
                match = re.search(CUT, line)
                self.cut_at(parse_match(match))
            elif re.match(INCREMENT, line):
                match = re.search(INCREMENT, line)
                self.deal_increment(parse_match(match))

    def deal_stack(self):
        self.deck.reverse()

    def cut_at(self, index):
        self.deck = self.deck[index:] + self.deck[:index]

    def deal_increment(self, num):
        new_deck = [0] * len(self.deck)
        for index, i in enumerate(self.deck):
            new_deck[(index * num) % len(self.deck)] = i
        self.deck = new_deck

SAMPLE = Deck(10)
SAMPLE.deal_increment(7)
SAMPLE.deal_stack()
SAMPLE.deal_stack()
assert SAMPLE.deck == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]

SAMPLE = Deck(10)
SAMPLE.shuffle('sample1.txt')
assert SAMPLE.deck == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]

SAMPLE = Deck(10)
SAMPLE.shuffle('sample2.txt')
assert SAMPLE.deck == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]

SAMPLE = Deck(10)
SAMPLE.shuffle('sample3.txt')
assert SAMPLE.deck == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]

SAMPLE = Deck(10)
SAMPLE.shuffle('sample4.txt')
assert SAMPLE.deck == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]

PROBLEM = Deck(10007)
PROBLEM.shuffle('input.txt')
utils.pretty_print_answer(1, PROBLEM.deck.index(2019))
