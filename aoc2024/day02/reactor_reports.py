def report_dampened_safe(report_deltas, index):
    updated_deltas = report_deltas[index + 1:]
    updated_deltas[0] += report_deltas[index]
    return report_safe(updated_deltas, False)

def report_safe(report_deltas, has_dampener):
    count_inc = 0
    count_dec = 0
    for index, delta in enumerate(report_deltas):
        if 1 <= abs(delta) <= 3:
            if delta < 0 and count_inc == 0:
                count_dec += 1
            elif delta > 0 and count_dec == 0:
                count_inc += 1
            elif not has_dampener or not report_dampened_safe(report_deltas, index):
                return False
            else:
                return False
        elif has_dampener:
            return report_dampened_safe(report_deltas, index)
        else:
            return False
    return count_inc == 0 or count_dec == 0

class Reports:
    def __init__(self, file_name):
        file = open(file_name, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()
        self.reports = []
        for line in lines:
            self.reports.append([int(x) for x in line.split(' ')])

    def count_strict(self, has_dampener=False):
        total = 0
        for report in self.reports:
            report_delta = []
            for index in range(len(report) - 1):
                report_delta.append(report[index] - report[index + 1])
            if report_safe(report_delta, has_dampener):
                total += 1
        print(total)
        return total

def main():
    sample = Reports('aoc2024/day02/sample.txt')
    problem = Reports('aoc2024/day02/input.txt')
    assert sample.count_strict() == 2
    print('Part 1:', problem.count_strict())

    assert sample.count_strict(has_dampener=True) == 4
    print('Part 2:', problem.count_strict(has_dampener=True))

if __name__ == "__main__":
    main()
