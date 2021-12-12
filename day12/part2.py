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
    st.append([False, ['start', x]])

while st:
    curr = st.pop(0)
    for x in conns[curr[1][-1]]:
        if x.islower():
            if x == 'end':
                paths += 1
            elif x == 'start':
                continue
            else:
                if x not in curr[1]:
                    st.append([curr[0], curr[1] + [x]])
                else:
                    if curr[0] == False:
                        st.append([True, curr[1] + [x]])
        else:
            st.append([curr[0], curr[1] + [x]])

print(paths)
