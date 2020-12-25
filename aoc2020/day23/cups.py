import utils

class Cups:
    def __init__(self, input_str, is_big=False):
        input_list = [int(x) for x in input_str]
        self.cups = {}
        self.current_cup = input_list[0]
        prev = self.current_cup
        for key in input_list:
            self.cups[prev] = key
            prev = key
        if is_big:
            for key in range(1000001):
                self.cups[prev] = key
                prev = key
        self.cups[prev] = self.current_cup

    def extract(self):
        values = []
        key = self.current_cup
        for _ in range(3):
            values.append(self.cups[key])
            key = self.cups[key]
        self.cups[self.current_cup] = self.cups[key]
        return values

    def play_round(self):
        #pick up the next 3 cups:
        values = self.extract()
        #find next value, which is current_cup.value-1
        destination = self.current_cup - 1 if self.current_cup > 1 else len(self.cups)
        while destination in values:
            destination = destination - 1 if destination > 1 else len(self.cups)
        #reinsert the extracted cups after the destination
        tail = self.cups[destination]
        for val in values:
            self.cups[destination] = val
            destination = val
        self.cups[destination] = tail
        #move current cup by 1
        self.current_cup = self.cups[self.current_cup]

    def play_game(self, num_rounds):
        for i in range(num_rounds):
            if i % 100000 == 0:
                print(i)
            self.play_round()

    def cup_order(self):
        result = []
        current = self.cups[1]
        while current != 1:
            result.append(str(current))
            current = self.cups[current]
        assert len(result) == 8, \
            'only call cup_order with is_big=False'
        return ''.join(result)

    def cup_hash(self):
        first = self.cups[1]
        second = self.cups[first]
        return first * second

def main():
    cups = Cups('253149867')
    cups.play_game(100)
    utils.pretty_print_answer(1, cups.cup_order())
    cups = Cups('253149867', is_big=True)
    cups.play_game(10000000)
    utils.pretty_print_answer(2, cups.cup_hash())

if __name__ == "__main__":
    main()
