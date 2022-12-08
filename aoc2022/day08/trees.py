class Trees:
    def __init__(self, file_name):
        file_input = open(file_name)
        lines = [s.strip() for s in file_input.readlines()]
        file_input.close()
        self.grove = [[int(x) for x in line] for line in lines]

    def is_visible_dir(self, x, y, x_pos, y_pos):
        height = self.grove[x][y]
        x += x_pos
        y += y_pos
        while x >= 0 and x < len(self.grove) and y >= 0 and y < len(self.grove):
            if self.grove[x][y] >= height:
                return False
            x += x_pos
            y += y_pos
        return True

    def is_visible(self, x, y):
        return (self.is_visible_dir(x, y, -1, 0)
            or self.is_visible_dir(x, y, 1, 0)
            or self.is_visible_dir(x, y, 0, -1)
            or self.is_visible_dir(x, y, 0, 1))

    def count_visible(self):
        edge = (len(self.grove) * 2) + (len(self.grove[0]) * 2) - 4
        inner = 0
        for x in range(1, len(self.grove) - 1):
            for y in range(1, len(self.grove[0]) -1):
                if self.is_visible(x, y):
                    inner += 1
        return edge + inner

    def view(self, x, y, x_pos, y_pos):
        distance = 0
        height = self.grove[x][y]
        x += x_pos
        y += y_pos
        while x >= 0 and x < len(self.grove) and y >= 0 and y < len(self.grove):
            distance += 1
            if self.grove[x][y] < height:
                x += x_pos
                y += y_pos
            else:
                return distance
        return distance

    def max_visible(self):
        #xpos, ypos, total
        max = {'x':None, 'y':None, 'score':-1}
        for x in range(len(self.grove)):
            for y in range(len(self.grove)):
                score = (self.view(x, y, -1, 0)
                    * self.view(x, y, 1, 0)
                    * self.view(x, y, 0, -1)
                    * self.view(x, y, 0, 1))
                if score > max['score']:
                    max['score'] = score
                    max['x'] = x
                    max['y'] = y
        return max['score']

def main():
    sample = Trees('sample.txt')
    assert sample.count_visible() == 21
    grove = Trees('input.txt')
    print('Part 1: ', grove.count_visible())

    sample = Trees('sample2.txt')
    assert sample.max_visible() == 8
    grove = Trees('input.txt')
    print('Part 2:', grove.max_visible())

if __name__ == '__main__':
    main()
