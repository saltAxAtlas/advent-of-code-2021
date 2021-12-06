f = open('./input.txt', 'r')

fish = [*map(int, f.readline().split(','))]
days = 80

while days:
    new_fish = 0
    for i in range(len(fish)):
        new_fish += 1*(fish[i] == 0)
        fish[i] = 6 if fish[i] == 0 else fish[i] - 1
    while new_fish:
        fish.append(8)
        new_fish -= 1
    days -= 1

print(len(fish))
