def is_prime(n):
    """Returns True if number is prime."""
    if n is not abs(int(n)):
        return False                            #test n a positive number.
    if n < 2:                                    #0 and 1 are not primes
        return False
    if n == 2:                                  #2 is the only even prime
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n/2) + 1, 2):
        if n % i == 0:
            print (n, i, (n % i))
            return False

    return True


primes = [4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993]
non_primes = [4, 459, 98, 999999, 8, 0]

print("some primes:")
for i in primes:
    print(i, "\t", is_prime(i))

print("\nsome non-primes:")
for i in non_primes:
    print(i, "\t", is_prime(i))
