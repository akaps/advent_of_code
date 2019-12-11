import utils

CENTER = 'COM'
DELIMETER = ')'

class Star:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return '{data} has parent {parent} and children {children}'.format(
            data=self.data,
            parent=self.parent,
            children=self.children
        )

class Constellation:
    def __init__(self, input_file):
        self.stars = {}
        self.initialize_orbits(utils.read_lines(input_file))

    def initialize_orbits(self, orbit_pairs):
        for pair in orbit_pairs:
            center, orbiter = pair.split(DELIMETER)
            if center not in self.stars:
                self.stars[center] = Star(center)
            self.stars[center].add_child(orbiter)
            if orbiter not in self.stars:
                self.stars[orbiter] = Star(orbiter)
            self.stars[orbiter].parent = center

    def total_distance(self):
        return self._total_distance(CENTER, 0)

    def _total_distance(self, current_node, current_depth):
        total = current_depth
        for child in self.stars[current_node].children:
            total += self._total_distance(child, current_depth + 1)
        return total

SAMPLE = Constellation('sample.txt')
DISTANCE = SAMPLE.total_distance()
assert DISTANCE == 42

PROBLEM = Constellation('input.txt')
utils.pretty_print_answer(1, PROBLEM.total_distance())
