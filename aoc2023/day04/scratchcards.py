import re

ID_DELIMITER = ': '
CARD_DELIMITER = ' | '
ID_REGEX = r'Card *(\d+)'

class ScratchCard:
    def __init__(self, line: str):
        self.winning_numbers, self.playing_numbers = line.strip().split(CARD_DELIMITER)
        self.winning_numbers = [int(x) for x in self.winning_numbers.split()]
        self.playing_numbers = [int(x) for x in self.playing_numbers.split()]

    def score(self):
        total = 0
        for number in self.playing_numbers:
            if number in self.winning_numbers:
                total += 1
        return total

class ScratchCards:
    def __init__(self, input_file):
        self.cards = {}
        lines = open(input_file).readlines()
        for line in lines:
            card_id, numbers = line.split(ID_DELIMITER)
            card_id = re.match(ID_REGEX, card_id).group(0)
            self.cards[card_id] = ScratchCard(numbers)

    def total_score(self):
        total = 0
        for card in self.cards.values():
            card_score = card.score()
            total += 2 ** (card_score - 1) if card_score > 0 else 0
        return total

    def total_cards(self):
        copies = [1] * len(self.cards)
        #card index: num_copies
        for index, card in enumerate(self.cards.values()):
            score = card.score()
            for i in range(index + 1, index + score + 1):
                if i < len(copies):
                    copies[i] += copies[index]
        return sum(copies)

def main():
    sample = ScratchCards('aoc2023/day04/sample.txt')
    assert sample.total_score() == 13
    problem = ScratchCards('aoc2023/day04/input.txt')
    print('Answer to Part 1: ', problem.total_score())

    assert sample.total_cards() == 30
    print('Answer to part 2: ', problem.total_cards())

if __name__ == '__main__':
    main()
