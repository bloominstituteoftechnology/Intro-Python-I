modulo_operator = [i for i in range(1, 11) if i % 2 ==0] 
print(modulo_operator)


squares = [i**2 for i in range(1, 11)]
print(squares)

names = ['Sarah', 'jorge', 'sam', 'frank', 'bob', 'sandy', 'shawn']
s_names = []
for i in names:
    if i[0].lower() == 's':
        s_names.append(i.capitalize())

print(s_names)

# list_comprehension

s_names = [i.capitalize() for i in names if i[0].lower() == 's']
print(s_names)


letters = 'abcdefghijklmnopqrstuvwxyz'

alpha = {letter: i + 1 for i, letter in enumerate(letters)}

print(alpha)

c = [0, 1, 0, 0, 0, 1, 0]

def jumpingOnClouds(c):
    # start with cloud 0
    # we can jump 1 or 2 clouds at once
    current = 0
    jumps = 0

    # keep iterating until we've won the game
    # stop when 'current' == the index of the last cloud

    while current < len(c):
        # check the cloud 2 spots away to see if we can jump there
        if current + 2 < len(c) and c[current + 2] == 0:
            current += 2
        else:
            current += 1

        jumps += 1

    return jumps

print(jumpingOnClouds(c))
