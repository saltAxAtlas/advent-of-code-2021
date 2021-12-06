f = open('./input.txt', 'r')

lines = f.readlines()
horz = 0
depth = 0
aim = 0

for line in lines:
    cmd, dist = line.split()
    if cmd == 'forward':
        horz += int(dist)
        depth += aim * int(dist)
    elif cmd == 'down':
        aim += int(dist)
    else:
        aim -= int(dist)

print(horz * depth)