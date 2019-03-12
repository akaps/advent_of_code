import utils
from automata import Automata

ON = '#'
OFF = '.'
STATES = [ON, OFF]

RULES = {
    ON: lambda counts: ON if (counts[ON] == 2 or counts[ON] == 3) else OFF,
    OFF: lambda counts: ON if counts[ON] == 3 else OFF
}

SAMPLE = Automata('sample.txt', STATES, RULES)
assert SAMPLE.count(ON) == 15
SAMPLE.next_generation()
assert SAMPLE.count(ON) == 11
SAMPLE.next_generation()
assert SAMPLE.count(ON) == 8
SAMPLE.next_generation()
assert SAMPLE.count(ON) == 4
SAMPLE.next_generation()
assert SAMPLE.count(ON) == 4

PROBLEM = Automata('input.txt', STATES, RULES)
for _ in range(100):
    PROBLEM.next_generation()
utils.pretty_print_answer(1, PROBLEM.count(ON))
