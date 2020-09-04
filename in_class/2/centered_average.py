import math


def centered_average(a):
    print(a)
    a.sort()
    print(a)

    middle = a[1:-1]
    print(middle)

    total = 0
    for v in middle:
        total += v

    return total // len(middle)

print(centered_average([1, 1, 5, 5, 10, 8, 7]))


def centered_average_2(a):
    a.remove(max(a))
    a.remove(min(a))

    total = 0
    for v in a:
        total += v

    return total // len(a)

print(centered_average_2([1, 1, 5, 5, 10, 8, 7]))



def centered_average_3(a):
    mn = min(a)
    mx = max(a)

    total = 0
    for v in a:
        total += v

    total -= mn
    total -= mx

    return total // (len(a) - 2)

print(centered_average_3([1, 1, 5, 5, 10, 8, 7]))


def centered_average_4(a):
    total = 0
    mx = -math.inf
    mn = math.inf


    for v in a:
        if v < mn:
            mn = v

        if v > mx:
            mx = v

        total += v

    total -= mn
    total -= mx

    return total // (len(a) - 2)

print(centered_average_4([1, 1, 5, 5, 10, 8, 7]))
