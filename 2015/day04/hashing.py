import hashlib
import itertools

assert hashlib.md5('abcdef609043'.encode()).hexdigest()[0:5] == '00000'
assert hashlib.md5('pqrstuv1048970'.encode()).hexdigest()[0:5] == '00000'

input_string = 'ckczppom'
for i in itertools.count():
    hashed = hashlib.md5((input_string + str(i)).encode()).hexdigest()[0:5]
    if hashed == '00000':
        print(i)
        break

for i in itertools.count():
    hashed = hashlib.md5((input_string + str(i)).encode()).hexdigest()[0:6]
    if hashed == '000000':
        print(i)
        break  
