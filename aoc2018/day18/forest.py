from copy import deepcopy
import utils
from automata import Automata

OPEN = '.'
TREE = '|'
YARD = '#'
STATES = [OPEN, TREE, YARD]

RULES = {
    OPEN: lambda counts: TREE if counts[TREE] >= 3 else OPEN,
    TREE: lambda counts: YARD if counts[YARD] >= 3 else TREE,
    YARD: lambda counts: YARD if counts[TREE] >= 1 and counts[YARD] >= 1 else OPEN

}

def score(total_count):
    return total_count[TREE] * total_count[YARD]

def score_pt_2(acres):
    trees = 0
    yards = 0
    for row in acres:
        for val in row:
            if val == TREE:
                trees += 1
            if val == YARD:
                yards += 1
    return trees * yards

SAMPLE = Automata('sample.txt', STATES, RULES)
total_count = SAMPLE.count()
assert total_count[TREE] == 27
assert total_count[YARD] == 17
assert total_count[OPEN] == 56
SAMPLE.next_generation()
total_count = SAMPLE.count()
assert total_count[TREE] == 40
assert total_count[YARD] == 12
assert total_count[OPEN] == 48

for _ in range(9):
    SAMPLE.next_generation()
total_count = SAMPLE.count()
assert total_count[TREE] == 37
assert total_count[YARD] == 31
assert total_count[OPEN] == 32
assert score(total_count) == 1147

PROBLEM = Automata('input.txt', STATES, RULES)
TIME = 0
while TIME < 10:
    PROBLEM.next_generation()
    TIME += 1
total_count = PROBLEM.count()
utils.pretty_print_answer(1, score(total_count))

while PROBLEM.cells not in PROBLEM.generations:
    PROBLEM.next_generation()
    TIME += 1

START_REPEAT_INDEX = PROBLEM.generations.index(PROBLEM.cells)
REPEAT_LENGTH = len(PROBLEM.generations) - START_REPEAT_INDEX
INDEX = START_REPEAT_INDEX + ((1000000000 - START_REPEAT_INDEX) % REPEAT_LENGTH)
print('Repeats starting at time {t}'.format(t=TIME))
print('Repeating pattern is from {t_start} to {t_end}'.format(t_start=PROBLEM.generations.index(PROBLEM.cells), t_end=TIME))
print('Solution index is at {index}'.format(index=INDEX))
utils.pretty_print_answer(2, score_pt_2(PROBLEM.generations[INDEX]))
