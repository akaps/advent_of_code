CARD_RANKINGS = 'AKQJT98765432'
JOKER_CARD_RANKINGS = 'AKQT98765432J'

FIVE_KIND = 'five of a kind'
FOUR_KIND = 'four of a kind'
FULL_HOUSE = 'full house'
THREE_KIND = 'three of a kind'
TWO_PAIR = 'two pair'
PAIR = 'one pair'
HIGH_CARD = 'high card'

JOKER = 'J'

CLASSIFICATIONS = {
    FIVE_KIND: 7,
    FOUR_KIND: 6,
    FULL_HOUSE: 5,
    THREE_KIND: 4,
    TWO_PAIR: 3,
    PAIR: 2,
    HIGH_CARD: 1
}

def classify_hand_by_counts(counts:dict[str, int]):
    if len(counts) == 1:
        return FIVE_KIND
    if 4 in counts:
        return FOUR_KIND
    if 3 in counts:
        if 2 in counts:
            return FULL_HOUSE
        return THREE_KIND
    if 2 in counts:
        count_pairs = sum([1 for count in counts if count ==2])
        if count_pairs == 2:
            return TWO_PAIR
        return PAIR
    return HIGH_CARD

def classify_hand(cards: str, joker:bool=False):
    count_map = {}
    for card in cards:
        if card not in count_map:
            count_map[card] = 1
        else:
            count_map[card] += 1
    if joker and JOKER in count_map and len(count_map) != 1:
        joker_count = count_map.pop(JOKER)
        max_key = max(count_map, key=count_map.get)
        count_map[max_key] += joker_count
    return classify_hand_by_counts(count_map.values())

class Cards:
    def __init__(self, cards: str, joker:bool):
        self.cards, self.bid = cards.split()
        self.bid = int(self.bid)
        self.classification = classify_hand(self.cards, joker)
        self.joker = joker

    def __lt__(self, other):
        if isinstance(other, Cards):
            if self.classification != other.classification:
                return CLASSIFICATIONS[self.classification] < CLASSIFICATIONS[other.classification]
            for index, card in enumerate(self.cards):
                other_card = other.cards[index]
                if card != other_card:
                    if self.joker:
                        return JOKER_CARD_RANKINGS.index(card) > JOKER_CARD_RANKINGS.index(other_card)
                    return CARD_RANKINGS.index(card) > CARD_RANKINGS.index(other_card)
            return self.cards < other.cards
        return self.__hash__() < other.__hash__()

    def __eq__(self, other):
        if isinstance(other, Cards):
            return self.cards == other.cards
        return False

    def __str__(self):
        return f'{self.cards}: {self.classification}->{self.bid}'

    def __repr__(self):
        return (str(self))

class CamelCards:
    def __init__(self, file_name: str, joker:bool=False):
        self.hands = []
        lines = open(file_name, encoding='utf-8').readlines()
        for line in lines:
            self.hands.append(Cards(line, joker))
        self.hands.sort()

    def total_winnings(self):
        total = 0
        for rank, hand in enumerate(self.hands):
            total += (rank + 1) * hand.bid
        return total

def main():
    assert classify_hand('AAAAA') == FIVE_KIND
    assert classify_hand('AA8AA') == FOUR_KIND
    assert classify_hand('23332') == FULL_HOUSE
    assert classify_hand('TTT98') == THREE_KIND
    assert classify_hand('23432') == TWO_PAIR
    assert classify_hand('A23A4') == PAIR
    assert classify_hand('23456') == HIGH_CARD

    sample = CamelCards('aoc2023/day07/sample.txt')
    assert sample.total_winnings() == 6440
    game = CamelCards('aoc2023/day07/input.txt')
    print('Answer to part 1:', game.total_winnings())

    sample = CamelCards('aoc2023/day07/sample.txt', joker=True)
    assert sample.total_winnings()
    game = CamelCards('aoc2023/day07/input.txt', joker=True)
    print('Answer to part 2:', game.total_winnings())

if __name__ == '__main__':
    main()
