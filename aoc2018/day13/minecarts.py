from complexvector import ComplexVector

NORTH = '^'
SOUTH = 'v'
WEST = '<'
EAST = '>'
DIRECTIONS = ''.join([NORTH, EAST, SOUTH, WEST])
HORIZONTAL = '-'
VERTICAL = '|'
JUNCTION = '+'
CURVES = '/\\'
LEFT = -1j
RIGHT = 1j
STRAIGHT = 1
TURNS = (LEFT, STRAIGHT, RIGHT)

class Minecart(ComplexVector):
    def __init__(self, magnitude, direction):
        ComplexVector.__init__(self, magnitude, direction)
        self.next_turn = 0

    def update_turn_behavior(self):
        self.next_turn = (self.next_turn + 1) % 3

class Minecarts:
    def __init__(self, file_name):
        file = open(file_name, 'r')
        lines = [x.rstrip() for x in file.readlines()]
        file.close()
        self.track = []
        self.carts = []
        self.generate_track(lines)
        self.crashes = []

    def generate_track(self, lines):
        for row, line in enumerate(lines):
            to_process = list(line)
            for col, val in enumerate(to_process):
                if val in DIRECTIONS:
                    #make a cart
                    magnitude = row + col * 1j
                    direction = facing(val)
                    self.carts.append(Minecart(magnitude, direction))
                    #replace the track with the proper representation
                    if val in [NORTH, SOUTH]:
                        to_process[col] = VERTICAL
                    if val in [EAST, WEST]:
                        to_process[col] = HORIZONTAL
            self.track.append(to_process)

    def run(self):
        while len(self.carts) > 1:
            self.carts.sort(key=lambda vector:
                            vector.magnitude.imag < vector.magnitude.imag
                            if vector.magnitude.real == vector.magnitude.real
                            else vector.magnitude.real < vector.magnitude.real)
            print('---')
            for cart in self.carts:
                print(cart)
                cart.translate(1)
                self.check_for_crash(cart)
                self.turn_cart(cart)
        if self.carts:
            last_cart = self.carts[0]
            return location(last_cart)
        return None

    def turn_cart(self, cart):
        row, col = location(cart)
        track = self.track[row][col]
        if track in CURVES:
            cart.rotate(take_curve(cart.direction, track))
        elif track == JUNCTION:
            cart.rotate(TURNS[cart.next_turn])
            cart.update_turn_behavior()

    def check_for_crash(self, cart):
        for other_cart in [c for c in self.carts if c != cart]:
            if cart.magnitude == other_cart.magnitude:
                print('CRASH at {loc}'.format(
                    loc=cart.magnitude))
                #Hack, implementation uses x as row and y as column
                #This is reverse of the problem spec
                self.crashes.append(location(cart))
                self.carts.remove(cart)
                self.carts.remove(other_cart)
                print('new number of carts: {size}'.format(
                    size=len(self.carts)))
                return

def facing(char):
    switcher = {
        NORTH : -1,
        SOUTH : 1,
        EAST : 1j,
        WEST : -1j
    }
    return switcher.get(char)

def location(last_cart):
    return int(last_cart.magnitude.real), int(last_cart.magnitude.imag)

def take_curve(heading, curve):
    if curve == '\\':
        if heading.real == 0: #N/S heading
            return LEFT
        return RIGHT
    if heading.real == 0: #N/S heading
        return RIGHT
    return LEFT

LINE = Minecarts('line.txt')
LINE.run()
assert LINE.crashes[0] == (3, 0)

SAMPLE = Minecarts('sample.txt')
SAMPLE.run()
print(SAMPLE.crashes)
assert SAMPLE.crashes[0] == (3, 7)

PROBLEM = Minecarts('input.txt')
LAST_CART = PROBLEM.run()
print('Answer to Part 1: {ans}'.format(
    ans=PROBLEM.crashes[0]))

SAMPLE = Minecarts('sample_pt2.txt')
LAST_CART = SAMPLE.run()
assert SAMPLE.crashes[0] == (0, 2)
assert SAMPLE.crashes[1] == (4, 2)
assert SAMPLE.crashes[2] == (4, 6)
assert SAMPLE.crashes[3] == (4, 2)
assert LAST_CART == (4, 6)

CRASHES = PROBLEM.crashes
assert CRASHES[0] == (107, 28)
assert CRASHES[1] == (103, 47)
assert CRASHES[2] == (85, 91)
assert CRASHES[3] == (80, 6)
assert CRASHES[4] == (54, 39)
assert CRASHES[5] == (37, 134)
assert CRASHES[6] == (100, 26)
assert CRASHES[7] == (-1, -1)
print('Answer to Part 2: {ans}'.format(
    ans=LAST_CART))
