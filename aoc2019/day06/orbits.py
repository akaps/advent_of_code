import utils

CENTER = 'COM'
DELIMETER = ')'

class Constellation:
    def __init__(self, input_file):
        self.orbits = {}
        self.initialize_orbits(utils.read_lines(input_file))

    def initialize_orbits(self, orbit_pairs):
        self.orbits[CENTER] = []
        for pair in orbit_pairs:
            key, val = pair.split(DELIMETER)
            self.orbits[val] = []
            if key in self.orbits:
                self.orbits[key].append(val)

    def total_distance(self):
        return self._total_distance(CENTER, 0)

    def _total_distance(self, current_node, current_depth):
        total = current_depth
        for child in self.orbits[current_node]:
            total += self._total_distance(child, current_depth + 1)
        return total

SAMPLE = Constellation('sample.txt')
DISTANCE = SAMPLE.total_distance()
assert DISTANCE == 42

PROBLEM = Constellation('input.txt')
utils.pretty_print_answer(1, PROBLEM.total_distance())
