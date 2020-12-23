import utils

class Cup:
    def __init__(self, cup_number):
        self.value = cup_number
        self.next = None

class Cups:
    def __init__(self, input_str, is_big=False):
        input_list = [int(x) for x in input_str]
        self.current_cup = Cup(input_list[0])
        runner = self.current_cup
        self.length = 9
        for val in input_list[1:]:
            runner.next = Cup(val)
            runner = runner.next
        if is_big:
            for val in range(10, 1000001):
                runner.next = Cup(val)
                runner = runner.next
            self.length = 1000000
        runner.next = self.current_cup

    def extract(self):
        values = []
        head = self.current_cup.next
        runner = head
        for _ in range(3):
            values.append(runner.value)
            runner = runner.next
        self.current_cup.next = runner
        return values, head

    def play_round(self):
        #pick up the next 3 cups:
        values, extracted = self.extract()
        #find next value, which is current_cup.value-1
        destination = self.current_cup.value - 1 if self.current_cup.value > 1 else self.length
        while destination in values:
            destination = destination - 1 if destination > 1 else self.length
        runner = self.current_cup
        while runner.value != destination:
            runner = runner.next
        #reinsert the extracted cups after the destination
        extracted.next.next.next = runner.next
        runner.next = extracted
        #move current cup by 1
        self.current_cup = self.current_cup.next

    def play_game(self, num_rounds):
        for i in range(num_rounds):
            if i % 1 == 0:
                print('round', i)
            self.play_round()

    def cup_order(self):
        result = []
        runner = self.current_cup
        while runner.value != 1:
            runner = runner.next
        runner = runner.next
        while runner.value != 1:
            result.append(str(runner.value))
            runner = runner.next
        assert len(result) == 8
        return ' '.join(result)

    def cup_hash(self):
        runner = self.current_cup
        while runner.value != 1:
            runner = runner.next
        return runner.next.value * runner.next.next.value

def main():
    cups = Cups('253149867')
    cups.play_game(100)
    utils.pretty_print_answer(1, cups.cup_order())
    cups = Cups('253149867', is_big=True)
    cups.play_game(10000000)
    print(cups.cup_order())
    utils.pretty_print_answer(2, cups.cup_hash())

if __name__ == "__main__":
    main()
