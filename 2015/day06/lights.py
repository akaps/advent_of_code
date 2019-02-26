import re
import numpy as np
import utils

class Lights:
    def __init__(self):
        self.reset()

    def reset(self):
        self.lights = np.full((1000, 1000), False)
        self.intensities = np.full((1000, 1000), 0)

    def turn_on(self, from_point, to_point):
        for i in range(from_point[0], to_point[0] + 1):
            for j in range(from_point[1], to_point[1] + 1):
                self.lights[i][j] = True
                self.intensities[i][j] += 1

    def turn_off(self, from_point, to_point):
        for i in range(from_point[0], to_point[0] + 1):
            for j in range(from_point[1], to_point[1] + 1):
                self.lights[i][j] = False
                self.intensities[i][j] = max(0, self.intensities[i][j] - 1)

    def toggle(self, from_point, to_point):
        for i in range(from_point[0], to_point[0] + 1):
            for j in range(from_point[1], to_point[1] + 1):
                self.lights[i][j] = not self.lights[i][j]
                self.intensities[i][j] += 2

    def count_on(self):
        return sum(np.count_nonzero(light_row) for light_row in self.lights)

    def intensity(self):
        return np.sum(self.intensities)

def parse_line(lights, input_line):
    regex = r'^(turn off|turn on|toggle) (\d+),(\d+) through (\d+),(\d+)$'
    action, from_point_x, from_point_y, to_point_x, to_point_y = re.search(regex, input_line).groups()
    from_point = (int(from_point_x), int(from_point_y))
    to_point = (int(to_point_x), int(to_point_y))
    if action == 'turn off':
        lights.turn_off(from_point, to_point)
    elif action == 'turn on':
        lights.turn_on(from_point, to_point)
    elif action == 'toggle':
        lights.toggle(from_point, to_point)

SAMPLE = Lights()
assert SAMPLE.count_on() == 0
parse_line(SAMPLE, 'turn on 0,0 through 999,999')
assert SAMPLE.count_on() == 1000000
SAMPLE.reset()
parse_line(SAMPLE, 'toggle 0,0 through 999,0')
assert SAMPLE.count_on() == 1000
SAMPLE.reset()
parse_line(SAMPLE, 'turn on 0,0 through 999,999')
parse_line(SAMPLE, 'turn off 499,499 through 500,500')
assert SAMPLE.count_on() == 999996

PROBLEM = Lights()
FILE = open('input.txt')
LINES = FILE.readlines()
FILE.close()
for line in LINES:
    parse_line(PROBLEM, line)
utils.pretty_print_answer(1, PROBLEM.count_on())

SAMPLE.reset()
parse_line(SAMPLE, 'turn on 0,0 through 0,0')
assert SAMPLE.intensity() == 1
SAMPLE.reset()
parse_line(SAMPLE, 'toggle 0,0 through 999,999')
assert SAMPLE.intensity() == 2000000

utils.pretty_print_answer(2, PROBLEM.intensity())
