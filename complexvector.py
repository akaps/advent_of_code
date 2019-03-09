class ComplexVector:
    def __init__(self, magnitude=0j, direction=1j):
        self.magnitude = magnitude
        self.direction = direction #facing north, or 1j

    def rotate(self, turn):
        self.direction *= turn

    def translate(self, dist):
        self.magnitude += dist * self.direction

    def __repr__(self):
        return '({x}, {y}), heading ({x_v}, {y_v})'.format(x=self.magnitude.real,
                                                           y=self.magnitude.imag,
                                                           x_v=self.direction.real,
                                                           y_v=self.direction.imag)
