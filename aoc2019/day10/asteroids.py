import math
import numpy
import utils

ASTEROID = '#'

def angle(point_a, point_b):
    rise = point_b[1] - point_a[1]
    run = point_b[0] - point_a[0]
    if run > 0:
        return numpy.arctan(rise/run)
    if run < 0:
        return numpy.arctan(rise/run) - math.pi
    if rise > 0:
        return math.pi / 2
    return -math.pi / 2

class Asteroids:
    def __init__(self, input_file):
        self.asteroids = []
        lines = utils.read_lines(input_file)
        for y, row in enumerate(lines):
            for x, val in enumerate(row):
                if val == ASTEROID:
                    self.asteroids.append((x, y))

    def most_visible_asteroids(self):
        most_seen = 0
        most_seen_pos = None
        for point in self.asteroids:
            processed_angles = self.compute_angles(point)
            seen = len(processed_angles)
            if seen > most_seen:
                most_seen = seen
                most_seen_pos = point
        return most_seen_pos, most_seen

    def compute_angles(self, point):
        processed_angles = set()
        for other_point in self.asteroids:
            if other_point != point:
                curr_angle = angle(point, other_point)
                processed_angles.add(curr_angle)
        return processed_angles

SAMPLE = Asteroids('sample0.txt')
POS, MOST = SAMPLE.most_visible_asteroids()
assert POS == (3, 4)
assert MOST == 8

SAMPLE = Asteroids('sample1.txt')
POS, MOST = SAMPLE.most_visible_asteroids()
assert POS == (5, 8)
assert MOST == 33

SAMPLE = Asteroids('sample2.txt')
POS, MOST = SAMPLE.most_visible_asteroids()
assert POS == (1, 2)
assert MOST == 35

SAMPLE = Asteroids('sample3.txt')
POS, MOST = SAMPLE.most_visible_asteroids()
assert POS == (6, 3)
assert MOST == 41

SAMPLE = Asteroids('sample4.txt')
POS, MOST = SAMPLE.most_visible_asteroids()
assert POS == (11, 13)
assert MOST == 210

PROBLEM = Asteroids('input.txt')
POS, MOST = PROBLEM.most_visible_asteroids()
assert MOST == 347
utils.pretty_print_answer(1, MOST)
