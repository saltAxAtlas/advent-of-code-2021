f = open('./input.txt', 'r')

lines = [[*map(int,[*x][:-1])] for x in f.readlines()]
lows = []

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
            lows.append((x, y))
            
sizes = []
for low in lows:
    st = [low]
    visited = set()
    visited.add(low)
    size = 1
    while st:
        x, y = st.pop(0)
        a = b = c = d = 9
        if x > 0:
            a = lines[y][x - 1]
        if x < len(line) - 1:
            b = lines[y][x + 1]
        if y > 0:
            c = lines[y - 1][x]
        if y < len(lines) - 1:
            d = lines[y + 1][x]
        if a < 9:
            if (x - 1, y) not in visited:
                st.append((x - 1, y))
                visited.add((x - 1, y))
                size += 1
        if b < 9:
            if (x + 1, y) not in visited:
                st.append((x + 1, y))
                visited.add((x + 1, y))
                size += 1
        if c < 9:
            if (x, y - 1) not in visited:
                st.append((x, y - 1))
                visited.add((x, y - 1))
                size += 1
        if d < 9:
            if (x, y + 1) not in visited:
                st.append((x, y + 1))
                visited.add((x, y + 1))
                size += 1
    sizes.append(size)

x, y, z = sorted(sizes)[-3:]
print(x * y * z)
