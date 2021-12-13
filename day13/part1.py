f = open('./input.txt', 'r')

dots = []
fold = ''
mx = my = 0

while 1:
    line = f.readline()
    if line == '\n':
        break
    x, y = map(int, line.split(','))
    mx = max(mx, x)
    my = max(my, y)
    dots.append([x, y])
    
fold = f.readline().split()[-1].split('=')

grid = [['.' for _ in range(mx + 1)] for _ in range(my + 1)]

for dot in dots:
    grid[dot[1]][dot[0]] = '#'

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

count = 0
for y in range(my + 1):
    for x in range(mx + 1):
        if grid[y][x] == '#':
            count += 1

print(count)
