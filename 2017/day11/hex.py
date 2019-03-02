import re

class Vector:
    def __init__(self):
        self.x, self.y, self.z = (0,0,0)
        self.furthest = 0

    def move(self, dir):
        if dir == 'n':
            self.y += 1
            self.z -= 1
        elif dir == 's':
            self.y -= 1
            self.z += 1
        elif dir == 'ne':
            self.x += 1
            self.z -= 1
        elif dir == 'sw':
            self.x -= 1
            self.z += 1
        elif dir == 'nw':
            self.x -= 1
            self.y += 1
        elif dir == 'se':
            self.x += 1
            self.y -= 1
        else:
            print('you fucked up...')

    def move_all(self, dirs):
        self.furthest = 0
        for dir in re.split(',', dirs):
            self.move(dir)
            if self.distance() > self.furthest:
                self.furthest = self.distance()

    def distance(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) // 2

    def __repr__(self):
        return '({x}, {y}, {z})'.format(x=self.x, y=self.y, z=self.z)

SAMPLE = Vector()
SAMPLE.move_all('ne,ne,ne')
print(SAMPLE)
print(SAMPLE.distance())
SAMPLE = Vector()
SAMPLE.move_all('ne,ne,sw,sw')
print(SAMPLE)
print(SAMPLE.distance())
SAMPLE = Vector()
SAMPLE.move_all('ne,ne,s,s')
print(SAMPLE)
print(SAMPLE.distance())
SAMPLE = Vector()
SAMPLE.move_all('se,sw,se,sw,sw')
print(SAMPLE)
print(SAMPLE.distance())

file = open('input.txt')
line = file.readline().strip()
file.close()
PROBLEM = Vector()
PROBLEM.move_all(line)
print(PROBLEM)
print(PROBLEM.distance())
print(PROBLEM.furthest)
