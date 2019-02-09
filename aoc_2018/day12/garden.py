from collections import deque
import re

DEAD = '.'
ALIVE = '#'

class Rule:
    def __init__(self, input):
        self.pattern, self.result = re.split(' => ', input)

    def __repr__(self):
        return 'if {pattern}, then {res}'.format(pattern=self.pattern, res=self.result)

class Garden:
    def __init__(self, input):
        initial_state = input[0].strip()
        self.pots = re.split('initial state: ', initial_state)[1]
        self.zero_index = 0
        self.rules = []
        for rule in input[2:]:
            self.rules.append(Rule(rule.strip()))

    def grow(self):
        next_generation = ''
        for i in range(len(self.pots)):
            pot = self.neighboring_pots(i)
            rule_to_apply = None
            for rule in self.rules:
                if not rule_to_apply and rule.pattern == pot:
                    rule_to_apply = rule
            next_generation += rule_to_apply.result if rule_to_apply else '.'
        self.pots = next_generation

    def neighboring_pots(self, index):
        res = ''
        for i in range(-2, 3):
            if self.oob(index + i):
                res += '.'
            else:
                res += self.pots[index + i]
        return res

    def score(self):
        res = 0
        for i in range(0, len(self.pots)):
            if self.pots[i] == ALIVE:
                res += i - self.zero_index
        return res

    def oob(self, index):
        return index < 0 or index >= len(self.pots)

    def __repr__(self):
        return str(self.pots)

file = open('sample.txt')
garden = Garden(file.readlines())
file.close()
assert garden.pots in '...#..#.#..##......###...###...........'
garden.grow() #1
assert garden.pots in '...#...#....#.....#..#..#..#...........'
garden.grow() #2
assert garden.pots in '...##..##...##....#..#..#..##..........'
garden.grow() #3
assert garden.pots in '..#.#...#..#.#....#..#..#...#..........'
garden.grow() #4
assert garden.pots in '...#.#..#...#.#...#..#..##..##.........'
garden.grow() #5
assert garden.pots in '....#...##...#.#..#..#...#...#.........'
garden.grow() #6
assert garden.pots in '....##.#.#....#...#..##..##..##........'
garden.grow() #7
assert garden.pots in '...#..###.#...##..#...#...#...#........'
garden.grow() #8
assert garden.pots in '...#....##.#.#.#..##..##..##..##.......'
garden.grow() #9
assert garden.pots in '...##..#..#####....#...#...#...#.......'
garden.grow() #10
assert garden.pots in '..#.#..#...#.##....##..##..##..##......'
garden.grow() #11
assert garden.pots in '...#...##...#.#...#.#...#...#...#......'
garden.grow() #12
assert garden.pots in '...##.#.#....#.#...#.#..##..##..##.....'
garden.grow() #13
assert garden.pots in '..#..###.#....#.#...#....#...#...#.....'
garden.grow() #14
assert garden.pots in '..#....##.#....#.#..##...##..##..##....'
garden.grow() #15
assert garden.pots in '..##..#..#.#....#....#..#.#...#...#....'
garden.grow() #16
assert garden.pots in '.#.#..#...#.#...##...#...#.#..##..##...'
garden.grow() #17
assert garden.pots in '..#...##...#.#.#.#...##...#....#...#...'
garden.grow() #18
assert garden.pots in '..##.#.#....#####.#.#.#...##...##..##..'
garden.grow() #19
assert garden.pots in '.#..###.#..#.#.#######.#.#.#..#.#...#..'
garden.grow() #20
assert garden.pots in '.#....##....#####...#######....#.#..##.'
assert 325 == garden.score()

file = open('input.txt')
garden = Garden(file.readlines())
file.close()
for _ in range(20):
    garden.grow()
print(garden.score())
