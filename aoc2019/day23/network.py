from int_code import IntCode, MissingInputError

NUM_COMPUTERS = 50
EMPTY = -1
PACKET_LENGTH = 3
HALT_PORT = 255

class Network:
    def __init__(self, input_file):
        self.computers = []
        self.queue = []
        for i in range(50):
            next_comp = IntCode(input_file)
            try:
                next_comp.run_program([i, EMPTY])
            except MissingInputError:
                self.queue.extend(next_comp.output)
                next_comp.output = []
            self.computers.append(next_comp)

    def run_network(self):
        while self.queue and len(self.queue) >= PACKET_LENGTH:
            port, x_val, y_val = self.queue[:PACKET_LENGTH]
            self.queue = self.queue[PACKET_LENGTH:]
            if port == HALT_PORT:
                return y_val
            current_computer = self.computers[port]
            try:
                current_computer.run_program([x_val, y_val])
            except MissingInputError:
                self.queue.extend(current_computer.output)
                current_computer.output = []

PROBLEM = Network('input.txt')
print(PROBLEM.run_network())
