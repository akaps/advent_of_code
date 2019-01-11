from collections import deque

class Polymers:
    def __init__(self, chain):
        self.chain = chain

    def reduce_given_chain(self):
        return self.reduce_chain(self.chain)

    def reduce_chain(self, chain):
        stack = deque()
        queue = deque(chain)
        while queue:
            stack.append(queue.popleft())
            if queue and self.equal_and_opposite(stack[-1], queue[0]):
                stack.pop()
                queue.popleft()
                if stack:
                    queue.appendleft(stack.pop())
        return str().join(stack)

    def equal_and_opposite(self, char_1, char_2):
        return char_1 != char_2 and char_1.lower() == char_2.lower()

    def remove_and_reduce(self, to_remove):
        chain = self.chain.replace(to_remove, '')
        chain = chain.replace(to_remove.upper(), '')
        chain = self.reduce_chain(chain)
        return len(chain)

file = open('day_5_input.txt', 'r')
polymer = file.readline().strip()
file.close()
res = Polymers(polymer) #'dabAcCaCBAcCcaDA'->10
print('reduced polymer is {size} units long'.format(size=len(res.reduce_given_chain())))

letters = [] #letter : size
for letter in 'abcdefghijklmnopqrstuvwxyz':
    chain_size = res.remove_and_reduce(letter)
    letters.append(chain_size)
print('minimum chain size is {size}'.format(size=min(letters)))
