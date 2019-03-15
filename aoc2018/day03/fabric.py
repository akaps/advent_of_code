import numpy
import re #regular expression, duh

def parse_lines(lines):
    """
    structure:
    #<ID> @ <X>,<Y>: <width>,<height>
    """
    res = []
    for line in lines:
        line = line.strip()
        processed = re.split('@|,|:|x', line)
        processed[0] = processed[0][1:]
        processed = list(map(int, processed))
        res.append(processed)
    return res

class Overlap:
    def __init__(self, file_name):
        self.fabric = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]
        file = open(file_name, 'r')
        self.cuts = parse_lines(file.readlines())
        file.close()
        self.process_cuts()

    def process_cuts(self):
        #cut format is:
        #0, index
        #1, x
        #2, y
        #3, width
        #4, height
        for cut in self.cuts:
            for i in range(cut[1], cut[1] + cut[3]):
                for j in range(cut[2], cut[2] + cut[4]):
                    if not self.fabric[i][j]:
                        self.fabric[i][j] = cut[0]
                    else:
                        self.fabric[i][j] = -1

    def overlap(self):
        total = 0
        for row in self.fabric:
            for col in row:
                if col == -1:
                    total += 1
        return total

    def unoverlapped(self):
        for cut in self.cuts:
            is_isolated = True
            for i in range(cut[1], cut[1] + cut[3]):
                for j in range(cut[2], cut[2] + cut[4]):
                    if is_isolated and self.fabric[i][j] != cut[0]:
                        is_isolated = False
            if is_isolated:
                return cut[0]

res = Overlap('input.txt')
print('overlapped area is: {overlapped}'.format(overlapped = res.overlap()))
print('unoverlapped id is: {unoverlapped}'.format(unoverlapped = res.unoverlapped()))
