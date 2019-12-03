import sys

n = sys.argv[1]


def is_prime(n):
    if not n.isdigit():
        return "INVALID INPUT"
    if int(n) < 2:
        return "NOT PRIME"
    for m in range(2, int(n)//2 + 1):
        if ((int(n)/m) == (int(n)//m)):
            return "NOT PRIME"
    return "PRIME"


print(is_prime(n))
