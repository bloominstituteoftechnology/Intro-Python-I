a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]

print(a)

print('----------')

b = [x*2 for x in a]

print(b)

print('--------------')


c = [x*2 for x in a if x <= 5]
print(c)

print('--------------')

b = []
for x in a:
    if x <= 5:
        b.append(x * 2)
print(b)
