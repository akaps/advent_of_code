import re

file = open('input.txt')
lines = file.readlines()
file.close()

total = 0
for line in lines:
    l,w,h = map(int, re.findall('\d+', line))
    sides = (l*w, w*h, h*l)
    total += 2 * sum(sides) + min(sides)
print(total)
