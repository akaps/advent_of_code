import re
import numpy

def extrapolate_sequence(sequence: list[int], forwards:bool=True):
    tail_differences = []
    head_differences = []
    while sequence[-1] != 0:
        tail_differences.append(sequence[-1])
        head_differences.append(sequence[0])
        sequence = numpy.diff(sequence)
    if forwards:
        return sum(tail_differences)

    diff = 0
    for i in head_differences[1:]:
        diff -= i
    return head_differences[0] + diff

class Oasis:
    def __init__(self, file_name):
        lines = open(file_name, encoding='utf-8').readlines()
        self.sequences = []
        for line in lines:
            self.sequences.append([int(x) for x in re.findall(r'-?\d+', line)])

    def extrapolate_values(self, forwards:bool=True):
        total = 0
        for sequence in self.sequences:
            total += extrapolate_sequence(sequence, forwards)
        return total

def main():
    assert extrapolate_sequence([0, 3, 6, 9, 12, 15]) == 18
    assert extrapolate_sequence([1, 3, 6, 10, 15, 21]) == 28
    assert extrapolate_sequence([10, 13, 16, 21, 30, 45]) == 68
    sample = Oasis('aoc2023/day09/sample.txt')
    assert sample.extrapolate_values() == 114

    oasis = Oasis('aoc2023/day09/input.txt')
    print('Answer to part 1: ', oasis.extrapolate_values())

    assert extrapolate_sequence([0, 3, 6, 9, 12, 15], forwards=False) == -3
    assert extrapolate_sequence([1, 3, 6, 10, 15, 21], forwards=False) == 0
    assert extrapolate_sequence([10, 13, 16, 21, 30, 45], forwards=False) == 5
    assert sample.extrapolate_values() == 2
    print('Answer to part 2: ', oasis.extrapolate_values(forwards=False))

if __name__ == '__main__':
    main()
