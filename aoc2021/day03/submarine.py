def read_lines(file_name):
    with open(file_name, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def sum_bits(diagnostics):
    result = [0] * len(diagnostics[0])
    for diagnostic in diagnostics:
        for bit_index, bit in enumerate(diagnostic):
            result[bit_index] += int(bit)
    return result

def find_gamma_rate(diagnostics) -> str:
    result = []
    totals = sum_bits(diagnostics)
    for total in totals:
        result.append('1' if total >= len(diagnostics) / 2 else '0')
    return ''.join(result)

def find_epsilon_rate(diagnostics) -> str:
    result = []
    totals = sum_bits(diagnostics)
    for total in totals:
        result.append('0' if total >= len(diagnostics) / 2 else '1')
    return ''.join(result)

def filter_candidates(candidates, current_index, target):
    assert current_index < len(target)
    new_candidates = []
    for candidate in candidates:
        if candidate[current_index] == target[current_index]:
            new_candidates.append(candidate)
    return new_candidates

class Submarine:
    def __init__(self, file_name:str):
        self.lines = read_lines(file_name)
        self.gamma_rate = find_gamma_rate(self.lines)
        self.epsilon_rate = find_epsilon_rate(self.lines)

    def power_consumption(self) -> int:
        return int(self.gamma_rate, 2) * int(self.epsilon_rate, 2)

    def life_support_rating(self) -> int:
        return int(self.oxygen_gen_rating(), 2) * int(self.co2_scrubber_rating(), 2)

    def oxygen_gen_rating(self) -> str:
        candidates = self.lines
        current_index = 0
        while len(candidates) > 1:
            print(candidates)
            candidates = filter_candidates(candidates, current_index, find_gamma_rate(candidates))
            current_index += 1
        print(candidates)
        return candidates[0]

    def co2_scrubber_rating(self) -> str:
        candidates = self.lines
        current_index = 0
        while len(candidates) > 1:
            print(candidates)
            candidates = filter_candidates(candidates, current_index, find_epsilon_rate(candidates))
            current_index += 1
        print(candidates)
        return candidates[0]

def main():
    test_sub = Submarine('aoc2021/day03/test.txt')
    assert 198 == test_sub.power_consumption()

    real_sub = Submarine('aoc2021/day03/input.txt')
    print('Answer to Part 1:', real_sub.power_consumption())

    assert 230 == test_sub.life_support_rating()
    print('Answer to Part 2:', real_sub.life_support_rating())

if __name__ == "__main__":
    main()
