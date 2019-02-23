class Mancala:
    def __init__(self, input_array):
        self.banks = input_array
        self.configs = []

    def reallocate(self):
        while self.banks not in self.configs:
            self.configs.append(self.banks.copy())
            redistribute = self.banks.index(max(self.banks))
            total = self.banks[redistribute]
            self.banks[redistribute] = 0
            for index in range(redistribute + 1, redistribute + total + 1): #can pigeonhole
                self.banks[index % len(self.banks)] += 1

SAMPLE = Mancala([0, 2, 7, 0])
SAMPLE.reallocate()
assert len(SAMPLE.configs) == 5
assert SAMPLE.configs[0] == [0, 2, 7, 0]
assert SAMPLE.configs[1] == [2, 4, 1, 2]
assert SAMPLE.configs[2] == [3, 1, 2, 3]
assert SAMPLE.configs[3] == [0, 2, 3, 4]
assert SAMPLE.configs[4] == [1, 3, 4, 1]

PROBLEM = Mancala([0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11])
PROBLEM.reallocate()
print('Answer to part 1: {ans}'.format(ans=len(PROBLEM.configs)))
