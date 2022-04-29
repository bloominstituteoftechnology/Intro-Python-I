import numpy as np

def is_prime(n):
    if n < 2:
        return(False)
    
    sieve = np.ones((n // 2) - 1, dtype=bool)
    for i in range ((n // 2) - 1):
        if sieve[i] == True:
            if n % (i + 2) == 0:
                return False
            for j in range(i + 2, (n // 2) // (i + 2)):
                sieve[(i + 2)*j - 2] = False
    return True

if __name__ == '__main__':
    n = int(input('Enter the number whose primality you wish to test: '))
    print(is_prime(n))
