from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = defaultdict(set())

    def add_link(self, source_vertex, destination_vertex):
        self.vertices[source_vertex].add(destination_vertex)

    def add_bidi_link(self, vertex1, vertex2):
        self.add_link(vertex1, vertex2)
        self.add_link(vertex2, vertex1)
