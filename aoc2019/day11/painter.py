import utils
from complexvector import ComplexVector
from aoc2019.int_code import IntCode, MissingInputError

BLACK = 0
WHITE = 1

LEFT = 0
RIGHT = 1

RIGHT_TURN = -1j
LEFT_TURN = 1j

class Painter:
    def __init__(self, input_file):
        self.computer = IntCode(input_file)
        self.vector = ComplexVector()
        self.colors = {self.vector.magnitude: BLACK}

    def get_next_instruction(self):
        result = None
        try:
            position = self.vector.magnitude
            input_val = BLACK
            if position in self.colors:
                input_val = self.colors[position]
            result = self.computer.run_program([input_val])
        except MissingInputError:
            result = self.computer.output
        self.computer.output = []
        return result

    def paint(self):
        result = self.get_next_instruction()
        while result:
            color, turn = result
            position = self.vector.magnitude
            self.colors[position] = color
            self.vector.rotate(RIGHT_TURN if turn == RIGHT else LEFT_TURN)
            self.vector.translate(1)
            result = self.get_next_instruction()

    def __repr__(self):
        x_min = int(min([key.real for key in self.colors]))
        x_max = int(max([key.real for key in self.colors]))
        y_max = -int(min([key.imag for key in self.colors]))
        y_min = -int(max([key.imag for key in self.colors]))
        result = []
        for y_pos in range(y_min, y_max + 1):
            row = []
            for x_pos in range(x_min, x_max + 1):
                point = x_pos + (y_pos * -1j)
                if point in self.colors:
                    color = self.colors[point]
                    if color == WHITE:
                        row.append('#')
                    else:
                        row.append(' ')
                else:
                    row.append(' ')
            result.append(''.join(row))
        return '\n'.join(result)

PROBLEM = Painter('input.txt')
PROBLEM.paint()
ANSWER = len(PROBLEM.colors)
assert ANSWER == 1709
utils.pretty_print_answer(1, len(PROBLEM.colors))

PROBLEM = Painter('input.txt')
PROBLEM.colors[PROBLEM.vector.magnitude] = 1
PROBLEM.paint()
print('answer to part 2:')
print(PROBLEM)
