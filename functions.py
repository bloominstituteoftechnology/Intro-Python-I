# Define a doubling function that passes args by value
x = 1

def mult2(x):
    return x * 2

print(mult2(x))


# Define a doubling function that passes aegs by reference
l = [1, 2, 3, 4]


def mult2_list(l):

    for i in range(len(l)):
        l[i] *= 2
    return l

print(mult2_list(l))
print(mult2_list([10, 9, 3, 15]))


# Try out our functions

y = mult2(12)
print(y)

l = [3, 7, 13]
print(mult2_list(l))

for i in l:
    print(i)