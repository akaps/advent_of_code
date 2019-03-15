import hashlib
import utils

class Password:
    def __init__(self, door_id):
        self.door_id = door_id
        self.valid_hashes = []
        self.i = 0

    def find_first_password(self):
        res = ''
        for _ in range(8):
            next_hash = self.determine_next_hash()
            self.valid_hashes.append(next_hash)
            res += next_hash[0]
        return res

    def find_second_password(self):
        res = [0, 0, 0, 0, 0, 0, 0, 0]
        for hash_val in self.valid_hashes:
            index = hash_val[0]
            if valid_index(index) and not res[int(index)]:
                res[int(index)] = hash_val[1]
        while 0 in res:
            next_hash = self.determine_next_hash()
            index = next_hash[0]
            if valid_index(index) and not res[int(index)]:
                res[int(index)] = next_hash[1]
        return ''.join(res)

    def determine_next_hash(self):
        hashed = 'xxxxx'
        while hashed[0:5] != '00000':
            hash_string = self.door_id + str(self.i)
            hashed = hashlib.md5(hash_string.encode()).hexdigest()
            self.i += 1
        self.valid_hashes.append(hashed[5:])
        return hashed[5:]

def valid_index(index):
    return index.isdigit() and int(index) < 8

SAMPLE = Password('abc')
assert SAMPLE.find_first_password() == '18f47a30'

PROBLEM = Password('uqwqemis')
utils.pretty_print_answer(1, PROBLEM.find_first_password())

assert SAMPLE.find_second_password() == '05ace8e3'
utils.pretty_print_answer(2, PROBLEM.find_second_password())
