import utils

class XmasEncryption:
    def __init__(self, file_name):
        lines = [int(x) for x in utils.read_lines(file_name)]
        self.preamble = lines[:25]
        self.to_process = lines[25:]

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

def main():
    encryption = XmasEncryption('aoc2020/day09/input.txt')
    utils.pretty_print_answer(1, encryption.find_part_1())

if __name__ == '__main__':
    main()
