f = open('./input.txt', 'r')

lines = [[*map(int,[*x][:-1])] for x in f.readlines()]

total = 0

for y, line in enumerate(lines):
    for x, value in enumerate(line):
        a = b = c = d = 10
        if x > 0:
            a = line[x - 1]
        if x < len(line) - 1:
            b = line[x + 1]
        if y > 0:
            c = lines[y - 1][x]
        if y < len(lines) - 1:
            d = lines[y + 1][x]

        if all(value < z for z in [a, b, c, d]):
            total += value + 1

print(total)
