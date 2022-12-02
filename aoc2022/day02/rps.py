OPP_ROCK = 'A'
OPP_PAPER = 'B'
OPP_SCISSORS = 'C'

ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

EXP_WIN = 'Z'
EXP_TIE = 'Y'
EXP_LOSE = 'X'

WIN = 6
TIE = 3
LOSE = 0

rigged_plays = {OPP_ROCK: {EXP_WIN: PAPER, EXP_TIE: ROCK, EXP_LOSE: SCISSORS},
                OPP_PAPER: {EXP_WIN: SCISSORS, EXP_TIE: PAPER, EXP_LOSE: ROCK},
                OPP_SCISSORS: {EXP_WIN: ROCK, EXP_TIE: SCISSORS, EXP_LOSE: PAPER}}
score_dict = {OPP_ROCK: {ROCK: TIE, PAPER: WIN, SCISSORS: LOSE},
                OPP_PAPER: {ROCK: LOSE, PAPER: TIE, SCISSORS: WIN},
                OPP_SCISSORS: {ROCK: WIN, PAPER: LOSE, SCISSORS: TIE}}
play_values = {ROCK: 1, PAPER: 2, SCISSORS: 3}

def score(opponent, response):
    return play_values[response] + score_dict[opponent][response]

def rigged_score(opponent, expected_result):
    move = rigged_plays[opponent][expected_result]
    return score(opponent, move)

def main():
    file_input = open('input.txt', 'r')
    lines = file_input.readlines()
    file_input.close()
    score_total = 0
    for line in lines:
        opponent, response = line.strip().split()
        score_total += score(opponent, response)
    print('part 1:', score_total)

    rigged_total = 0
    for line in lines:
        opponent, result = line.strip().split()
        rigged_total += rigged_score(opponent, result)
    print('part 2: ', rigged_total)

if __name__ == '__main__':
    assert score('A', 'Y') == 8
    assert score('B', 'X') == 1
    assert score('C', 'Z') == 6

    assert rigged_score('A', 'Y') == 4
    assert rigged_score('B', 'X') == 1
    assert rigged_score('C', 'Z') == 7
    main()
