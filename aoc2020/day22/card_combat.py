import utils

class Deck:
    def __init__(self, cards):
        self.cards = [int(x) for x in cards]

    def draw(self):
        return self.cards.pop(0)

    def add(self, card_a, card_b):
        self.cards.append(card_a)
        self.cards.append(card_b)

    def score(self):
        place = 1
        score = 0
        for card in reversed(self.cards):
            score += card * place
            place += 1
        return score

def play_game(deck1, deck2):
    while deck1.cards and deck2.cards:
        deck1_card = deck1.draw()
        deck2_card = deck2.draw()
        if deck1_card > deck2_card:
            deck1.add(deck1_card, deck2_card)
        else:
            deck2.add(deck2_card, deck1_card)
    return deck1 if deck1.cards else deck2

def main():
    player1, player2 = utils.read_groups('input.txt')
    deck1 = Deck(player1[1:])
    deck2 = Deck(player2[1:])
    winner = play_game(deck1, deck2)
    print(winner.cards)
    utils.pretty_print_answer(1, winner.score())

if __name__ == "__main__":
    main()
