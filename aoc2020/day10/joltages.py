from collections import defaultdict
import utils

class Jolts:
    def __init__(self, file_name):
        self.joltages = read_joltages(file_name)
        self.sub_answers = {}

    def part_1(self):
        diffs = defaultdict(lambda: 0)
        for current_index, current_joltage in enumerate(self.joltages):
            if current_index + 1 < len(self.joltages):
                diff = difference(current_joltage, self.joltages[current_index + 1])
                diffs[diff] += 1
        return diffs

    def all_connections(self):
        connections = {}
        for current_index, current_joltage in enumerate(self.joltages):
            connections[current_joltage] = []
            for next_index in range(current_index + 1, len(self.joltages)):
                diff = difference(current_joltage, self.joltages[next_index])
                if diff <= 3:
                    connections[current_joltage].append(self.joltages[next_index])
                else:
                    break
        return connections

    def count_connections(self):
        self.sub_answers = {self.joltages[-1]: 1}
        return self.count_connections_helper(0)

    #does not add the 16 value to 15...
    def count_connections_helper(self, jolt_index):
        current_value = self.joltages[jolt_index]
        if current_value in self.sub_answers:
            return self.sub_answers[current_value]
        result = 0
        for mod in range(1, 4):
            next_value = current_value + mod
            if next_value in self.joltages:
                result += self.count_connections_helper(self.joltages.index(next_value))
        assert result > 0, 'Did not find a connection for {val}'.format(val=current_value)
        self.sub_answers[current_value] = result
        return result

def difference(num1, num2):
    return num2 - num1

def read_joltages(file_name):
    lines = [int(x) for x in utils.read_lines(file_name)]
    lines.sort()
    lines.insert(0, 0)
    lines.append(lines[-1] + 3)
    return lines

def main():
    jolts = Jolts('aoc2020/day10/input.txt')
    diffs = jolts.part_1()
    utils.pretty_print_answer(1, diffs[1] * diffs[3])
    utils.pretty_print_answer(2, jolts.count_connections())

if __name__ == "__main__":
    main()
