import utils

TRANSFORMS = {(0, 7): 1}

def transform(loop_size, subject_number):
    result = 1
    for i in range(loop_size):
        result *= subject_number
        result %= 20201227
    return result

def find_loop_size(public_key):
    loop_size = 0
    value = transform(loop_size, 7)
    while value != public_key:
        loop_size += 1
        if loop_size % 1000 == 0:
            print(loop_size)
        value = transform(loop_size, 7)
    return loop_size

def find_encryption_key(card_public_key, door_public_key):
    card_loop = find_loop_size(card_public_key)
    door_loop = find_loop_size(door_public_key)
    print('loop sizes found', card_loop, door_loop)
    encryption = transform(door_loop, card_public_key)
    check = transform(card_loop, door_public_key)
    print(encryption, check)
    assert encryption == check
    return encryption

def main():
    utils.pretty_print_answer(1, find_encryption_key(6930903, 19716708))

if __name__ == "__main__":
    main()
