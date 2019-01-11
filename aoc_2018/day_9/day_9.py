import re

class Marble:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return '{l}<-{v}->{r}'.format(l=self.left.val, v=self.val, r=self.right.val)

def play_game(input):
    players, last_marble = parse_input(input)
    to_play = range(2, last_marble + 1)
    list_players = [0] * players
    zero = current_marble = Marble(0)
    next = Marble(1)
    next.left, next.right = current_marble, current_marble
    current_marble.left, current_marble.right = next, next
    current_marble = current_marble.right
    current_player = 0
    for next_marble in to_play:
        if not next_marble % 23:
            removed = current_marble.left.left.left.left.left.left.left
            removed.left.right, removed.right.left = removed.right, removed.left
            current_marble = removed.right
            list_players[current_player] += next_marble + removed.val
        else:
            to_add = Marble(next_marble)
            current_marble = current_marble.right #hack to get my bad math to work :)
            to_add.left, to_add.right = current_marble, current_marble.right
            to_add.right.left = to_add
            current_marble.right = to_add
            current_marble = to_add
        current_player = (current_player + 1) % len(list_players)
    return max(list_players)

def rep(curr):
    res = [curr.val]
    curr = curr.right
    while curr.val != 0:
        res.append(curr.val)
        curr = curr.right
    return res

def rep_backwards(curr):
    res = [curr.val]
    curr = curr.left
    while curr.val != 0:
        res.append(curr.val)
        curr = curr.left
    return res

def parse_input(input):
    vals = re.split('^| players; last marble is worth | points$', input)
    return [(int)(val) for val in vals[1:3]]

sample_1 = '9 players; last marble is worth 25 points'
sample_2 = '10 players; last marble is worth 1618 points'
sample_3 = '13 players; last marble is worth 7999 points'
sample_4 = '17 players; last marble is worth 1104 points'
sample_5 = '21 players; last marble is worth 6111 points'
sample_6 = '30 players; last marble is worth 5807 points'
input = '428 players; last marble is worth 72061 points'
input_10 = '428 players; last marble is worth 720610 points'
input_100 = '428 players; last marble is worth 7206100 points'

assert 32 == play_game(sample_1)
assert 8317 == play_game(sample_2)
assert 146373 == play_game(sample_3)
assert 2764 == play_game(sample_4)
assert 54718 == play_game(sample_5)
assert 37305 == play_game(sample_6)
print('Answer is {ans}'.format(ans=play_game(input)))
print('Answer to part 2')
print(play_game(input_100))
