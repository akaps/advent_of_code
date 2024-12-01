class ListPairs:
    def __init__(self, file_name):
        self.left_list = []
        self.right_list = []

        lines = open(file_name, 'r').readlines()
        for line in lines:
            left, right = [int(x) for x in line.strip().split()]
            self.left_list.append(left)
            self.right_list.append(right)
        self.left_list.sort()
        self.right_list.sort()

    def sum_diffs(self):
        sum_diff = 0
        for index, val in enumerate(self.left_list):
            sum_diff += abs(val - self.right_list[index])
        return sum_diff

    def sum_occurences(self):
        sum_occ = 0
        for val in self.left_list:
            sum_occ += val * self.right_list.count(val)
        return sum_occ

def main():
    sample = ListPairs('aoc2024/day01/sample.txt')
    input = ListPairs('aoc2024/day01/input.txt')
    assert sample.sum_diffs() == 11
    print('Part 1:', input.sum_diffs())

    assert sample.sum_occurences() == 31
    print('Part 2:', input.sum_occurences())

if __name__ == "__main__":
    main()
