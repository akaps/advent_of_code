def manhattan_distance(loc1, loc2):
    dist = 0
    for dim in enumerate(loc1):
        dist += abs(dim[1]-loc2[dim[0]])
    return dist

def pretty_print_answer(part, answer):
    print('Answer to part {num}: {ans}'.format(num=part, ans=answer))

def read_lines(file_name, is_strip=True):
    file = open(file_name)
    lines = [s for s in file.readlines()]
    file.close()
    if is_strip:
        lines = [s.strip for s in lines]
    return lines

def translate_to_chars(ascii_vals):
    result = [chr(i) for i in ascii_vals]
    return ''.join(result)

def translate_to_ascii(chars):
    return [ord(c) for c in chars]
