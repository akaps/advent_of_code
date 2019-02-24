import utils
import hashlib
import itertools

def password(door_id):
    res = ''
    for i in itertools.count():
        hash_string = door_id + str(i)
        hashed = hashlib.md5(hash_string.encode()).hexdigest()
        if hashed[0:5] == '00000':
            print(door_id, i, hashed)
            res += hashed[5]
        if len(res) == 8:
            break
    print(res)
    return res

def password2(door_id):
    res = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in itertools.count():
        hash_string = door_id + str(i)
        hashed = hashlib.md5(hash_string.encode()).hexdigest()
        if (
                hashed[0:5] == '00000' and
                hashed[5].isdigit() and
                int(hashed[5]) < 8 and
                res[int(hashed[5])] == 0
            ):
            print(door_id, i, hashed)
            res[int(hashed[5])] = hashed[6]
        if 0 not in res:
            break
    print(''.join(res))
    return ''.join(res)

assert password('abc') == '18f47a30'
utils.pretty_print_answer(1, password('uqwqemis'))

assert password2('abc') == '05ace8e3'
utils.pretty_print_answer(2, password2('uqwqemis'))
