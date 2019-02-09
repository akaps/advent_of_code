from collections import deque
import sys

class TreeNode:
    def __init__(self, len_children, len_metadata):
        self.len_children = len_children
        self.len_metadata = len_metadata
        self.children = []
        self.metadata = []

    def __repr__(self):
        res = '' + str(self.metadata) + '\n'
        for child in self.children:
            res += str(child) + '\n'
        return res.strip()

class Tree:
    def __init__(self, inline):
        #sys.setrecursionlimit(8000)
        self.input = deque([(int)(x) for x in inline])
        self.root = TreeNode(self.input.popleft(), self.input.popleft())
        self.build(self.root)

    def build(self, curr):
        for _ in range(0, curr.len_children):
            child = TreeNode(self.input.popleft(), self.input.popleft())
            curr.children.append(child)
            self.build(child)
        for metadata in range(0, curr.len_metadata):
            curr.metadata.append(self.input.popleft())

    def sum_meta_data(self):
        return self.sum_meta_data_inner(self.root)

    def sum_meta_data_inner(self, curr):
        if not curr:
            return 0
        total = 0
        for child in curr.children:
            total += self.sum_meta_data_inner(child)
        return total + sum(curr.metadata)

    def value(self):
        return self.value_inner(self.root)

    def value_inner(self, curr):
        print('children at node: {children}'.format(children=curr.children))
        print('metadata at node: {meta}'.format(meta=curr.metadata))
        if not curr.len_children:
            print('leaf, sum is {sum}'.format(sum=sum(curr.metadata)))
            return sum(curr.metadata)
        total = 0
        for index in curr.metadata:
            print(index)
            if index < curr.len_children:
                total += self.value_inner(curr.children[index])
                print('total is now {total}'.format(total=total))
            else:
                print('index oob: {index}'.format(index=index))
        return total

    def __repr__(self):
        return str(self.root)

def make_tree(input):
    root = Tree(input[0], [input[1]])
    if input:
        root = make_tree(input)

file = open('sample.txt', 'r')
input = file.readline().strip().split()
file.close()
tree = Tree(input)

assert 138 == tree.sum_meta_data()
assert 10 == tree.value()

file = open('input.txt', 'r')
input = file.readline().strip().split()
file.close()
tree = Tree(input)
print('Metadata sum is {sum}'.format(sum=tree.sum_meta_data()))
print('Value of root is {value}'.format(value=tree.value()))
