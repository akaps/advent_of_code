import utils

WIDTH = 25
HEIGHT = 6

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

SAMPLE = '123456789012'
SAMPLE_WIDTH = 3
SAMPLE_HEIGHT = 2
SAMPLE_IMAGE = SpaceImage(SAMPLE, SAMPLE_WIDTH, SAMPLE_HEIGHT)
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

utils.pretty_print_answer(2, -2)
