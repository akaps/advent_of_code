class InverseCaptcha:
    def __init__(self, input):
        self.digits = [0] * 10
        self.reverse_captcha(input)

    def reverse_captcha(self, input):
        length = len(input)
        for i in range(length):
            if input[i] == input[(i + 1) % length]:
                self.digits[(int)(input[i])] += 1

    def total(self):
        print(self.digits)
        sum = 0
        for i in range(len(self.digits)):
            sum += i * self.digits[i]
        return sum

file = open('day_1_input.txt')
captcha = InverseCaptcha(file.readline().strip())
file.close()
print(captcha.total())
