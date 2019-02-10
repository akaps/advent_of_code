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

def direction(char):
    switcher = {
        NORTH : -1j,
        SOUTH : 1j,
        EAST : 1,
        WEST : -1
    }
    return switcher.get(char)

#implementing carts as a complex vector
#y is flipped, so -j is up, and j is down
class Cart:
    def __init__(self, location, heading):
        assert heading != 0j
        self.location = location
        self.direction = heading
        self.next_turn = 0

    def move(self):
        self.location += self.direction

    def turn(self, rotation):
        assert rotation != 0j
        self.direction *= rotation

    def update_turn_behavior(self):
        self.next_turn = (self.next_turn + 1) % 3

    def __repr__(self):
        return 'Cart at {p} going {dir}'.format(p=self.location, dir=self.direction)

class Minecarts:
    def __init__(self, file_name):
        file = open(file_name, 'r')
        lines = [x.strip() for x in file.readlines()]
        file.close()
        self.generate_track(lines)
        self.crash = None

    def generate_track(self, lines):
        self.track = []
        self.carts = []
        for line_enum in enumerate(lines):
            to_process = list(line_enum[1])
            for char_enum in enumerate(to_process):
                char = char_enum[1]
                if char in DIRECTIONS:
                    #make a cart
                    point = (line_enum[0] * 1j + char_enum[0])
                    self.carts.append(Cart(point, direction(char)))
                    #replace the track with the proper representation
                    if char in (EAST, WEST):
                        to_process[char_enum[0]] = HORIZONTAL
                    elif char in (SOUTH, NORTH):
                        to_process[char_enum[0]] = VERTICAL
            self.track.append(to_process)

    def run(self):
        while not self.crash:
            self.move_carts()
            self.check_for_crashes()

    def move_carts(self):
        for cart in self.carts:
            self.validate_cart(cart)
            cart.move()
            new_loc = cart.location
            track = self.track[int(new_loc.imag)][int(new_loc.real)]
            if track in CURVES:
                print('turn for {cart}'.format(cart=cart))
                cart.turn(take_curve(cart.direction, track))
                print('Cart is now {cart}'.format(cart=cart))
            elif track == JUNCTION:
                print('junction for {cart}'.format(cart=cart))
                cart.turn(TURNS[cart.next_turn])
                cart.update_turn_behavior()
                print('Cart is now {cart}'.format(cart=cart))

    def validate_cart(self, cart):
        track_piece = self.track[int(cart.location.imag)][int(cart.location.real)]
        if cart.direction in (EAST, EAST):
            assert track_piece in (HORIZONTAL, JUNCTION) or track_piece in CURVES
        elif cart.direction in (NORTH, SOUTH):
            assert track_piece in (VERTICAL, JUNCTION) or track_piece in CURVES

    def check_for_crashes(self):
        for cart in self.carts:
            for other_cart in [c for c in self.carts if c != cart]:
                if cart.location == other_cart.location:
                    print('BANG!')
                    #Hack, implementation uses x as row and y as column
                    #This is reverse of the problem spec
                    self.crash = int(cart.location.real), int(cart.location.imag)
                    return


def take_curve(heading, curve):
    if curve == '\\':
        if heading.real == 0: #N/S heading
            return LEFT
        return RIGHT
    if heading.real == 0:
        return RIGHT
    return LEFT

LINE = Minecarts('line.txt')
LINE.run()
assert LINE.crash == (0, 3)

SAMPLE = Minecarts('sample.txt')
SAMPLE.run()
assert SAMPLE.crash == (7, 3)

PROBLEM = Minecarts('input.txt')
PROBLEM.run()
print('Answer to Part 1: {ans}'.format(ans=PROBLEM.crash))
