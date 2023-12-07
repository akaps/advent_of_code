import math
import re

class Boat:
    def __init__(self, time, distance):
        self.time = int(time)
        self.distance = int(distance)

    def ways_to_win(self):
        #find roots of y=-x^2 + (time * x) -distance
        #(-b +/- sqrt(b^2-4ac))/2a
        square_root = math.sqrt((self.time ** 2) - (4 * self.distance))
        roots = [(-self.time + square_root) / -2, (-self.time - square_root) / -2]
        return math.floor(max(roots) - 1e-5) - math.ceil(min(roots) + 1e-5) + 1

class Races:
    def __init__(self, file_name):
        lines = open(file_name, encoding='utf-8')

        self.boats = []

        times = re.findall(r'\d+', lines.readline())
        distances = re.findall(r'\d+', lines.readline())
        for index, time in enumerate(times):
            self.boats.append(Boat(time, distances[index]))

    def ways_to_win(self):
        ways = []
        for race in self.boats:
            ways.append(race.ways_to_win())
        return math.prod(ways)

def main():
    sample = Races('aoc2023/day06/sample.txt')
    assert sample.ways_to_win() == 288
    boats = Races('aoc2023/day06/input.txt')
    print('Answer to Part 1:', boats.ways_to_win())

    sample = Races('aoc2023/day06/sample_kerned.txt')
    assert sample.ways_to_win() == 71503
    boats = Races('aoc2023/day06/input_kerned.txt')
    print('Answer to Part 1:', boats.ways_to_win())

if __name__ == '__main__':
    main()
