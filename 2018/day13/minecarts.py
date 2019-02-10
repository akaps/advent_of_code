import copy

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'
CARTS = ''.join([UP, RIGHT, DOWN, LEFT])
HORIZONTAL = '-'
VERTICAL = '|'
JUNCTION = '+'
CURVES = '\/'
STRAIGHT = ''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, point):
        self.x += point.x
        self.y += point.y

    def __repr__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            print('the same!')
            return self.x == other.x and self.y == other.y
        else:
            return False

def get_mods(dir):
    dirs = {
        UP: Point(-1, 0),
        DOWN: Point(1, 0),
        LEFT: Point(0, -1),
        RIGHT: Point(0, 1),
    }
    return dirs.get(dir, "Invalid direction")

#implementing carts as a vector
class Cart:
    def __init__(self, location, direction):
        self.location = location
        self.direction = direction
        self.junction_behavior = LEFT

    def turn(self, new_direction):
        self.direction = new_direction

    def move(self):
        self.location.translate(get_mods(self.direction))

    def update_junction_behavior(self):
        if self.junction_behavior == LEFT:
            self.junction_behavior = STRAIGHT
        elif self.junction_behavior == STRAIGHT:
            self.junction_behavior = RIGHT
        else:
            self.junction_behavior = LEFT

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
                if char in CARTS:
                    #make a cart
                    point = Point(line_enum[0], char_enum[0])
                    self.carts.append(Cart(point, line_enum[1]))
                    #replace the track with the proper representation
                    if line_enum[1] == LEFT or line_enum[1] == RIGHT:
                        to_process[char_enum[0]] = HORIZONTAL
                    elif line_enum[1] == DOWN or line_enum[1] == UP:
                        to_process[char_enum[0]] = VERTICAL
            self.track.append(to_process)

    def run(self):
        while not self.crash:
            self.move_carts()
            self.check_for_crashes()

    def move_carts(self):
        for cart in self.carts:
            cart.move()
            new_loc = cart.location
            if self.track[new_loc.x][new_loc.y] in CURVES:
                print('uh-oh, haven\'t figure this out!')
            elif self.track[new_loc.x][new_loc.y] == JUNCTION:
                print('did not start this either!')

    def check_for_crashes(self):
        print('all: {carts}'.format(carts=self.carts))
        for cart in self.carts:
            print('looking at: {cart}'.format(cart=cart))
            for other_cart in [c for c in self.carts if c != cart]:
                print('checking against {cart}'.format(cart=other_cart))
                if cart.location == other_cart.location:
                    print('BANG!')
                    self.crash = cart.location
                    return

LINE = Minecarts('line.txt')
LINE.run()
assert LINE.crash == Point(3, 0)

SAMPLE = Minecarts('sample.txt')
SAMPLE.run()
assert SAMPLE.crash == Point(7, 3)

PROBLEM = Minecarts('input.txt')
PROBLEM.run()
print('Answer to Part 1: {ans}'.format(ans=PROBLEM.crash))
