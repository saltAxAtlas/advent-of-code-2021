f = open('./input.txt', 'r')

lines = f.readlines()
dots = []
folds = []
mx = my = 0

d = True
for line in lines:
    if line == '\n':
        d = False
        continue
    if d:
        x, y = map(int, line.split(','))
        mx = max(mx, x)
        my = max(my, y)
        dots.append([x, y])
    else:
        folds.append(line.split()[-1].split('='))

grid = [[' ' for _ in range(mx + 1)] for _ in range(my + 1)]

for dot in dots:
    grid[dot[1]][dot[0]] = '#'

for fold in folds:
    direction = fold[0]
    axis = int(fold[1])

    if direction == 'x':
        for y in range(my + 1):
            for x in range(axis + 1, mx + 1):
                if grid[y][x] == '#':
                    grid[y][axis - (x - axis)] = '#'
        mx = axis
    else:
        for y in range(axis + 1, my + 1):
            for x in range(mx + 1):
                if grid[y][x] == '#':
                    grid[axis - (y - axis)][x] = '#'
        my = axis

for y in range(my + 1):
    print(''.join(grid[y][:mx + 1]))
