f = open('./input.txt', 'r')

lines = [int(x) for x in f.readlines()]

prev = lines[0]
count = 0

for line in lines[1:]:
    if prev < line:
        count += 1
    prev = line

print(count)