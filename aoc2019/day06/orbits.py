import utils

CENTER = 'COM'
DELIMETER = ')'

YOU = 'YOU'
SAN = 'SAN'

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
            self.add_orbit(center, orbiter)

    def add_orbit(self, center, orbiter):
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

    def _parents_of(self, current):
        if current == CENTER:
            return []
        parent = self.stars[current].parent
        parents = self._parents_of(parent)
        parents.append(parent)
        return parents

    def distance_between(self, start, end):
        start_parents = self._parents_of(start)
        current = self.stars[end].parent
        count = 0
        while current not in start_parents:
            current = self.stars[current].parent
            count += 1
        count += len(start_parents) - start_parents.index(current) - 1
        return count

SAMPLE = Constellation('sample.txt')
DISTANCE = SAMPLE.total_distance()
assert DISTANCE == 42

PROBLEM = Constellation('input.txt')
DISTANCE = PROBLEM.total_distance()
assert DISTANCE == 140608
utils.pretty_print_answer(1, DISTANCE)

SAMPLE.add_orbit('K', YOU)
SAMPLE.add_orbit('I', SAN)
DISTANCE = SAMPLE.distance_between(YOU, SAN)
assert DISTANCE == 4

DISTANCE = PROBLEM.distance_between(YOU, SAN)
assert DISTANCE == 337
utils.pretty_print_answer(2, DISTANCE)
