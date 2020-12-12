import re
from turtle import Turtle
import utils

DIRECTIONS_REGEX = r'(\w)(\d+)'

N = 'N'
S = 'S'
E = 'E'
W = 'W'
L = 'L'
R = 'R'
F = 'F'

class Ship:
    def __init__(self, file_name):
        self.directions = []
        lines = utils.read_lines(file_name)
        for line in lines:
            action, distance = re.match(DIRECTIONS_REGEX, line).groups()
            self.directions.append((action, int(distance)))

    def travel(self):
        turtle = Turtle()
        turtle.screen.screensize(640, 480)
        turtle.screen.setworldcoordinates(-10, -1000, 1000, 200)
        turtle.setheading(0)
        turtle.speed(0)
        for action, magnitude in self.directions:
            if action == N:
                turtle.sety(turtle.ycor() + magnitude)
            elif action == S:
                turtle.sety(turtle.ycor() - magnitude)
            elif action == E:
                turtle.setx(turtle.xcor() + magnitude)
            elif action == W:
                turtle.setx(turtle.xcor() - magnitude)
            elif action == L:
                turtle.left(magnitude)
            elif action == R:
                turtle.right(magnitude)
            elif action == F:
                turtle.forward(magnitude)
            else:
                assert False, 'Unexpected direciton {dir}'.format(dir=action)
        return abs(turtle.xcor()) + abs(turtle.ycor())

    def waypoint_travel(self):
        ship = Turtle()
        ship.screen.clearscreen()
        ship.screen.setworldcoordinates(-19295, -76725, 25115, 3795)
        ship.setheading(0)
        ship.speed(0)
        waypoint = Turtle()
        waypoint.setx(10)
        waypoint.sety(1)
        waypoint.speed(0)
        waypoint.color('Red')
        for action, magnitude in self.directions:
            if action == N:
                waypoint.sety(waypoint.ycor() + magnitude)
            elif action == S:
                waypoint.sety(waypoint.ycor() - magnitude)
            elif action == E:
                waypoint.setx(waypoint.xcor() + magnitude)
            elif action == W:
                waypoint.setx(waypoint.xcor() - magnitude)
            elif action == L:
                rotate(waypoint, magnitude)
            elif action == R:
                rotate(waypoint, 360 - magnitude)
            elif action == F:
                ship.setx(ship.xcor() + (waypoint.xcor() * magnitude))
                ship.sety(ship.ycor() + (waypoint.ycor() * magnitude))
            else:
                assert False, 'Unexpected direction {dir}'.format(dir=action)
        return abs(ship.xcor()) + abs(ship.ycor())

def rotate(turtle, magnitude):
    temp = turtle.xcor()
    if magnitude == 90:
        turtle.setx(-turtle.ycor())
        turtle.sety(temp)
    elif magnitude == 180:
        turtle.setx(-turtle.xcor())
        turtle.sety(-turtle.ycor())
    elif magnitude == 270:
        turtle.setx(turtle.ycor())
        turtle.sety(-temp)
    else:
        assert False, 'Unexpected magnitude {mag}'.format(mag=magnitude)

def main():
    ship = Ship('input.txt')
    utils.pretty_print_answer(1, ship.travel())
    utils.pretty_print_answer(2, ship.waypoint_travel())

if __name__ == "__main__":
    main()
