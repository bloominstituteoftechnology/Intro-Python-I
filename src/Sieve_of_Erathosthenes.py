from bitmap import BitMap


def is_prime(n):
    bm = BitMap(n + 1)
    for i in range(2, n):
        if bm.test(i):
            continue
        for i_s in range(i, n + 1, i):
            if i_s > n:
                break
            if not bm.test(i_s):
                bm.set(i_s)
                if i_s == n:
                    return False
    return True


assert is_prime(2) == True, '2 is prime'
assert is_prime(4) == False, '4 is not prime'
assert is_prime(5) == True, '5 is prime'
assert is_prime(6) == False, '6 is not prime'
assert is_prime(7) == True, '7 is prime'
assert is_prime(21) == False, '21 is not prime'
assert is_prime(23) == True, '23 is prime'
assert is_prime(24) == False, '24 is not prime'
assert is_prime(25) == False, '25 is not prime'

