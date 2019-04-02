import copy
from  functools import total_ordering

ELF = 'E'
GOBLIN = 'G'
OPEN = '.'
WALL = '#'

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

DIRECTIONS = {
    UP : (-1, 0),
    DOWN : (1, 0),
    LEFT : (0, 1),
    RIGHT : (0, -1)
}

@total_ordering
class Unit:
    def __init__(self, unit_id, location):
        self.unit_id = unit_id
        self.location = location
        self.hit_points = 200
        self.attack_power = 3

    def __repr__(self):
        return '{loc} has unit {id} with {hp} HP'.format(
            loc=self.location,
            id=self.unit_id,
            hp=self.hit_points
        )

    def __eq__(self, other):
        return self.location == other.location

    def __lt__(self, other):
        if self.location[0] != other.location[0]:
            return self.location[0] < other.location[0]
        return self.location[1] < other.location[1]

    def move(self, targets, current_map):
        in_range = self.in_range(targets, current_map)
        in_range = self.find_reachable(current_map)
        nearest = self.find_nearest(current_map, in_range)
        chosen = self.choose_nearest(nearest)
        self.move_towards(chosen)

class Map:
    def __init__(self, file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        self.map = []
        self.units = []
        self.populate_map(lines)
        self.num_rounds = 0

    def populate_map(self, lines):
        for row, line in enumerate(lines):
            next_row = []
            for col, char in enumerate(line.strip()):
                if char in [GOBLIN, ELF]:
                    next_row.append(OPEN)
                    self.units.append(Unit(char, (row, col)))
                else:
                    next_row.append(char)
            self.map.append(next_row)

    def perform_round(self, targets):
        self.units.sort()
        current_map = self.current_map
        for unit in self.units:
            unit.move(targets, current_map)
            if unit.can_attack(targets):
                attacked = unit.attacks_whom(targets)
                attacked.hit_points -= 3
                if attacked.hit_points <= 0:
                    self.units.remove(attacked)

    def run_simulation(self):
        targets = self.generate_targets()
        while len(targets) > 1:
            self.perform_round(targets)
            targets = self.generate_targets()
            self.num_rounds += 1

    def generate_targets(self):
        result = {GOBLIN : [], ELF : []}
        for unit in self.units:
            result[unit.unit_id].append(unit)
        result[GOBLIN].sort()
        result[ELF].sort()
        return result

    def __repr__(self):
        current_map = self.current_map()
        result = []
        for line in current_map:
            result.append(''.join(line))
        result.extend([str(unit) for unit in self.units])
        result = '\n'.join(result)
        return result

    def outcome(self):
        total = sum([unit.hit_points for unit in self.units])
        return self.num_rounds * total

    def current_map(self):
        map_copy = copy.deepcopy(self.map)
        for unit in self.units:
            loc = unit.location
            map_copy[loc[0]][loc[1]] = unit.unit_id
        return map_copy

SAMPLE = Map('sample_order.txt')
SAMPLE.run_simulation()
print(SAMPLE.outcome())
