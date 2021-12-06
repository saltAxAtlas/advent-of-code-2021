f = open('./input.txt', 'r')

lines = [int(x) for x in f.readlines()]

a = sum(lines[0:3])
count = 0

for i in range(1, len(lines)-2):
    b = sum(lines[i:i+3])
    if a < b:
        count += 1
    a = b

print(count)

# a, b, c, d = lines[:4]
# sum1 = a + b + c
# sum2 = b + c
# for d in lines[4:]:
#     sum2 += d
#     if sum1 < sum2:
#         count += 1
#     sum1 -= a
#     sum1 += d
#     sum2 -= b
#     a, b, c = b, c, d
# print(count)
