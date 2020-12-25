from turtle import Turtle
import utils

class Maze:
    def __init__(self, file_name, wall_val):
        Maze.walls = wall_val
        lines = utils.read_lines(file_name)
        self.maze = []
        self.walker = Turtle()
        for line in lines:
            self.maze.append(list(line))

    def search(self, target):
        assert 'Unimplemented'
