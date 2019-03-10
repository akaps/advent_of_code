import collections
import utils

DASH = '-'
BRACKET = '['
SPACE = ' '
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class Room:
    def __init__(self, room_name):
        split = room_name.rindex(DASH)
        checksum_start = room_name.index(BRACKET)
        self.encrypted_name = room_name[ : split]
        self.room_id = int(room_name[split + 1 : checksum_start])
        self.checksum = room_name[checksum_start + 1 : -1]

    def is_real_room(self):
        letter_counts = collections.Counter(self.encrypted_name)
        del letter_counts[DASH]
        letters = sorted(letter_counts.keys())
        letters = sorted(letters, key=lambda c: -letter_counts[c])
        expected = ''.join(letters[:5])
        return expected == self.checksum

    def decrypt_name(self):
        decrypted = []
        for val in self.encrypted_name:
            if val == DASH:
                decrypted.append(SPACE)
            else:
                index = (ALPHABET.index(val) + self.room_id) % 26
                decrypted.append(ALPHABET[index])
        return ''.join(decrypted)

SAMPLES = [
    Room('aaaaa-bbb-z-y-x-123[abxyz]'),
    Room('a-b-c-d-e-f-g-h-987[abcde]'),
    Room('not-a-real-room-404[oarel]'),
    Room('totally-real-room-200[decoy]')
]
assert SAMPLES[0].is_real_room()
assert SAMPLES[1].is_real_room()
assert SAMPLES[2].is_real_room()
assert not SAMPLES[3].is_real_room()

TOTAL = 0
LINES = utils.read_lines('input.txt')
ROOM = None
for line in LINES:
    room = Room(line)
    if room.is_real_room():
        TOTAL += room.room_id
        if room.decrypt_name() == 'northpole object storage':
            ROOM = room
utils.pretty_print_answer(1, TOTAL)

assert Room('qzmt-zixmtkozy-ivhz-343[zmith]').decrypt_name() == 'very encrypted name'

utils.pretty_print_answer(2, ROOM.room_id)
