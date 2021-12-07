f = open('./input.txt', 'r')

lines = [int(x) for x in f.readlines()]

count = 0
for i in range(3, len(lines)):
    if lines[i - 3] < lines[i]:
        count += 1

print(count)
