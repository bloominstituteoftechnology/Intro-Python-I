# Stretch goal
# Write a program to determine if a number, given on the command line, is prime.
# How can you optimize this program?
# Implement The Sieve of Eratosthenes, one of the oldest algorithms known (ca. 200 BC).

import numpy as np 
 
def sieve(n):
    if n < 2:
        return False
    
    sieve = np.ones((n // 2) - 1, dtype=bool)
    for i in range ((n // 2) - 1):
        if sieve[i] == True:
            if n % (i + 2) == 0:
                return False
            for x in range(i + 2, (n // 2) // (i + 2)):
                sieve[(i + 2)*x - 2] = False
    return True

if __name__ == '__main__':
    n = int(input('Input a number to test its primality: '))
    print(sieve(n))