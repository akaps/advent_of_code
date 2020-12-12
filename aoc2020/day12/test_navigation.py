from turtle import Turtle
import pytest
from aoc2020.day12.navigation import rotate

@pytest.fixture()
def turtle():
    new_turtle = Turtle()
    new_turtle.setpos(1, 2)
    yield new_turtle

def test_rotate_90(turtle):
    rotate(turtle, 90)
    assert turtle.pos() == (-2, 1)

def test_rotate_180(turtle):
    rotate(turtle, 180)
    assert turtle.pos() == (-1, -2)

def test_rotate_270(turtle):
    rotate(turtle, 270)
    assert turtle.pos() == (2, -1)

def test_rotate_neg90(turtle):
    rotate(turtle, 360-90)
    assert turtle.pos() == (2, -1)

def test_rotate_neg180(turtle):
    rotate(turtle, 360-180)
    assert turtle.pos() == (-1, -2)

def test_rotate_neg270(turtle):
    rotate(turtle, 360-270)
    assert turtle.pos() == (-2, 1)

def test_multiple_rotates(turtle):
    rotate(turtle, 90)
    assert turtle.pos() == (-2, 1)
    rotate(turtle, 90)
    assert turtle.pos() == (-1, -2)
    rotate(turtle, 90)
    assert turtle.pos() == (2, -1)
    rotate(turtle, 90)
    assert turtle.pos() == (1, 2)

def test_180_identity(turtle):
    rotate(turtle, 180)
    assert turtle.pos() == (-1, -2)
    rotate(turtle, 180)
    assert turtle.pos() == (1, 2)

def test_270_identity(turtle):
    rotate(turtle, 270)
    assert turtle.pos() == (2, -1)
    rotate(turtle, 270)
    assert turtle.pos() == (-1, -2)
    rotate(turtle, 270)
    assert turtle.pos() == (-2, 1)
    rotate(turtle, 270)
    assert turtle.pos() == (1, 2)
