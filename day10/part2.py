f = open('./input.txt', 'r')

points = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}
pairs  = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}

lines = [x[:-1] for x in f.readlines()]
scores = []

for line in lines:
    st = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            st.append(c)
        else:
            x = st.pop(-1)
            if pairs[x] != c:
                break
    else:
        score = 0
        while st:
            x = st.pop(-1)
            score *= 5
            score += points[x]
        scores.append(score)

print(sorted(scores)[len(scores) // 2])
