#!/usr/bin/env python3

import sys

def sieve_of_eratosthenes(limit):
    candidates = set([*range(2, limit+1)])
    for x in range(2, (limit+1)):
        if (x not in candidates):
            continue
        composite = x + x
        while composite < limit + 1:
            candidates.discard(composite)
            composite += x
    return candidates

args = sys.argv[1:]

if len(args) != 1:
    print("Expected one, and only one, argument.", file=sys.stderr)
    print("Usage:", file=sys.stderr)
    print(f"  {sys.argv[0]} <integer>", file=sys.stderr)
    print("Returns 0 if the number is prime, 1 if it is not", file=sys.stderr)
    exit(64)

number = int(args[0])

if number <= 0:
    print("Number must be greater than 0 !", file=sys.stderr)
    exit(64)

primes_up_to_number = sieve_of_eratosthenes(number)

is_prime = number in primes_up_to_number
print(str(is_prime))

if !is_prime:
    exit(1)
