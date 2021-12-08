def sortedString(string):
    return ''.join(sorted([*string]))

f = open('./input.txt', 'r')

lines = f.readlines()
total = 0

for line in lines:
    d = {}
    inputs, outputs = line.split(' | ')
    inputs  = [*map(sortedString, inputs.split())]
    outputs = [*map(sortedString, outputs.split())]
    
    for value in inputs:
        if len(value) == 2:
            d[1] = value
        elif len(value) == 3:
            d[7] = value
        elif len(value) == 4:
            d[4] = value
        elif len(value) == 7:
            d[8] = value

    for value in inputs:
        a = all(x in value for x in d[1])
        b = all(x in value for x in d[4])
        if len(value) == 6:
            if not a and not b:
                d[6] = value
            elif a and b:
                d[9] = value
            elif a and not b:
                d[0] = value
        elif len(value) == 5:
            if a:
                d[3] = value
            elif sum([1 for x in value if x in d[4]]) == 3:
                d[5] = value
            else:
                d[2] = value
    
    answer = 0
    for output in outputs:
        for key, value in d.items():
            if value == output:
                answer *= 10 
                answer += key
    total += answer

print(total)
