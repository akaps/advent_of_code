def reverse_captcha(input, distance):
    digits = [0] * 10
    length = len(input)
    for i in range(length):
        if input[i] == input[(i + distance) % length]:
            digits[(int)(input[i])] += 1
    return digits

def total(digits):
    sum = 0
    for i in range(len(digits)):
        sum += i * digits[i]
    return sum

def solve(input, distance):
    digits = reverse_captcha(input, distance)
    tot = total(digits)
    print('Total for distance {dist} is {total}'.format(dist=distance, total=tot))

file = open('input.txt')
input = file.readline().strip()
file.close()

solve(input, 1)
solve(input, len(input) // 2)
