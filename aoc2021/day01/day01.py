def pretty_print_answer(part, answer):
    print('Answer to part {num}: {ans}'.format(num=part, ans=answer))

def read_lines(file_name, is_strip=True):
    file = open(file_name)
    lines = [s for s in file.readlines()]
    file.close()
    if is_strip:
        lines = [s.strip() for s in lines]
    return lines

def increases(depths):
    increase = 0
    prev_depth = depths[0]
    for depth in depths[1:]:
        if depth > prev_depth:
            increase += 1
        prev_depth = depth
    return increase

def increase_window(depths):
    index = 0
    increase = 0
    prev_window = depths[0] + depths[1] + depths[2]
    for depth in range(1, len(depths)-2):
        window = prev_window - depths[depth - 1] + depths[depth + 2]
        if window > prev_window:
            increase += 1
    return increase

def main():
    depths = [int(line) for line in read_lines('input.txt')]
    pretty_print_answer(1, increases(depths))
    pretty_print_answer(2, increase_window(depths))

if __name__ == "__main__":
    main()
