import re

class Checksum:
    def __init__(self, file_name):
        file = open(file_name)
        self.array = self.populate(file.readlines())
        file.close()

    def populate(self, lines):
        res = []
        for line in lines:
            line = line.strip()
            line = re.split(r' |\t', line)
            res.append([int(x) for x in line])
        return res

    def checksum(self):
        total = 0
        for row in self.array:
            minimum = min(row)
            maximum = max(row)
            total += maximum - minimum
        return total

SAMPLE = Checksum('sample.txt')
assert SAMPLE.checksum() == 18

PROBLEM = Checksum('input.txt')
print('Answer to part 1: {ans}'.format(ans=PROBLEM.checksum()))
