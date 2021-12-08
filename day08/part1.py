f = open('./input.txt', 'r')

lengths = [2, 3, 4, 7]

lines = f.readlines()
count = 0

for line in lines:
    output_digits = line[line.index('|')+1:].split()
    count += sum([1 for x in output_digits if len(x) in lengths])

print(count)
