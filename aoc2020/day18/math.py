import re
import utils

PRECEDENCE_REGEX = r'\(?([\d+ *]*)\)?'
EXPRESSION_REGEX = r'(?P<operand>\d+) (?P<operator>[+*]) (?P<rhs>.*)'
#(?P<operand>\d+)( (?P<operator>[+*]) (?P<next_operand>\d+))+
OPEN_PAREN = '('
CLOSE_PAREN = ')'
SPACE = ' '
MULT = '*'
ADD = '+'

def calculate(expression):
    while OPEN_PAREN in expression:
        count_parens = 1
        start_index = expression.index(OPEN_PAREN)
        end_index = -1
        for index in range(start_index + 1, len(expression)):
            if expression[index] == OPEN_PAREN:
                count_parens += 1
            elif expression[index] == CLOSE_PAREN:
                count_parens -= 1
                if count_parens == 0:
                    end_index = index
                    break
        assert end_index != -1, 'badly formed expression {expr}'.format(expr=expression)
        inner = expression[start_index:end_index+1]
        value = calculate(inner[1:-1])
        expression = expression.replace(inner, str(value))
    return calculate_simple_expression(expression)

def calculate_simple_expression(expression):
    expression = expression.split(SPACE)
    total = int(expression.pop(0))
    while expression:
        operator = expression.pop(0)
        operand = int(expression.pop(0))
        if operator == MULT:
            total *= operand
        elif operator == ADD:
            total += operand
        else:
            assert False, 'Unsupported operand {op}'.format(op=operand)
    return total

def part_1(lines):
    total = 0
    for line in lines:
        total += calculate(line)
    return total

def main():
    lines = utils.read_lines('input.txt')
    utils.pretty_print_answer(1, part_1(lines))

if __name__ == "__main__":
    main()
