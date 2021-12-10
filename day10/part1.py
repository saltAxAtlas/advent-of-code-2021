f = open('./input.txt', 'r')

points = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
pairs  = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}

lines = [x[:-1] for x in f.readlines()]
total = 0

for line in lines:
    st = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            st.append(c)
        else:
            x = st.pop(-1)
            if pairs[x] != c:
                total += points[c]
                break

print(total)