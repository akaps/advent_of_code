def detect_run(input, run_length):
    run_length -= 1
    run = list(input[:run_length])
    for i in range(run_length, len(input)):
        last = input[i]
        if last not in run and len(set(run)) == run_length:
            return i + 1
        else:
            run.append(input[i])
            run.pop(0)
    return -1

def detect_packet(input):
    return detect_run(input, 4)

def detect_message(input):
    return detect_run(input, 14)

def main():
    assert detect_packet('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
    assert detect_packet('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert detect_packet('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert detect_packet('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert detect_packet('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

    file_input = open('input.txt')
    signal = file_input.readline().strip()
    file_input.close()
    print('Part 1: ', detect_packet(signal))

    assert detect_message('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
    assert detect_message('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
    assert detect_message('nppdvjthqldpwncqszvftbrmjlhg') == 23
    assert detect_message('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
    assert detect_message('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26

    print('Part 2: ', detect_message(signal))

if __name__ == '__main__':
    main()
