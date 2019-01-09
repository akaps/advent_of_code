from collections import deque
import sys

class TreeNode:
    def __init__(self, len_children, len_metadata):
        self.len_children = len_children
        self.len_metadata = len_metadata
        self.children = []
        self.metadata = []

class Tree:
    def __init__(self, input):
        #sys.setrecursionlimit(8000)
        self.input = input
        self.root = TreeNode(self.input.popleft(), self.input.popleft())
        self.build(self.root)

    def build(self, curr):
        for _ in range(0, curr.len_children):
            child = TreeNode(self.input.popleft(), self.input.popleft())
            curr.children.append(child)
            self.build(child)
        for metadata in range(0, curr.len_metadata):
            curr.metadata.append(input.popleft())

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
        print('node has {num} children'.format(num=curr.len_children))
        if not curr.len_children:
            print('value is {total}'.format(total=sum(curr.metadata)))
            return sum(curr.metadata)
        total = 0
        print(curr.metadata)
        for index in curr.metadata:
            print('check {index}, {len}'.format(index=index, len=curr.len_children))
            if index < curr.len_children:
                val = self.value_inner(curr.children[index])
                print('child value is {val}'.format(val=val))
                total += val
            else:
                print('OOB index {index}. value is 0'.format(index=index))
                total += 0
        return total

def make_tree(input):
    root = Tree(input[0], [input[1]])
    if input:
        root = make_tree(input)

sys.setrecursionlimit(2000)
file = open('day_8_sample.txt', 'r')
input = file.readline().strip().split()
input = deque([(int)(x) for x in input])
file.close()
tree = Tree(input)
print('Metadata sum is {sum}'.format(sum=tree.sum_meta_data()))
print('Value of root is {value}'.format(value=tree.value()))
