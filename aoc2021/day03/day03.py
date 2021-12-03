from copy import deepcopy

def pretty_print_answer(part, answer):
    print(f'Answer to part {0}: {1}', part, answer)

def read_lines(file_name, is_strip=True):
    file = open(file_name)
    lines = list(file.readlines())
    file.close()
    if is_strip:
        lines = [s.strip() for s in lines]
    return lines

def common_bits(lines):
    counts = [0] * len(lines[0])
    half = len(lines)/2
    for line in lines:
        for index, entry in enumerate(line):
            if entry == '1':
                counts[index] += 1
    for index, entry in enumerate(counts):
        counts[index] = "1" if counts[index] >= half else "0"
    return counts

def power_consumption(lines):
    gamma = epsilon = ""
    bits = common_bits(lines)
    for bit in bits:
        gamma += bit
        epsilon += "0" if bit == "1" else "1"
    gamma = gamma.encode('utf-8')
    epsilon = epsilon.encode('utf-8')
    print(int(gamma))
    print(int(epsilon))
    return int(gamma, 2) * int(epsilon, 2)

def life_support(lines):
    common = deepcopy(lines)
    uncommon = deepcopy(lines)
    index = 0
    working = deepcopy(common)
    while len(common) > 1:
        print(len(common))
        bits = common_bits(common)
        for entry in common:
            if entry[index] != bits[index]:
                working.remove(entry)
        index += 1
        common = working
    print("oxygen", common, int(common[0], 2))

    index = 0
    working = deepcopy(uncommon)
    while len(uncommon) > 1:
        bits = common_bits(uncommon)
        for entry in uncommon:
            if entry[index] == bits[index]:
                working.remove(entry)
        index += 1
        uncommon = working
    print("carbon", uncommon, int(uncommon[0], 2))
    return int(common[0], 2) * int(uncommon[0], 2)

def main():
    lines = read_lines('test.txt')
    pretty_print_answer(1, power_consumption(lines))
    pretty_print_answer(2, life_support(lines))

if __name__ == "__main__":
    main()
