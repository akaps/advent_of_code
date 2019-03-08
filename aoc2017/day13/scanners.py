import re

class Scanner:
    def __init__(self, depth):
        self.depth = depth
        self.scanner = 0
        self.dir = 1 # positive to go down, negative to go up

    def update_scanner(self):
        if self.scanner +self.dir < 0 or self.scanner +self.dir == self.depth:
            self.dir *= -1
        self.scanner += self.dir

class Scanners:
    def __init__(self, file_name):
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()
        self.scanners = {}
        self.populate_scanners(lines)

    def populate_scanners(self, lines):
        for line in lines:
            layer, depth = re.split(r': ', line)
            layer = int(layer)
            depth = int(depth)
            self.scanners[layer] = Scanner(depth)

    def run(self):
        catches = 0
        max_t = max(self.scanners.keys()) + 1
        for t in range(max_t):
            if t in self.scanners and self.scanners[t].scanner == 0:
                print('Caught at time {t} with depth {d}'.format(t=t, d=self.scanners[t].depth))
                catches += t * self.scanners[t].depth
            for scanner in self.scanners.values():
                scanner.update_scanner()
        return catches

SAMPLE = Scanners('sample.txt')
assert SAMPLE.run() == 24

PROBLEM = Scanners('input.txt')
print('Answer for part 1: {ans}'.format(ans=PROBLEM.run()))
