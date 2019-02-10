import re

file = open('input.txt')
lines = file.readlines()
file.close()

total_paper = 0
total_ribbon = 0
for line in lines:
    dims = list(map(int, re.findall('\d+', line)))
    dims.sort()
    sides = (dims[0] * dims[1], dims[1] * dims[2], dims[2] * dims[0])
    total_paper += 2 * sum(sides) + min(sides)
    #2*smallest+2*not largest+lwh
    total_ribbon += 2 * (dims[0] + dims[1]) + (dims[0] * dims[1] * dims[2])
print('total paper needed = {ans}'.format(ans=total_paper))
print('total ribbon needed = {ans}'.format(ans=total_ribbon))
