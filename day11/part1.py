f = open('./input.txt', 'r')

lines = [[*map(int, x[:-1])] for x in f.readlines()]
octos = [[[x, False] for x in row] for row in lines]
flashes = 0
steps = 100

while steps:
    steps -= 1
    octos = [[[x[0] + 1, False] for x in row] for row in octos]
    done = True
    while done:
        done = False
        for y, row in enumerate(octos):
            for x, col in enumerate(row):
                if col[0] > 9 and col[1] == False:
                    done = True
                    octos[y][x] = [col[0], True]
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            ny = y + dy
                            nx = x + dx
                            if ny >= 0 and ny < len(octos) and nx >= 0 and nx < len(octos[0]):
                                octos[ny][nx] = [octos[ny][nx][0] + 1, octos[ny][nx][1]]
    for y, row in enumerate(octos):
        for x, col in enumerate(row):
            if col[1] == True:
                flashes += 1
                octos[y][x] = [0, False]

print(flashes)