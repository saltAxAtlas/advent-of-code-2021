f = open('./input.txt', 'r')

lines = f.readlines()
horz = 0
depth = 0

for line in lines:
    cmd, dist = line.split()
    if cmd == 'forward':
        horz += int(dist)
    elif cmd == 'down':
        depth += int(dist)
    else:
        depth -= int(dist)

print(horz * depth)