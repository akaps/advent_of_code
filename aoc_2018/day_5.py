from collections import deque

class Polymers:
    def __init__(self, chain):
        self.chain = chain

    def reduce_chain(self):
        stack = deque()
        queue = deque(self.chain)
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

file = open('day_5_input.txt', 'r')
polymer = file.readline().strip()
file.close()
res = Polymers(polymer) #'dabAcCaCBAcCcaDA'->10
print('reduced polymer is {size} units long'.format(size=len(res.reduce_chain())))
