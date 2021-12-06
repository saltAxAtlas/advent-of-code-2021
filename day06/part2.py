f = open('./input.txt', 'r')

fishes = [*map(int, f.readline().split(','))]
days = 256

d = {x:0 for x in range(days)}

for fish in fishes:
    while fish < days:
        d[fish] += 1
        fish += 7

for day in range(days):
    number_fish = d[day]
    day += 9
    while day < days:
        d[day] += number_fish
        day += 7

print(sum(d.values()) + len(fishes))