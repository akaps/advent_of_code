class ComplexVector:
    def __init__(self):
        self.magnitude = 0j
        self.direction = 1j #facing north, or 1j

    def rotate(self, turn):
        self.direction *= turn

    def translate(self, dist):
        self.magnitude += dist * self.direction

    def __repr__(self):
        return '({x}, {y})'.format(x=self.magnitude.real, y=self.magnitude.imag)
