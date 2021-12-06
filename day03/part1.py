f = open('./input.txt', 'r')

lines = [list(x)[:-1] for x in f.readlines()]
gamma = ''
epsilon = ''

for col in zip(*lines):
    if sum([1 if x == '1' else -1 for x in col]) > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))