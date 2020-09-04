def foo(x):
    x[2] = 99

a = [1, 2, 3, 4]

foo(a)

print(a[2])
print(a)
