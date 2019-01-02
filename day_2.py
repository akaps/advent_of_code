import collections

class Checksum:
    def __init__(self, ids):
        self.checksum = self.generate_checksum(ids)
        self.matched = self.find_match(ids)

    def find_match(self, ids):
        processed = []
        for id in ids:
            id = id.strip()
            for to_process in processed:
                matches = self.matches(id, to_process)
                if len(matches) == len(id) - 1:
                    return matches
            processed.append(id)

    def matches(self, id, to_process):
        matches = ''
        for i in range(0, len(id)):
            if id[i] == to_process[i]:
                matches += id[i]
        return matches

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
id_list = file.readlines()
file.close()

res = Checksum(id_list)
print('checksum is: {sum}'.format(sum=res.checksum))
print('matched letters are: {matched}'.format(matched=res.matched))
