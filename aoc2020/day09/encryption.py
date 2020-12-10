import utils

class XmasEncryption:
    def __init__(self, file_name):
        self.lines = [int(x) for x in utils.read_lines(file_name)]
        self.preamble = self.lines[:25]
        self.to_process = self.lines[25:]

    def get_window(self):
        window = set()
        for index, x_val in enumerate(self.preamble):
            for y_index in range(index + 1, len(self.preamble)):
                window.add(x_val + self.preamble[y_index])
        return window

    def number_valid(self, number):
        window = self.get_window()
        return number in window

    def adjust_window(self, number):
        self.preamble.pop(0)
        self.preamble.append(number)

    def find_part_1(self):
        for number in self.to_process:
            if not self.number_valid(number):
                return number
            self.adjust_window(number)
        return -1

    def find_weakness(self, weakness):
        for window_length in range(2, len(self.lines)):
            for window_offset in range(0, len(self.lines) - window_length):
                run = self.lines[window_offset: window_offset + window_length]
                candidate = sum(run)
                if candidate == weakness:
                    print(candidate)
                    print(run)
                    run.sort()
                    print(run)
                    return run[0] + run[-1]
        return -1

def main():
    encryption = XmasEncryption('aoc2020/day09/input.txt')
    weakness = encryption.find_part_1()
    utils.pretty_print_answer(1, weakness)
    utils.pretty_print_answer(2, encryption.find_weakness(weakness))

if __name__ == '__main__':
    main()
