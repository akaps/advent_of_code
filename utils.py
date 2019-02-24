def manhattan_distance(loc1, loc2):
    dist = 0
    for dim in enumerate(loc1):
        dist += abs(dim[1]-loc2[dim[0]])
    return dist

def pretty_print_answer(part, answer):
    print('Answer to part {num}: {ans}'.format(num=part, ans=answer))

def read_lines(file_name):
    file = open(file_name)
    lines = [s.strip() for s in file.readlines()]
    file.close()
    return lines