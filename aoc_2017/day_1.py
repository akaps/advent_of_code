class InverseCaptcha:
    def __init__(self, input):
        self.digits = [0] * 10
        self.half_digits = [0] * 10
        self.reverse_captcha(input)
        self.reverse_half(input)

    def reverse_captcha(self, input):
        length = len(input)
        for i in range(length):
            if input[i] == input[(i + 1) % length]:
                self.digits[(int)(input[i])] += 1

    def reverse_half(self, input):
        length = len(input)
        half = length // 2
        for i in range(length):
            if input[i] == input[(i + half) % length]:
                self.half_digits[(int)(input[i])] += 1

def total(digits):
    print(digits)
    sum = 0
    for i in range(len(digits)):
        sum += i * digits[i]
    return sum

file = open('day_1_input.txt')
captcha = InverseCaptcha(file.readline().strip())
file.close()
print(total(captcha.digits))
print(total(captcha.half_digits))
