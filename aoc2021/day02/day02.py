FORWARD = 'forward'
DOWN = 'down'
UP = 'up'

def pretty_print_answer(part, answer):
    print('Answer to part {num}: {ans}'.format(num=part, ans=answer))

def read_lines(file_name, is_strip=True):
    file = open(file_name)
    lines = [s for s in file.readlines()]
    file.close()
    if is_strip:
        lines = [s.strip() for s in lines]
    return lines

def travel(lines):
    posx = posy = 0
    for line in lines:
        direction, magnitude = line.split()
        magnitude = int(magnitude)
        if direction == FORWARD:
            posx += magnitude
        elif direction == DOWN:
            posy += magnitude
        elif direction == UP:
            posy -= magnitude
        else:
            assert(False, f'unsupported action {0}', direction)
    return posx * posy

def aim_travel(lines):
    posx = posy = aim = 0
    for line in lines:
        direction, magnitude = line.split()
        magnitude = int(magnitude)
        if direction == FORWARD:
            posx += magnitude
            posy += aim * magnitude
        elif direction == DOWN:
            aim += magnitude
        elif direction == UP:
            aim -= magnitude
        else:
            assert(False, f'unsupported action {0}', direction)
    return posx * posy

def main():
    lines = read_lines('input.txt')
    pretty_print_answer(1, travel(lines))
    pretty_print_answer(2, aim_travel(lines))

if __name__ == "__main__":
    main()
