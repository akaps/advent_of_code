import utils

class CubicLife:
    def __init__(self, file_name):
        z_index = 0
        w_index = 0
        self.cells = {}
        matrix = utils.read_matrix(file_name)
        for x_index, row in enumerate(matrix):
            for y_index, val in enumerate(row):
                if val == '#':
                    self.cells[(x_index, y_index, z_index, w_index)] = True

    def count_adj(self, coordinate, is_4d=False):
        count = 0
        adj = get_adj(coordinate, is_4d)
        for coord in adj:
            if coord in self.cells:
                count += 1
        return count

    def run_cycle(self, is_4d=False):
        next_generation = {}
        accounted = set()
        to_process = []
        to_process.extend(self.cells.keys())
        for cell_coordinate in self.cells:
            adj = get_adj(cell_coordinate, is_4d)
            for adj_cell_coordinate in adj:
                if not adj_cell_coordinate in accounted:
                    accounted.add(adj_cell_coordinate)
                    to_process.append(adj_cell_coordinate)
            accounted.add(cell_coordinate)
        for cell_coordinate in to_process:
            state = self.cells[cell_coordinate] if cell_coordinate in self.cells else False
            neighbors = self.count_adj(cell_coordinate, is_4d)
            if state and 2 <= neighbors <= 3:
                next_generation[cell_coordinate] = True
            elif not state and neighbors == 3:
                next_generation[cell_coordinate] = True
        self.cells = next_generation

    def count_live(self):
        return len(self.cells)

def get_adj(coordinate, is_4d=False):
    adj = []
    for x_mod in range(-1, 2):
        for y_mod in range(-1, 2):
            for z_mod in range(-1, 2):
                if is_4d:
                    for w_mod in range(-1, 2):
                        if not x_mod == y_mod == z_mod == w_mod == 0:
                            adj.append((coordinate[0] + x_mod,
                                        coordinate[1] + y_mod,
                                        coordinate[2] + z_mod,
                                        coordinate[3] + w_mod))
                elif not x_mod == y_mod == z_mod == 0:
                    adj.append((coordinate[0] + x_mod,
                                coordinate[1] + y_mod,
                                coordinate[2] + z_mod,
                                coordinate[3]))
    return adj

def main():
    life = CubicLife('input.txt')
    for _ in range(6):
        life.run_cycle()
    utils.pretty_print_answer(1, life.count_live())

    life = CubicLife('input.txt')
    for _ in range(6):
        life.run_cycle(is_4d=True)
    utils.pretty_print_answer(2, life.count_live())

if __name__ == "__main__":
    main()
