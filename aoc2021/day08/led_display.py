SPACE = ' '
PIPE = '|'
simple_lens = [2, 3, 4, 7]

class LED:
    def __init__(self, line):
        input, output = [s.strip() for s in line.split(PIPE)]
        self.inputs = input.split(SPACE)
        self.outputs = output.split(SPACE)

    def simple_count(self):
        total = 0
        for output in self.outputs:
            if len(output) in simple_lens:
                total += 1
        return total

class Displays:
    def __init__(self, file_name):
        file_input = open(file_name, 'r')
        self.leds = [LED(line) for line in file_input.readlines()]
        file_input.close()

    def count_simple(self):
        total = 0
        for display in self.leds:
            total += display.simple_count()
        return total

def main():
    sample = Displays('aoc2021/day08/sample.txt')
    assert sample.count_simple() == 26

    problem = Displays('aoc2021/day08/input.txt')
    print('Part 1:', problem.count_simple())

if __name__ == '__main__':
    main()
