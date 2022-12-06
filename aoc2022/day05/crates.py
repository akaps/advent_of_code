import re

regex = r'move (\d+) from (\d) to (\d)'

def read_input():
    return None

def use_input():
    crates = Crates(9)
    crates.insert_crate('D', 1)
    crates.insert_crate('L', 1)
    crates.insert_crate('V', 1)
    crates.insert_crate('T', 1)
    crates.insert_crate('M', 1)
    crates.insert_crate('H', 1)
    crates.insert_crate('F', 1)

    crates.insert_crate('H', 2)
    crates.insert_crate('Q', 2)
    crates.insert_crate('G', 2)
    crates.insert_crate('J', 2)
    crates.insert_crate('C', 2)
    crates.insert_crate('T', 2)
    crates.insert_crate('N', 2)
    crates.insert_crate('P', 2)

    crates.insert_crate('R', 3)
    crates.insert_crate('S', 3)
    crates.insert_crate('D', 3)
    crates.insert_crate('M', 3)
    crates.insert_crate('P', 3)
    crates.insert_crate('H', 3)

    crates.insert_crate('L', 4)
    crates.insert_crate('B', 4)
    crates.insert_crate('V', 4)
    crates.insert_crate('F', 4)

    crates.insert_crate('N', 5)
    crates.insert_crate('H', 5)
    crates.insert_crate('G', 5)
    crates.insert_crate('L', 5)
    crates.insert_crate('Q', 5)

    crates.insert_crate('W', 6)
    crates.insert_crate('B', 6)
    crates.insert_crate('D', 6)
    crates.insert_crate('G', 6)
    crates.insert_crate('R', 6)
    crates.insert_crate('M', 6)
    crates.insert_crate('P', 6)

    crates.insert_crate('G', 7)
    crates.insert_crate('M', 7)
    crates.insert_crate('N', 7)
    crates.insert_crate('R', 7)
    crates.insert_crate('C', 7)
    crates.insert_crate('H', 7)
    crates.insert_crate('L', 7)
    crates.insert_crate('Q', 7)

    crates.insert_crate('C', 8)
    crates.insert_crate('L', 8)
    crates.insert_crate('W', 8)

    crates.insert_crate('R', 9)
    crates.insert_crate('D', 9)
    crates.insert_crate('L', 9)
    crates.insert_crate('Q', 9)
    crates.insert_crate('J', 9)
    crates.insert_crate('Z', 9)
    crates.insert_crate('M', 9)
    crates.insert_crate('T', 9)
    assert crates.topmost() == 'FPHFQPQWT'
    return crates

class Crates:
    def __init__(self, num_stacks):
        self.stacks = [[] for _ in range(num_stacks)]

    #ONES BASED INDEXING
    def insert_crate(self, crate_name, index):
        self.stacks[index - 1].append(crate_name)

    def __str__(self):
        return str(self.stacks)

    def topmost(self):
        result = ''
        for stack in self.stacks:
            result += stack[-1] if stack else ' '
        return result

    def prepare_instructions(self):
        file_input = open('input.txt')
        lines = [s.strip() for s in file_input.readlines()]
        lines = lines [10:]
        return lines


    def run_instructions(self):
        lines = self.prepare_instructions()

        for line in lines:
            before = self.topmost()
            amount, source, dest = [int(x) for x in re.search(regex, line).groups()]
            for _ in range(amount):
                box = self.stacks[source - 1].pop()
                self.stacks[dest - 1].append(box)

    def run_instructions9001(self):
        lines = self.prepare_instructions()

        for line in lines:
            amount, source, dest = [int(x) for x in re.search(regex, line).groups()]
            temp = []
            for _ in range(amount):
                temp.append(self.stacks[source - 1].pop())
            while temp:
                self.stacks[dest - 1].append(temp.pop())

def main():
    crates = Crates(3)
    crates.insert_crate('C', 1)
    crates.insert_crate('M', 2)
    crates.insert_crate('Z', 3)
    assert crates.topmost() == 'CMZ'

    crates = use_input()
    crates.run_instructions()
    print('Part 1: ', crates.topmost())

    crates = use_input()
    crates.run_instructions9001()
    print('Part 2: ', crates.topmost())

if __name__ == '__main__':
    main()
