f = open('./input.txt', 'r')

rules = {}
string = f.readline()[:-1]
f.readline()
line = f.readline()
while line:
    a, b = line.split(' -> ')
    rules[a] = b[:-1]
    line = f.readline()

pairs = {}
for i in range(len(string) - 1):
    if string[i:i+2] not in pairs:
        pairs[string[i:i+2]] = 0
    pairs[string[i:i+2]] += 1

steps = 40
while steps:
    steps -= 1
    nPairs = {}
    for key, value in pairs.items():
        m = rules[key]
        left  = key[0] + m
        right = m + key[1]
        if left not in nPairs:
            nPairs[left] = 0
        if right not in nPairs:
            nPairs[right] = 0
        nPairs[left] += value
        nPairs[right] += value
    pairs = nPairs
    
z = {}
for key, value in pairs.items():
    if key[0] not in z:
        z[key[0]] = 0
    if key[1] not in z:
        z[key[1]] = 0
    z[key[0]] += value
    z[key[1]] += value

z[string[0]] += 1
z[string[-1]] += 1

maxx = max(z.values())
minn = min(z.values())

print((maxx - minn) // 2)