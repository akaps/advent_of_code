from collections import defaultdict
import utils

COMMA = ','

class Counter:
    def __init__(self, start):
        self.current_time = 1
        self.seed = start
        self.previous = defaultdict(lambda: 0)

    def play_round(self, number):
        self.current_time += 1
        past_time = self.previous[number]
        self.previous[number] = self.current_time
        if past_time == 0:
            return 0
        return self.current_time - past_time

    def play_game(self, total_time):
        previous_number = -1
        for number in self.seed:
            previous_number = self.play_round(number)
        while self.current_time < total_time:
            previous_number = self.play_round(previous_number)
        return previous_number

def main():
    seed = [10, 16, 6, 0, 1, 17]
    counter = Counter(seed)
    utils.pretty_print_answer(1, counter.play_game(2020))
    counter = Counter(seed)
    utils.pretty_print_answer(2, counter.play_game(30000000))

if __name__ == "__main__":
    main()
