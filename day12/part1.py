f = open('./input.txt', 'r')

lines = f.readlines()
conns = {}

for line in lines:
    a, b = line[:-1].split('-')
    if a not in conns:
        conns[a] = []
    if b not in conns:
        conns[b] = []
    conns[a].append(b)
    conns[b].append(a)

st = []
paths = 0

for x in conns['start']:
    st.append(['start', x])

while st:
    curr = st.pop(0)
    for x in conns[curr[-1]]:
        if x == 'end':
            paths += 1
        elif x.islower():
            if x not in curr:
                st.append(curr + [x])
        else:
            st.append(curr + [x])

print(paths)
