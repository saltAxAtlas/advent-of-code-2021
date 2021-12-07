f = open('./input.txt', 'r')

crabs = [*map(int, f.readline().split(','))]

min_horz = min(crabs)
max_horz = max(crabs)
min_fuel = 999999999999

for i in range(min_horz, max_horz + 1):
    min_fuel = min(sum([abs(i - x) for x in crabs]), min_fuel)

print(min_fuel)
