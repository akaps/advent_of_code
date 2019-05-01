import utils

DIVISOR = 2147483647
LOW_16 = 0xffff
A_FACTOR = 16807
B_FACTOR = 48271
A_MULTIPLE = 4
B_MULTIPLE = 8

class Generator:
    def __init__(self, starting, factor, multiple=1):
        self.value = starting
        self.factor = factor
        self.multiple = multiple

    def next_value(self):
        self.value = self.value * self.factor % DIVISOR
        while self.value % self.multiple != 0:
            #print('skipping {val} as it is not a multiple of {mult}'.format(
            #    val=self.value,
            #    mult=self.multiple))
            self.value = self.value * self.factor % DIVISOR

    def __eq__(self, other):
        return (self.value & LOW_16) == (other.value & LOW_16)

def part_1():
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

    count = 0
    A = Generator(873, A_FACTOR)
    B = Generator(583, B_FACTOR)

    for T in range(40000000):
        if T % 1000000 == 0:
            print(T)
        A.next_value()
        B.next_value()
        if A == B:
            count += 1

def part_2():
    A = Generator(65, A_FACTOR, A_MULTIPLE)
    B = Generator(8921, B_FACTOR, B_MULTIPLE)
    A.next_value()
    B.next_value()
    assert A.value == 1352636452
    assert B.value == 1233683848
    assert A != B

    A.next_value()
    B.next_value()
    assert A.value == 1992081072
    assert B.value == 862516352
    assert A != B

    A.next_value()
    B.next_value()
    assert A.value == 530830436
    assert B.value == 1159784568
    assert A != B

    A.next_value()
    B.next_value()
    assert A.value == 1980017072
    assert B.value == 1616057672
    assert A != B

    A.next_value()
    B.next_value()
    assert A.value == 740335192
    assert B.value == 412269392
    assert A != B

    for _ in range(1051):
        A.next_value()
        B.next_value()
    assert A.value == 1023762912
    assert B.value == 896885216
    assert A == B

    print('Evaluating Part 2')
    count = 0
    A = Generator(873, A_FACTOR, A_MULTIPLE)
    B = Generator(583, B_FACTOR, B_MULTIPLE)

    for _ in range(5000000):
        A.next_value()
        B.next_value()
        if A == B:
            count += 1
    return count

utils.pretty_print_answer(1, part_1())
utils.pretty_print_answer(2, part_2())
