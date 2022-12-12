from queue import PriorityQueue

START = 'S'
END = 'E'

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Mountain:
    def __init__(self, file_name):
        file_input = open(file_name)
        self.map = [list(row.strip()) for row in file_input.readlines()]
        file_input.close()
        self.start = None
        self.end = None
        for row_index, row in enumerate(self.map):
            for col_index, val in enumerate(row):
                if val == START:
                    self.start = (row_index, col_index)
                    self.map[row_index][col_index] = 'a'
                elif val == END:
                    self.end = (row_index, col_index)
                    self.map[row_index][col_index] = 'z'
        assert self.start
        assert self.end

    def estimated_distance(self, location):
        return abs(location[0] - self.end[0]) + abs(location[1] - self.end[1])

    def distance_to_end(self):
        came_from, cost_so_far = self.a_star()
        return cost_so_far[self.end]

    def a_star(self):
        frontier = PriorityQueue()
        frontier.put(self.start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[self.start] = None
        cost_so_far[self.start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == self.end:
                break

            for next in self.candidates(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.estimated_distance(next)
                    frontier.put(next, priority)
                    came_from[next] = current

        print(cost_so_far)
        return came_from, cost_so_far

    def candidates(self, location):
        result = []
        elevation = self.map[location[0]][location[1]]
        for direction in directions:
            new_x = location[0] + direction[0]
            new_y = location[1] + direction[1]
            if (self.in_bounds(new_x, new_y)
                    and abs(ord(elevation) - ord(self.map[new_x][new_y])) <= 1):
                result.append((new_x, new_y))
        return result

    def in_bounds(self, x, y):
        return (x >= 0
            and x < len(self.map)
            and y >= 0
            and y < len(self.map[0]))

def main():
    map = Mountain('sample.txt')
    assert map.distance_to_end() == 31

    map = Mountain('input.txt')
    print('Part 1: ', map.distance_to_end())

if __name__ == '__main__':
    main()
