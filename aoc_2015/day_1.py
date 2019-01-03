from collections import deque

class Elevators:
    def __init__(self):
        self.first = 0
        self.bottom = False
        pass

    def calculate_floors(self, input):
        floor = 0
        for paren in input:
            if not self.bottom:
                self.first += 1
            if paren == '(':
                floor += 1
            elif paren == ')':
                floor -= 1
            if floor == -1:
                self.bottom = True
        return floor

elevators = Elevators()
file = open('day_1_input.txt')
input = file.read().strip()
file.close()
print(elevators.calculate_floors(input))
print(elevators.first)
