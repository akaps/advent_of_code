import re

def play_game(input):
    players, last_marble = parse_input(input)
    to_play = [i for i in range(last_marble + 1) if i != 0]
    list_players = [0] * players
    circle = [0]
    current_marble = 0
    current_player = 0
    while to_play:
        #print(circle)
        #print('player_scores: {scores}'.format(scores=list_players))
        next_marble = to_play.pop(0)
        if not next_marble % 23:
            #print('buzz')
            to_remove = (current_marble - 7 + len(circle)) % len(circle)
            removed = circle.pop(to_remove)
            #print(removed)
            list_players[current_player] += next_marble + removed
            current_marble = to_remove % len(circle)
        else:
            where_to_play = (current_marble + 1) % len(circle) + 1
            circle.insert(where_to_play, next_marble)
            current_marble = where_to_play
        current_player += 1
        current_player %= len(list_players)
    return max(list_players)

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

print('Should be 32')
print('Answer is {ans}'.format(ans=play_game(sample_1)))
print('Should be 8317')
print('Answer is {ans}'.format(ans=play_game(sample_2)))
print('Should be 146373')
print('Answer is {ans}'.format(ans=play_game(sample_3)))
print('Should be 2764')
print('Answer is {ans}'.format(ans=play_game(sample_4)))
print('Should be 54718')
print('Answer is {ans}'.format(ans=play_game(sample_5)))
print('Should be 37305')
print('Answer is {ans}'.format(ans=play_game(sample_6)))
print('If above is true, this should work')
print('Answer is {ans}'.format(ans=play_game(input)))
