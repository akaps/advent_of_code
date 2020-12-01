import utils

def product_of_20(file_name):
    lines = utils.read_lines(file_name)
    lines = [int(line) for line in lines]
    for index, val in enumerate(lines):
        for j in range(index + 1, len(lines)):
            if val + lines[j] == 2020:
                return val * lines[j]

def product_of_20_for_3(file_name):
    lines = utils.read_lines(file_name)
    lines = [int(line) for line in lines]
    for index, val in enumerate(lines):
        for j in range(index + 1, len(lines)):
            for k in range(j + 1, len(lines)):
                if val + lines[j] + lines[k] == 2020:
                    return val * lines[j] * lines[k]

def main():
    utils.pretty_print_answer(1, product_of_20('input.txt'))
    utils.pretty_print_answer(2, product_of_20_for_3('input.txt'))

if __name__ == '__main__':
    main()
