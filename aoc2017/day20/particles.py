import operator
import re
import heapq
from functools import total_ordering
import utils

@total_ordering
class Particle:
    def __init__(self, particle_id, point, vel, accel):
        self.particle_id = particle_id
        self.point = point
        self.vel = vel
        self.accel = accel
        self.is_diverging = False

    def update(self):
        self.vel = tuple(map(operator.add, self.vel, self.accel))
        next_point = tuple(map(operator.add, self.point, self.vel))
        self.is_diverging = distance(next_point) > distance(self.point)
        self.point = next_point

    def distance(self):
        return distance(self.point)

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __eq__(self, other):
        difference = tuple(map(operator.sub, self.point, other.point))
        return difference == (0, 0, 0)

    def __repr__(self):
        return '{id}@p={p},v={v},a={a})'.format(id=self.particle_id, p=self.point, v=self.vel, a=self.accel)

def distance(particle):
    return sum(abs(mag) for mag in particle)

def parse_particles(lines):
    particle_list = []
    for count, line in enumerate(lines):
        coordinates = re.findall(r'-?\d+', line)
        point = tuple(int(x) for x in coordinates[0:3])
        vel = tuple(int(x) for x in coordinates[3:6])
        accel = tuple(int(x) for x in coordinates[6:9])
        particle_list.append(Particle(count, point, vel, accel))
    return particle_list

def find_closest_to_origin(particles):
    while len(particles) > 1:
        for particle in particles:
            particle.update()
        heapq.heapify(particles)
        for point in reversed(particles):
            if point.is_diverging:
                particles.remove(point)
                print('removing {p}, dist of {d}'.format(p=point.particle_id, d=point.distance()))
                break

def perform_collisions(particles):
    all_diverging = False
    while not all_diverging:
        all_diverging = True
        print(len(particles))
        locations = {}
        for particle in particles:
            particle.update()
            if particle.point not in locations:
                locations[particle.point] = [particle]
            else:
                locations[particle.point].append(particle)
            if not particle.is_diverging:
                all_diverging = False
        for particles_at_loc in locations.values():
            if len(particles_at_loc) > 1:
                print('collisions with points {p}'.format(p=particles_at_loc))
                for part in particles_at_loc:
                    particles.remove(part)

a = (2, 3, -4)
b = (0, 0, 0)
c = (-1, -1, -1)
p = Particle('p', a, b, c)
assert p.distance() == 9
p.update()
assert p.distance() == 8

a = Particle('a', (3, 0, 0), (2, 0, 0), (-1, 0, 0))
b = Particle('b', (4, 0, 0), (0, 0, 0), (-2, 0, 0))

file = open('input.txt')
particles = parse_particles(file.readlines())
file.close()
find_closest_to_origin(particles)
utils.pretty_print_answer(1, particles[0].particle_id)

file = open('input.txt')
particles = parse_particles(file.readlines())
file.close()
perform_collisions(particles)
utils.pretty_print_answer(2, len(particles))
