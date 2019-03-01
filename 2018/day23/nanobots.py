import re
import utils as utils

class Nanobots:
    def __init__(self, lines):
        self.radius = -1
        self.center = None
        self.nanobots = []
        for line in lines:
            x, y, z, rad = map(int, re.findall('-?\d+', line))
            if rad > self.radius:
                self.radius = rad
                self.center = (x, y, z)
            self.nanobots.append((x, y, z))

    def within_cluster(self):
        total = 0
        for nanobot in self.nanobots:
            dist = utils.manhattan_distance(nanobot, self.center)
            if dist <= self.radius:
                total += 1
        return total

def determine_cluster(file_name):
    file = open(file_name, 'r')
    nanobots = Nanobots(file.readlines())
    file.close()
    return nanobots.within_cluster()

assert determine_cluster('sample.txt') == 7
ANSWER = determine_cluster('input.txt')
print('Answer to part 1: {ans}'.format(ans=ANSWER))
