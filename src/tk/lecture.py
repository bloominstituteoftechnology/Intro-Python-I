def my_func(a):
    '''
    Lists are passed by reference.
    Lists are mutable, so can be changed.
    '''
    print(f'1: {a}')
    a[0] = 99
    print(f'2: {a}')


a = [0, 1, 2, 3]
my_func(a)
print(a)

c = [1, 2, 3]
d = c
del c[:]
print(c)
print(d)
