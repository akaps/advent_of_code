from collections import defaultdict
import utils

def part_1(joltages):
    diffs = defaultdict(lambda: 0)
    for current_index, current_joltage in enumerate(joltages):
        if current_index + 1 < len(joltages):
            diff = difference(current_joltage, joltages[current_index + 1])
            diffs[diff] += 1
    return diffs

def difference(num1, num2):
    return num2 - num1

def all_connections(joltages):
    connections = {}
    for current_index, current_joltage in enumerate(joltages):
        connections[current_joltage] = []
        for next_index in range(current_index + 1, len(joltages)):
            diff = difference(current_joltage, joltages[next_index])
            if diff <= 3:
                connections[current_joltage].append(joltages[next_index])
            else:
                break
    return connections

def count_connections(adapter_map, root):
    stack = [root]
    answer = 0
    while stack:
        current_joltage = stack.pop(0)
        answer += 1
        adapters = adapter_map[current_joltage]
        if len(adapters) == 1:
            next_adapter = adapters[0]
            while len(adapter_map[next_adapter]) == 1:
                next_adapter = adapter_map[next_adapter][0]
            if adapter_map[next_adapter]:
                stack.extend(adapter_map[next_adapter])
        else:
            stack.extend(adapters)
    return answer

def read_joltages(file_name):
    lines = [int(x) for x in utils.read_lines(file_name)]
    lines.sort()
    lines.insert(0, 0)
    lines.append(lines[-1] + 3)
    return lines

def main():
    joltages = read_joltages('aoc2020/day10/sample1.txt')
    diffs = part_1(joltages)
    utils.pretty_print_answer(1, diffs[1] * diffs[3])
    connections = all_connections(joltages)
    utils.pretty_print_answer(2, count_connections(connections, 0))

if __name__ == "__main__":
    main()
