import re

class Checksum:
    def __init__(self, file_name):
        file = open(file_name)
        self.array = populate(file.readlines())
        file.close()

    def checksum(self):
        total = 0
        for row in self.array:
            minimum = min(row)
            maximum = max(row)
            total += maximum - minimum
        return total

    def divisible(self):
        total = 0
        for row in self.array:
            num, other = find_divisible(row)
            total += num // other
        return total

def populate(lines):
    res = []
    for line in lines:
        line = line.strip()
        line = re.split(r' |\t', line)
        res.append([int(x) for x in line])
    return res

def find_divisible(row):
    row.sort()
    for num in row:
        for other_num in row:
            if num % other_num == 0 and num != other_num:
                return num, other_num
    return -1, -1

SAMPLE = Checksum('sample.txt')
assert SAMPLE.checksum() == 18

PROBLEM = Checksum('input.txt')
print('Answer to part 1: {ans}'.format(ans=PROBLEM.checksum()))

SAMPLE = Checksum('sample2.txt')
assert SAMPLE.divisible() == 9
print('Answer to part 2: {ans}'.format(ans=PROBLEM.divisible()))
