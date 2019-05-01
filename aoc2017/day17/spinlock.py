import utils

TOTAL_INSERTIONS = 2017
TOTAL_INSERTIONS_PT_2 = 50000000

class Spinlock:
    def __init__(self, steps):
        self.steps = steps
        self.sequence = [0]
        self.current_pos = 0

    def insert_next(self, val):
        next_index = (self.current_pos + self.steps) % len(self.sequence) + 1
        self.sequence.insert(next_index, val)
        self.current_pos = next_index

    def fill(self, last):
        for i in range(1, last + 1):
            self.insert_next(i)

    def val_after(self, val):
        index = self.sequence.index(val)
        return self.sequence[(index + 1) % len(self.sequence)]

    def __repr__(self):
        return ','.join([str(x) for x in self.sequence])

LOCK = Spinlock(3)
assert str(LOCK) == '0'
LOCK.insert_next(1)
assert str(LOCK) == '0,1'
LOCK.insert_next(2)
assert str(LOCK) == '0,2,1'
LOCK.insert_next(3)
assert str(LOCK) == '0,2,3,1'
LOCK.insert_next(4)
assert str(LOCK) == '0,2,4,3,1'
LOCK.insert_next(5)
assert str(LOCK) == '0,5,2,4,3,1'
LOCK.insert_next(6)
assert str(LOCK) == '0,5,2,4,3,6,1'
LOCK.insert_next(7)
assert str(LOCK) == '0,5,7,2,4,3,6,1'
LOCK.insert_next(8)
assert str(LOCK) == '0,5,7,2,4,3,8,6,1'
LOCK.insert_next(9)
assert str(LOCK) == '0,9,5,7,2,4,3,8,6,1'

LOCK = Spinlock(3)
LOCK.fill(TOTAL_INSERTIONS)
assert LOCK.val_after(TOTAL_INSERTIONS) == 638

LOCK = Spinlock(367)
LOCK.fill(TOTAL_INSERTIONS)
utils.pretty_print_answer(1, LOCK.val_after(TOTAL_INSERTIONS))

LOCK = Spinlock(367)
LOCK.fill(TOTAL_INSERTIONS_PT_2)
utils.pretty_print_answer(2, LOCK.val_after(0))
