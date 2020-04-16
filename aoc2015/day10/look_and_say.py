import re
import utils

DIGIT_GROUPING = r'\d'

def run_length_encode(input_str):
    head = 0
    adv = 0
    last_val = -1
    res = []
    while head < len(input_str):
        if input_str[head] != last_val:
            count = 0
            adv = head
            last_val = input_str[head]
            while adv < len(input_str) and input_str[adv] == last_val:
                count += 1
                adv += 1
            res.append('{count}{val}'.format(count=count, val=last_val))
        head = adv
    return ''.join(res)

def main():
    seed = '1113122113'
    for _ in range(40):
        seed = run_length_encode(seed)
    utils.pretty_print_answer(1, len(seed))

    for _ in range(10):
        seed = run_length_encode(seed)
    utils.pretty_print_answer(2, len(seed))

if __name__ == '__main__':
    main()
