f = open('./input.txt', 'r')

lines = [list(x)[:-1] for x in f.readlines()]
oxy_lines = lines
co2_lines = lines
oxygen = 0
co2 = 0

oxy_index = 0
while len(oxy_lines) > 1:
    z = sum([1 if x[oxy_index] == '1' else -1 for x in oxy_lines])
    if z >= 0:
        oxy_lines = [x for x in oxy_lines if x[oxy_index] == '1']
    else:
        oxy_lines = [x for x in oxy_lines if x[oxy_index] == '0']
    oxy_index += 1

c02_index = 0
while len(co2_lines) > 1:
    z = sum([1 if x[c02_index] == '1' else -1 for x in co2_lines])
    if z < 0:
        co2_lines = [x for x in co2_lines if x[c02_index] == '1']
    else:
        co2_lines = [x for x in co2_lines if x[c02_index] == '0']
    c02_index += 1

print(int(''.join(oxy_lines[0]), 2) * int(''.join(co2_lines[0]), 2))