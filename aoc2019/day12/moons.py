import re
import math
import utils

X = 'x'
Y = 'y'
Z = 'z'

def process_line(line):
    m = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', line)
    return [int(x) for x in m.groups()]

def format_coordinate(coordinate):
    x_coord, y_coord, z_coord = coordinate.values()
    return '<x={x}, y={y}, z={z}>'.format(x=x_coord, y=y_coord, z=z_coord)

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
        return 'pos={pos}, vel ={vel}'.format(
            pos=format_coordinate(self.position),
            vel=format_coordinate(self.velocity))

    def axis_data(self, axis):
        return self.position[axis], self.velocity[axis]

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

    def repeats_axis(self, axis):
        steps = 0
        previous = {}
        pos1, vel1 = self.moons[0].axis_data(axis)
        pos2, vel2 = self.moons[1].axis_data(axis)
        pos3, vel3 = self.moons[2].axis_data(axis)
        pos4, vel4 = self.moons[3].axis_data(axis)
        found = False
        while not found:
            if pos1 in previous:
                if vel1 in previous[pos1]:
                    if pos2 in previous[pos1][vel1]:
                        if vel2 in previous[pos1][vel1][pos2]:
                            if pos3 in previous[pos1][vel1][pos2][vel2]:
                                if vel3 in previous[pos1][vel1][pos2][vel2][pos3]:
                                    if pos4 in previous[pos1][vel1][pos2][vel2][pos3][vel3]:
                                        if vel4 in previous[pos1][vel1][pos2][vel2][pos3][vel3][pos4]:
                                            return steps
                                        else:
                                            previous[pos1][vel1][pos2][vel2][pos3][vel3][pos4].append(vel4)
                                    else:
                                        previous[pos1][vel1][pos2][vel2][pos3][vel3][pos4] = [vel4]
                                else:
                                    previous[pos1][vel1][pos2][vel2][pos3][vel3] = {}
                                    previous[pos1][vel1][pos2][vel2][pos3][vel3][pos4] = [vel4]
                            else:
                                previous[pos1][vel1][pos2][vel2][pos3] = {}
                                previous[pos1][vel1][pos2][vel2][pos3][vel3] = {}
                                previous[pos1][vel1][pos2][vel2][pos3][vel3][pos4] = [vel4]
                        else:
                            previous[pos1][vel1][pos2][vel2] = {}
                            previous[pos1][vel1][pos2][vel2][pos3] = {}
                            previous[pos1][vel1][pos2][vel2][pos3][vel3] = {}
                            previous[pos1][vel1][pos2][vel2][pos3][vel3][pos4] = [vel4]
                    else:
                        previous[pos1][vel1][pos2] = {}
                        previous[pos1][vel1][pos2][vel2] = {}
                        previous[pos1][vel1][pos2][vel2][pos3] = {}
                        previous[pos1][vel1][pos2][vel2][pos3][vel3] = {}
                        previous[pos1][vel1][pos2][vel2][pos3][vel3][pos4] = [vel4]
                else:
                    previous[pos1][vel1] = {}
                    previous[pos1][vel1][pos2] = {}
                    previous[pos1][vel1][pos2][vel2] = {}
                    previous[pos1][vel1][pos2][vel2][pos3] = {}
                    previous[pos1][vel1][pos2][vel2][pos3][vel3] = {}
                    previous[pos1][vel1][pos2][vel2][pos3][vel3][pos4] = [vel4]
            else:
                previous[pos1] = {}
                previous[pos1][vel1] = {}
                previous[pos1][vel1][pos2] = {}
                previous[pos1][vel1][pos2][vel2] = {}
                previous[pos1][vel1][pos2][vel2][pos3] = {}
                previous[pos1][vel1][pos2][vel2][pos3][vel3] = {}
                previous[pos1][vel1][pos2][vel2][pos3][vel3][pos4] = [vel4]
            self.update()
            pos1, vel1 = self.moons[0].axis_data(axis)
            pos2, vel2 = self.moons[1].axis_data(axis)
            pos3, vel3 = self.moons[2].axis_data(axis)
            pos4, vel4 = self.moons[3].axis_data(axis)
            steps += 1
            if steps % 100000 == 0:
                print('still calculating... finished {steps} steps'.format(steps=steps))
        return steps

def steps_til_repeat(input_file):
    moons = Moons(input_file)
    x_repeat = moons.repeats_axis(X)
    print('x axis repeats at {repeat}'.format(repeat=x_repeat))
    moons = Moons(input_file)
    y_repeat = moons.repeats_axis(Y)
    print('y axis repeats at {repeat}'.format(repeat=y_repeat))
    moons = Moons(input_file)
    z_repeat = moons.repeats_axis(Z)
    print('z axis repeats at {repeat}'.format(repeat=z_repeat))
    lcm_xy = (x_repeat * y_repeat) // math.gcd(x_repeat, y_repeat)
    lcm = (lcm_xy * z_repeat) // math.gcd(lcm_xy, z_repeat)
    return lcm

SAMPLE1 = Moons('sample1.txt')
for _ in range(10):
    SAMPLE1.update()
assert SAMPLE1.total_energy() == 179

PROBLEM = Moons('input.txt')
for _ in range(1000):
    PROBLEM.update()
ANSWER = PROBLEM.total_energy()
assert ANSWER == 9958
utils.pretty_print_answer(1, ANSWER)

print('testing steps for sample 1')
STEPS = steps_til_repeat('sample1.txt')
assert STEPS == 2772

print('testing steps for sample2')
STEPS = steps_til_repeat('sample2.txt')
assert STEPS == 4686774924

print('calculating solution for part 2')
STEPS = steps_til_repeat('input.txt')
#assert STEPS ==
utils.pretty_print_answer(2, STEPS)
