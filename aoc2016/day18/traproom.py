import utils

TRAP = '^'
SAFE = '.'

class RogueLikeMap:

    def __init__(self, seed, num_rows):
        self.map = []
        self.generate_rows(seed, num_rows)

    def generate_rows(self, seed, num_rows):
        while len(self.map) < num_rows:
            self.map.append(seed)
            seed = generate_next_seed(seed)

    def num_safe(self):
        answer = 0
        for row in self.map:
            answer += row.count(SAFE)
        return answer

def generate_next_seed(seed):
    next_seed = []
    for pos, char in enumerate(seed):
        next_seed.append(next_tile(pos, seed))
    return ''.join(next_seed)

def next_tile(position, above):
    left = above[position - 1] if position - 1 >= 0 else SAFE
    right = above[position + 1] if position + 1 < len(above) else SAFE
    if left != right:
        return TRAP
    return SAFE

assert next_tile(0, '..^^.') == SAFE
assert next_tile(1, '..^^.') == TRAP
assert next_tile(2, '..^^.') == TRAP
assert next_tile(3, '..^^.') == TRAP
assert next_tile(4, '..^^.') == TRAP

SAMPLE = RogueLikeMap('..^^.', 3)
assert SAMPLE.map[0] == '..^^.'
assert SAMPLE.map[1] == '.^^^^'
assert SAMPLE.map[2] == '^^..^'

SAMPLE = RogueLikeMap('.^^.^.^^^^', 10)
print('\n'.join(SAMPLE.map))
assert SAMPLE.map[0] == '.^^.^.^^^^'
assert SAMPLE.map[1] == '^^^...^..^'
assert SAMPLE.map[2] == '^.^^.^.^^.'
assert SAMPLE.map[3] == '..^^...^^^'
assert SAMPLE.map[4] == '.^^^^.^^.^'
assert SAMPLE.map[5] == '^^..^.^^..'
assert SAMPLE.map[6] == '^^^^..^^^.'
assert SAMPLE.map[7] == '^..^^^^.^^'
assert SAMPLE.map[8] == '.^^^..^.^^'
assert SAMPLE.map[9] == '^^.^^^..^^'
assert SAMPLE.num_safe() == 38

PROBLEM = RogueLikeMap('^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^', 40)
print(PROBLEM.num_safe())
utils.pretty_print_answer(1, PROBLEM.num_safe())

PROBLEM = RogueLikeMap('^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^', 400000)
utils.pretty_print_answer(2, PROBLEM.num_safe())
