from collections import deque

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
    def __init__(self, file_name):
        file = open(file_name, 'r')
        data = file.readline().strip().split()
        file.close()
        data = deque([(int)(x) for x in data])
        self.root = TreeNode(data.popleft(), data.popleft())
        self.build(self.root, data)

    def build(self, curr, data):
        for _ in range(0, curr.len_children):
            child = TreeNode(data.popleft(), data.popleft())
            curr.children.append(child)
            self.build(child, data)
        for _ in range(0, curr.len_metadata):
            curr.metadata.append(data.popleft())

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

TREE = Tree('sample.txt')
assert TREE.sum_meta_data() == 138
assert TREE.value() == 66

TREE = Tree('input.txt')
print('Metadata sum is {sum}'.format(sum=TREE.sum_meta_data()))
print('Value of root is {value}'.format(value=TREE.value()))
