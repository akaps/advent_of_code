class Matrix:
    def __init__(self, num_rows, num_cols):
        self.matrix = []
        for _ in range(num_rows):
            self.matrix.append([0 * num_cols])
