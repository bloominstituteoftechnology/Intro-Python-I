def bill(a, b, *args, **kwargs):
    print('hello word')
    print('a==>', a)
    print('b==>', b)
    print('args==>', args)
    print('args==>', kwargs)


zoo = {
    's': 's',
    'z': 9
}
arr = [1, 3, 4, 5, 6, 6, ]
# bill(2, 4, 5, 6, 6, 7, arr, *zoo, goat='foof')
# bill(2, 4, 5, 6, 6, 7, *arr, **zoo, goat='foof')
# bill(2, 4, 5, 6, 6, 7, arr, *zoo, goat='foof')
bill(2, 4, 5, 6, 6, 7, arr, zoo, goat='foof')
