from functools import reduce
import utils

COMMA = ','

def get_ids(line):
    ids = []
    values = line.split(COMMA)
    for value in values:
        if value.isdigit():
            ids.append(int(value))
    return ids

def find_earliest(arrival_time, ids):
    shortest_wait = arrival_time
    shortest_id = -1
    for bus_id in ids:
        soonest_time = ((arrival_time // bus_id) * bus_id) + bus_id
        wait_time = soonest_time - arrival_time
        if wait_time < shortest_wait:
            shortest_wait = wait_time
            shortest_id = bus_id
    return shortest_id * shortest_wait

def ids_with_offsets(line):
    ids = line.split(COMMA)
    offset_ids = {}
    for offset, bus_id in enumerate(ids):
        if bus_id.isdigit():
            offset_ids[int(bus_id)] = -offset
    return offset_ids

def chinese_remainder(line):
    offset_ids = ids_with_offsets(line)
    total = 0
    product = reduce(lambda a, b: a * b, offset_ids)
    for bus_id, offset in offset_ids.items():
        quotient = product // bus_id
        total += offset * mul_inv(quotient, bus_id) * quotient
    return total % product

#effectively lcm, but with more work
def mul_inv(quotient, bus_id):
    b_0 = bus_id
    x_0, x_1 = 0, 1
    if bus_id == 1:
        return 1
    while quotient > 1:
        factor = quotient // bus_id
        quotient, bus_id = bus_id, quotient % bus_id
        x_0, x_1 = x_1 - factor * x_0, x_0
    if x_1 < 0:
        x_1 += b_0
    return x_1

def main():
    lines = utils.read_lines('input.txt')
    arrival_time = int(lines[0])
    ids = get_ids(lines[1])
    utils.pretty_print_answer(1, find_earliest(arrival_time, ids))
    utils.pretty_print_answer(2, chinese_remainder(lines[1]))

if __name__ == "__main__":
    main()
