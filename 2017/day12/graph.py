import re

class Graph:
    def __init__(self, file_name):
        file =open(file_name, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        self.ids = {}
        self.populate_graph(lines)

    def populate_graph(self, lines):
        for line in lines:
            id, connections = re.split(r' <-> ', line)
            connections = re.split(r', ', connections)
            for connection in connections:
                self.add_connection(id, connection)
                self.add_connection(connection, id)

    def add_connection(self, id_1, id_2):
        if id_1 not in self.ids:
            self.ids[id_1] = set()
        self.ids[id_1].add(id_2)

    def dfs(self, id):
        processed = set()
        return self.dfs_inner(id, processed)

    def dfs_inner(self, id, processed):
        processed.add(id)
        for node in self.ids[id]:
            if node not in processed:
                self.dfs_inner(node, processed)
        return processed

    def number_of_groups(self):
        total = 0
        processed = set()
        for node in self.ids.keys():
            if node not in processed:
                self.dfs_inner(node, processed)
                total += 1
        return total

SAMPLE = Graph('sample.txt')
DFS = SAMPLE.dfs('0')
assert len(DFS) == 6

PROBLEM = Graph('input.txt')
DFS = PROBLEM.dfs('0')
print('Answer to part 1: {ans}'.format(ans=len(DFS)))

assert SAMPLE.number_of_groups() == 2
print('Answer to part 2: {ans}'.format(ans=PROBLEM.number_of_groups()))
