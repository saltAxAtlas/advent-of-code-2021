f = open('./input.txt', 'r')

lines = f.readlines()

grid = [[0 for col in range(1000)] for row in range(1000)]

for line in lines:
    a, b = line.split(' -> ')
    x1, y1 = map(int, a.split(','))
    x2, y2 = map(int, b.split(','))
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    if x1 != x2 and y1 != y2:
        continue
    grid[x1][y1] += 1
    while x1 != x2 or y1 != y2:
        if x1 != x2:
            x1 += 1
        if y1 != y2:
            y1 += 1
        grid[x1][y1] += 1

print(sum([sum([1 for col in row if col > 1]) for row in grid]))
