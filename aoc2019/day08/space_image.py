from PIL import Image as Visual
import utils

WIDTH = 25
HEIGHT = 6

BLACK = 0
WHITE = 1
TRANSPARENT = 2

class SpaceImageLayer:
    def __init__(self, input_string, width, height):
        self.layer = []
        self.digits = {}
        for x in range(height):
            row = []
            for y in range(width):
                val = int(input_string[x * width + y])
                row.append(val)
                if val in self.digits:
                    self.digits[val] += 1
                else:
                    self.digits[val] = 1
            self.layer.append(row)

    def count_digit(self, number):
        if number in self.digits:
            return self.digits[number]
        return 0

class SpaceImage:
    def __init__(self, input_string, width, height):
        self.width = width
        self.height = height
        self.layers = []
        layer_width = width * height
        while input_string:
            self.layers.append(SpaceImageLayer(input_string[:layer_width], width, height))
            input_string = input_string[layer_width:]

    def layer_with_fewest_zeroes(self):
        fewest, fewest_layer = self.width * self.height, -1
        for index, layer in enumerate(self.layers):
            count = layer.count_digit(0)
            if count < fewest:
                fewest = count
                fewest_layer = index
        return fewest_layer

    def color_for_point(self, row, col):
        curr_depth = 0
        while (curr_depth < len(self.layers)
               and self.layers[curr_depth].layer[row][col] == TRANSPARENT):
            curr_depth += 1
        result = self.layers[curr_depth].layer[row][col]
        assert result != TRANSPARENT, (
            'expected result is transparent at {pos}'.format(pos=(row, col)))
        return result

    def render_image(self):
        result = []
        for x in range(self.height):
            row = []
            for y in range(self.width):
                row.append(self.color_for_point(x, y))
            result.append(row)
        return result

SAMPLE = '123456789012'
SAMPLE_IMAGE = SpaceImage(SAMPLE, 3, 2)
assert SAMPLE_IMAGE.layers[0].count_digit(0) == 0
assert SAMPLE_IMAGE.layers[1].count_digit(0) == 1
assert SAMPLE_IMAGE.layer_with_fewest_zeroes() == 0
assert SAMPLE_IMAGE.layers[0].count_digit(1) == 1
assert SAMPLE_IMAGE.layers[0].count_digit(2) == 1

FILE = open('input.txt')
INPUT = FILE.readline().strip()
FILE.close()
PROBLEM = SpaceImage(INPUT, WIDTH, HEIGHT)
PART_A_LAYER = PROBLEM.layer_with_fewest_zeroes()
PART_A = (PROBLEM.layers[PART_A_LAYER].count_digit(1)
          * PROBLEM.layers[PART_A_LAYER].count_digit(2))
assert PART_A == 1584
utils.pretty_print_answer(1, PART_A)

SAMPLE_IMAGE = SpaceImage('0222112222120000', 2, 2)
assert SAMPLE_IMAGE.render_image() == [[0, 1], [1, 0]]
PART_B = PROBLEM.render_image()
utils.pretty_print_answer(2, 'rendered via Pillow')
# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
IMG = Visual.new('RGB', (WIDTH, HEIGHT), 'black') # create a new black image
PIXELS = IMG.load() # create the pixel map
for row_index, row in enumerate(PART_B):
    for col_index, val in enumerate(row):
        PIXELS[col_index, row_index] = (254 * val, 0, 100) # set the colour accordingly
IMG.show()
