"""
The Sieve of Eratosthenes is an algorithm for finding all prime numbers up to
any given limit.

Input: n, an integer > 1
Output: A, an array of all prime numbers from 2 through n.
"""
import sys


def sieve_of_eratosthenes(n):
    # Create a list of consecutive integers from 0 to n
    A = [True for i in range(n+1)]
    # Initially, let i = 2, the smallest prime number
    i = 2

    while i * i <= n:
        if A[i]:
            # Enumerate the multiples of each prime i from i^2
            for j in range(i * i, n+1, i):
                A[j] = False  # they are not prime
        i += 1

    # Print i if still prime
    for i in range(2, n+1):
        if A[i]:
            print(i)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(
        'The following integers are the prime numbers less than or equal to',
        n,
        ':'
    )
    sieve_of_eratosthenes(n)
