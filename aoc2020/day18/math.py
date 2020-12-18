import utils

OPEN_PAREN = '('
CLOSE_PAREN = ')'
SPACE = ' '
MULT = '*'
ADD = '+'

def calculate(expression, precendence_agnostic):
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
        value = calculate(inner[1:-1], precendence_agnostic)
        expression = expression.replace(inner, str(value))
    expression = expression.split(SPACE)
    if precendence_agnostic:
        return calculate_simple_expression(expression)
    return calculate_precedence_expression(expression)

def calculate_simple_expression(expression):
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

def calculate_precedence_expression(expression):
    while ADD in expression:
        add_index = expression.index(ADD)
        rht = int(expression.pop(add_index + 1))
        lht = int(expression.pop(add_index - 1))
        expression[add_index - 1] = lht + rht
    return calculate_simple_expression(expression)

def sum_expressions(lines, precendence_agnostic=True):
    total = 0
    for line in lines:
        total += calculate(line, precendence_agnostic)
    return total

def main():
    lines = utils.read_lines('input.txt')
    utils.pretty_print_answer(1, sum_expressions(lines))
    utils.pretty_print_answer(2, sum_expressions(lines, precendence_agnostic=False))

if __name__ == "__main__":
    main()
