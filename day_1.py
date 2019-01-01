#starting at 0, report the correct frequency
#each line is a modifier of the current frequency
class Frequency:
    def __init__(self, freqs):
        self.first_repeat = None
        self.processed = {0}
        self.total = 0
        while self.first_repeat is None:
            self.frequency(freqs)

    def frequency(self, freqs):
        for freq in freqs:
            self.total += int(freq)
            self.update_first_repeat(self.total)

    def update_first_repeat(self, new_val):
        if self.first_repeat is None:
            if new_val in self.processed:
                self.first_repeat = new_val
            else:
                self.processed.add(new_val)

file = open('day_1_input.txt', 'r')
freqs = file.readlines()
file.close()

res = Frequency(freqs)
print('sequence results in {freq}'.format(freq = res.total))
print('first repeat is at {repeat}'.format(repeat = res.first_repeat))
