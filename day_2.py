import collections

class Checksum:
    def __init__(self, ids):
        self.checksum = self.generate_checksum(ids)

    def generate_checksum(self, ids):
        twos = 0
        threes = 0
        for id in ids:
            letters = collections.Counter(id.strip())
            has_twos = False
            has_threes = False
            for count in letters.values():
                if count == 2:
                    has_twos = True
                if count == 3:
                    has_threes = True
            twos += 1 if has_twos else 0
            threes += 1 if has_threes else 0
        return twos * threes

file = open('day_2_input.txt', 'r')
ids = file.readlines()
file.close()

res = Checksum(ids)
print 'checksum is {sum}'.format(sum = res.checksum)
