import utils

def product_of_20(lines):
    for index, val in enumerate(lines):
        for j in range(index + 1, len(lines)):
            if val + lines[j] == 2020:
                return val * lines[j]

def product_of_20_for_3(lines):
    for index, val in enumerate(lines):
        for j in range(index + 1, len(lines)):
            for k in range(j + 1, len(lines)):
                if val + lines[j] + lines[k] == 2020:
                    return val * lines[j] * lines[k]

def main():
    lines = utils.read_lines('input.txt')
    lines = [int(line) for line in lines]
    utils.pretty_print_answer(1, product_of_20(lines))
    utils.pretty_print_answer(2, product_of_20_for_3(lines))

if __name__ == '__main__':
    main()
