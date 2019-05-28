from bitmap import BitMap


def is_prime(n):
    bm = BitMap(n)
    for i in range(2, n):
        for i_s in range(i, n, i):
            if i_s > n - 1:
                break
            bm.set(i_s)
            print(f'i: {i} i_s: {i_s}')
        if bm.count() >= n - (1 if n % 2 == 0 else 2):
            return True
        print(f"count: {bm.count()}")
    return False



assert is_prime(4) == False, '4 is not prime'
assert is_prime(5) == True, '5 is prime'
assert is_prime(6) == False, '6 is not prime'
assert is_prime(7) == True, '7 is prime'
assert is_prime(23) == True, '23 is prime'
assert is_prime(24) == False, '24 is not prime'
