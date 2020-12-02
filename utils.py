import re
import math

#File input helpers
def pretty_print_answer(part, answer):
    print('Answer to part {num}: {ans}'.format(num=part, ans=answer))

def read_lines(file_name, is_strip=True):
    file = open(file_name)
    lines = [s for s in file.readlines()]
    file.close()
    if is_strip:
        lines = [s.strip() for s in lines]
    return lines

def split_line(regex, line):
    assert re.match(regex, line), 'No match for "{regex}" in "{line}"'.format(regex=regex, line=line)
    return re.match(regex, line).groups()

#Vector analysis
def manhattan_distance(loc1, loc2):
    dist = 0
    for dim in enumerate(loc1):
        dist += abs(dim[1]-loc2[dim[0]])
    return dist

def linear_distance(vec1, vec2):
    assert len(vec1) == len(vec2), 'Unmatched tuple lengths'
    distance = 0
    for dim, val1 in enumerate(vec1):
        distance += (val1 - vec2[dim])^2
    return math.sqrt(distance)

#Character manipulation
def ascii_to_string(ascii_vals):
    return [chr(i) for i in ascii_vals]

def string_to_ascii(string):
    return [ord(c) for c in string]
