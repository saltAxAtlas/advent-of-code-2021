from collections import Counter

f = open('./input.txt', 'r')

rules = {}
string = f.readline()[:-1]
f.readline()
line = f.readline()
while line:
    a, b = line.split(' -> ')
    rules[a] = b[:-1]
    line = f.readline()

steps = 10
while steps:
    steps -= 1
    nString = ''
    for i in range(1, len(string)):
        nString += string[i - 1] + rules[string[i - 1:i + 1]]
    nString += string[-1]
    string = nString

c = Counter(string)
maxx = max(c.values())
minn = min(c.values())

print(maxx - minn)
