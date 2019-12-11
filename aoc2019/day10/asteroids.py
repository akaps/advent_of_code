import math
import copy
import numpy
import utils

ASTEROID = '#'

def calculate_distance(point_a, point_b):
    x = (point_a[0] - point_b[0]) ** 2
    y = (point_a[1] - point_b[1]) ** 2
    return math.sqrt(x + y)

def calculate_angle(point_a, point_b):
    '''
    returns an angle with angle 0 to the north (pi/2 radians in unit circle)
    '''
    rise = point_b[1] - point_a[1]
    run = point_b[0] - point_a[0]
    return (math.degrees(math.atan2(rise, run)) + 450) % 360

def shoot_asteroids(asteroids_by_angle, stop):
    angles = sorted(asteroids_by_angle.keys())
    _asteroids_by_angle = copy.deepcopy(asteroids_by_angle)
    current_index = 0
    count = 0
    current_asteroid = None
    while angles and count < stop:
        index_mod = 1
        current_angle = angles[current_index]
        current_asteroid = _asteroids_by_angle[current_angle].pop(0)
        if not _asteroids_by_angle[current_angle]:
            angles.remove(current_angle)
            index_mod = 0
        count += 1
        current_index = (current_index + index_mod) % len(angles) if angles else 0
    return current_asteroid

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
            processed_angles = self.asteroid_angles_for_position(point)
            seen = len(processed_angles)
            if seen > most_seen:
                most_seen = seen
                most_seen_pos = point
        return most_seen_pos, most_seen

    def asteroid_angles_for_position(self, point):
        processed_angles = {}
        for other_point in self.asteroids:
            if other_point != point:
                curr_angle = calculate_angle(point, other_point)
                if curr_angle not in processed_angles:
                    processed_angles[curr_angle] = []
                processed_angles[curr_angle].append(other_point)
        for key, asteroids in processed_angles.items():
            processed_angles[key] = sorted(
                asteroids,
                key=lambda asteroid: calculate_distance(point, asteroid))
        return processed_angles

#angle asserts
CENTER = (1, 1)
assert calculate_angle(CENTER, (1, 0)) == 0
assert calculate_angle(CENTER, (2, 0)) == 45
assert calculate_angle(CENTER, (2, 1)) == 90
assert calculate_angle(CENTER, (2, 2)) == 135
assert calculate_angle(CENTER, (1, 2)) == 180
assert calculate_angle(CENTER, (0, 2)) == 225
assert calculate_angle(CENTER, (0, 1)) == 270
assert calculate_angle(CENTER, (0, 0)) == 315

#problem asserts
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
PROBLEM_POS, PROBLEM_MOST = PROBLEM.most_visible_asteroids()
assert PROBLEM_MOST == 347
utils.pretty_print_answer(1, PROBLEM_MOST)

ANGLES = SAMPLE.asteroid_angles_for_position((11, 13))
assert shoot_asteroids(ANGLES, 1) == (11, 12)
assert shoot_asteroids(ANGLES, 2) == (12, 1)
assert shoot_asteroids(ANGLES, 3) == (12, 2)
assert shoot_asteroids(ANGLES, 10) == (12, 8)
assert shoot_asteroids(ANGLES, 20) == (16, 0)
assert shoot_asteroids(ANGLES, 50) == (16, 9)
assert shoot_asteroids(ANGLES, 100) == (10, 16)
assert shoot_asteroids(ANGLES, 199) == (9, 6)
assert shoot_asteroids(ANGLES, 200) == (8, 2)
assert shoot_asteroids(ANGLES, 201) == (10, 9)
assert shoot_asteroids(ANGLES, 299) == (11, 1)

ANGLES = PROBLEM.asteroid_angles_for_position(PROBLEM_POS)
POS_200 = shoot_asteroids(ANGLES, 200)
ANSWER = POS_200[0] * 100 + POS_200[1]
utils.pretty_print_answer(2, ANSWER)
