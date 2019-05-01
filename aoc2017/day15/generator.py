import utils

DIVISOR = 2147483647
LOW_16 = 0xffff
A_FACTOR = 16807
B_FACTOR = 48271

class Generator:
    def __init__(self, starting, factor):
        self.value = starting
        self.factor = factor

    def next_value(self):
        self.value = self.value * self.factor % DIVISOR

    def __eq__(self, other):
        return (self.value & LOW_16) == (other.value & LOW_16)

A = Generator(65, A_FACTOR)
B = Generator(8921, B_FACTOR)
A.next_value()
B.next_value()
assert A.value == 1092455
assert B.value == 430625591
assert A != B

A.next_value()
B.next_value()
assert A.value == 1181022009
assert B.value == 1233683848
assert A != B

A.next_value()
B.next_value()
assert A.value == 245556042
assert B.value == 1431495498
assert A == B

A.next_value()
B.next_value()
assert A.value == 1744312007
assert B.value == 137874439
assert A != B

A.next_value()
B.next_value()
assert A.value == 1352636452
assert B.value == 285222916
assert A != B

COUNT = 0
A = Generator(873, A_FACTOR)
B = Generator(583, B_FACTOR)

for T in range(40000000):
    A.next_value()
    B.next_value()
    if A == B:
        COUNT += 1
utils.pretty_print_answer(1, COUNT)
