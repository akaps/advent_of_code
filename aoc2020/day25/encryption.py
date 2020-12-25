import utils

TRANSFORMS = {(0, 7): 1}

def transform(loop_size, subject_number):
    result = 1
    for _ in range(loop_size):
        result = transform_generator(result, subject_number)
    return result

def transform_generator(result, subject_number):
    result *= subject_number
    result %= 20201227
    return result

def find_loop_size(public_key):
    loop_size = 0
    value = 1
    while value != public_key:
        loop_size += 1
        value = transform_generator(value, 7)
    return loop_size

def find_encryption_key(card_public_key, door_public_key):
    card_loop = find_loop_size(card_public_key)
    print('found card loop size {size}'.format(size=card_loop))
    door_loop = find_loop_size(door_public_key)
    print('found door loop size {size}'.format(size=door_loop))
    encryption = transform(door_loop, card_public_key)
    utils.pretty_print_answer(1, encryption)
    print('no part 2, confirming answer matches expectations')
    check = transform(card_loop, door_public_key)
    assert encryption == check
    print('confirmed. Happy holidays :)')

def main():
    find_encryption_key(6930903, 19716708)

if __name__ == "__main__":
    main()
