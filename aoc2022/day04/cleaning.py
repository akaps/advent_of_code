def complete_overlaps(lines):
    overlaps = 0

    for line in lines:
        group_a, group_b = line.split(',')
        a_min, a_max = [int(s) for s in group_a.split('-')]
        b_min, b_max = [int(s) for s in group_b.split('-')]
        if (a_min <= b_min and a_max >= b_max) or (b_min <= a_min and b_max >= a_max):
            overlaps += 1
    return overlaps

def overlaps(lines):
    overlaps = 0
    for line in lines:
        group_a, group_b = line.split(',')
        a_min, a_max = [int(s) for s in group_a.split('-')]
        b_min, b_max = [int(s) for s in group_b.split('-')]
        if set(range(a_min, a_max + 1)).intersection(range(b_min, b_max + 1)):
            overlaps += 1
    return overlaps

def main():
    file_input = open('input.txt')
    lines = [line.strip() for line in file_input.readlines()]
    file_input.close()
    pairs = complete_overlaps(lines)
    print('Part 1: ', pairs)
    num_overlaps = overlaps(lines)
    print('Part 2: ', num_overlaps)

if __name__ == '__main__':
    main()
