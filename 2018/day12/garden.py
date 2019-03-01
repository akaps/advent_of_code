from collections import deque
import re

DEAD = '.'
ALIVE = '#'

class Rule:
    def __init__(self, rule):
        self.matching, self.result = re.split(r' => ', rule.strip())

    def matches(self, pots, index):
        check = []
        if index == -1:
            check = ['.', '.', '.']
            check.extend(pots[0 : 2])
        elif index == 0:
            check = ['.', '.']
            check.extend(pots[0 : 3])
        elif index == 1:
            check = ['.']
            check.extend(pots[0 : 4])
        elif index == len(pots) - 2:
            check.extend(pots[index - 2 : index + 3])
            check.append('.')
        elif index == len(pots) - 1:
            check.extend(pots[index - 2 : index + 3])
            check.extend(['.', '.'])
        elif index == len(pots):
            check.extend(pots[index - 2 : index + 3])
            check.extend(['.', '.', '.'])
        else:
            check = pots[index - 2 : index + 3]
        return ''.join(check) == self.matching

    def __repr__(self):
        return str([self.matching, self.result])

class Garden:
    def __init__(self, file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        self.pots = self.initialize_pots(lines[0])
        self.rules = self.initialize_rules(lines[2:])
        self.initial_loc = 0

    def initialize_pots(self, line):
        return list(re.search('([.#]+)', line)[0])

    def initialize_rules(self, rules):
        return [Rule(rule) for rule in rules]

    def grow(self):
        next_generation = []
        #check first index...
        for rule in self.rules:
            if rule.matches(self.pots, -1) and rule.result == '#':
                next_generation.append(rule.result)
                self.initial_loc += 1
        for index in enumerate(self.pots):
            for rule in self.rules:
                if rule.matches(self.pots, index[0]):
                    next_generation.append(rule.result)
        #check last index...
        for rule in self.rules:
            if rule.matches(self.pots, len(self.pots)) and rule.result == '#':
                next_generation.append(rule.result)
        self.pots = next_generation

    def score(self):
        total = 0
        for pot in enumerate(self.pots):
            if pot[1] == ALIVE:
                total += pot[0] - self.initial_loc
        return total

SAMPLE = Garden('sample.txt')
assert SAMPLE.pots == list('#..#.#..##......###...###')
SAMPLE.grow() #1
assert SAMPLE.pots == list('#...#....#.....#..#..#..#')
SAMPLE.grow() #2
assert SAMPLE.pots == list('##..##...##....#..#..#..##')
SAMPLE.grow() #3
assert SAMPLE.pots == list('#.#...#..#.#....#..#..#...#')
SAMPLE.grow() #4
assert SAMPLE.pots == list('.#.#..#...#.#...#..#..##..##')
SAMPLE.grow() #5
assert SAMPLE.pots == list('..#...##...#.#..#..#...#...#')
SAMPLE.grow() #6
assert SAMPLE.pots == list('..##.#.#....#...#..##..##..##')
SAMPLE.grow() #7
assert SAMPLE.pots == list('.#..###.#...##..#...#...#...#')
SAMPLE.grow() #8
assert SAMPLE.pots == list('.#....##.#.#.#..##..##..##..##')
SAMPLE.grow() #9
assert SAMPLE.pots == list('.##..#..#####....#...#...#...#')
SAMPLE.grow() #10
assert SAMPLE.pots == list('#.#..#...#.##....##..##..##..##')
SAMPLE.grow() #11
assert SAMPLE.pots == list('.#...##...#.#...#.#...#...#...#')
SAMPLE.grow() #12
assert SAMPLE.pots == list('.##.#.#....#.#...#.#..##..##..##')
SAMPLE.grow() #13
assert SAMPLE.pots == list('#..###.#....#.#...#....#...#...#')
SAMPLE.grow() #14
assert SAMPLE.pots == list('#....##.#....#.#..##...##..##..##')
SAMPLE.grow() #15
assert SAMPLE.pots == list('##..#..#.#....#....#..#.#...#...#')
SAMPLE.grow() #16
assert SAMPLE.pots == list('#.#..#...#.#...##...#...#.#..##..##')
SAMPLE.grow() #17
assert SAMPLE.pots == list('.#...##...#.#.#.#...##...#....#...#')
SAMPLE.grow() #18
assert SAMPLE.pots == list('.##.#.#....#####.#.#.#...##...##..##')
SAMPLE.grow() #19
assert SAMPLE.pots == list('#..###.#..#.#.#######.#.#.#..#.#...#')
SAMPLE.grow() #20
assert SAMPLE.pots == list('#....##....#####...#######....#.#..##')
assert 325 == SAMPLE.score()

GARDEN = Garden('input.txt')
for _ in range(20):
    GARDEN.grow()
print(GARDEN.score())

for _ in range(50000000000-20):
    GARDEN.grow()
print(GARDEN.score())
