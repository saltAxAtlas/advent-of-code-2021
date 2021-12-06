f = open('./input.txt', 'r')

lines = [int(x) for x in f.readlines()]

last = lines[0]
count = 0

for line in lines[1:]:
    if line > last:
        count += 1
    last = line

print(count)