import re

class TrieNode:
    def __init__(self, input_line):
        self.data, self.size = parse(input_line)
        self.children = []

    def __repr__(self):
        res = [self.data]
        if self.children:
            res.append('->')
            res.append(', '.join([str(child) for child in self.children]))
        return ''.join(res)

    def depth(self):
        if self.children:
            return 1 + max([child.depth() for child in self.children])
        return 1

class Trie:
    def __init__(self, file_name):
        file = open(file_name)
        inputs = file.readlines()
        file.close()
        self.root = populate(inputs)

def populate(lines):
    nodes = {}
    to_process = {}
    for line in lines:
        line = line.strip()
        if ' -> ' in line:  #has children
            data, children = re.split(' -> ', line)
            node = TrieNode(data)
            nodes[node.data] = node
            to_process[node.data] = re.split(', ', children)
        else:   #is leaf
            node = TrieNode(line)
            nodes[node.data] = node
    link_children(nodes, to_process)
    return find_root(nodes)

def find_root(nodes):
    max_depth = 0
    max_node = None
    for name, node in nodes.items():
        depth = node.depth()
        if depth > max_depth:
            max_depth = depth
            max_node = node
    return max_node

def link_children(nodes, to_process):
    for node, children in to_process.items():
        for child in children:
            nodes[node].children.append(nodes[child])

def parse(input_line):
    number = input_line.index('(')
    return input_line[: number - 1], int(input_line[number + 1: -1])

SAMPLE = Trie('sample.txt')
assert SAMPLE.root.data == 'tknk'

PROBLEM = Trie('input.txt')
print('Answer to part 1: {ans}'.format(ans=PROBLEM.root.data))
