import utils
from aoc2019.int_code import IntCode

NUM_COMPUTERS = 50
EMPTY = -1
PACKET_LENGTH = 3
HALT_PORT = 255

class Network:
    def __init__(self, input_file):
        self.programs = []
        self.queue = []
        computer = IntCode(input_file)
        for i in range(50):
            next_program = computer.load_program()
            next_program.send(None)
            next_program.send(i)
            self.queue.extend(next_program.send(EMPTY))
            self.programs.append(next_program)

    def run_network(self):
        while self.queue and len(self.queue) >= PACKET_LENGTH:
            port, x_val, y_val = self.queue[:PACKET_LENGTH]
            self.queue = self.queue[PACKET_LENGTH:]
            if port == HALT_PORT:
                return y_val
            current_program = self.programs[port]
            current_program.send(x_val)
            self.queue.extend(current_program.send(y_val))

PROBLEM = Network('input.txt')
ANSWER = PROBLEM.run_network()
assert ANSWER == 23057
utils.pretty_print_answer(1, ANSWER)
