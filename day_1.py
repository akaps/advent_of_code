#starting at 0, report the correct frequency
#each line is a modifier of the current frequency
def total(freqs):
    curr_freq = 0
    for freq in freqs:
        curr_freq += int(freq)
    return curr_freq

def first_repeat(freqs):
    prev_freqs = set()
    curr_freq = 0
    for freq in freqs:
        curr_freq += int(freq)
        if curr_freq in prev_freqs:
            return curr_freq
        prev_freqs.add(curr_freq)
    print 'Could not find a duplicate'
    return -1

file = open('day_1_input.txt', 'r')
freqs = file.readlines()
print 'ending frequency'
print total(freqs)
print 'first repeat'
print first_repeat(freqs)
file.close()
