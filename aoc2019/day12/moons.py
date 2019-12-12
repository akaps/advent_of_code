import re
import utils

X = 'x'
Y = 'y'
Z = 'z'

def process_line(line):
    m = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', line)
    return [int(x) for x in m.groups()]

def format_coordinate(coordinate):
    x, y, z = coordinate
    return '<x={x}, y={y}, z={z}>'.format(x=x, y=y, z=z)

class Moon:
    def __init__(self, x, y, z):
        self.position = {X: x, Y: y, Z: z}
        self.velocity = {X: 0, Y: 0, Z: 0}

    def update_velocity(self, other_moon):
        for key in self.position:
            if self.position[key] < other_moon.position[key]:
                self.velocity[key] += 1
            elif self.position[key] > other_moon.position[key]:
                self.velocity[key] -= 1

    def update_position(self):
        for key in self.position:
            self.position[key] = self.position[key] + self.velocity[key]

    def potential_energy(self):
        total = 0
        for val in self.position.values():
            total += abs(val)
        return total

    def kinetic_energy(self):
        total = 0
        for val in self.velocity.values():
            total += abs(val)
        return total

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def __repr__(self):
        return 'pos={pos}, vel ={vel}'.format(pos=format_coordinate(self.position), vel=format_coordinate(self.velocity))

class Moons:
    def __init__(self, input_file):
        lines = utils.read_lines(input_file)
        self.moons = []
        for line in lines:
            x, y, z = process_line(line)
            self.moons.append(Moon(x, y, z))

    def update(self):
        for moon in self.moons:
            for other_moon in self.moons:
                moon.update_velocity(other_moon)

        for moon in self.moons:
            moon.update_position()

    def __repr__(self):
        result = [str(x) for x in self.moons]
        return '\n'.join(result).strip()

    def total_energy(self):
        total = 0
        for moon in self.moons:
            total += moon.total_energy()
        return total

SAMPLE1 = Moons('sample1.txt')
for _ in range(10):
    SAMPLE1.update()
assert SAMPLE1.total_energy() == 179

PROBLEM = Moons('input.txt')
for _ in range(1000):
    PROBLEM.update()
utils.pretty_print_answer(1, PROBLEM.total_energy())
