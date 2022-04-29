# from sys import argv
# from math import sqrt

# args = argv
# arg_count = len(args)

# if arg_count != 2:
#     raise ValueError('Please provide exactly one integer argument.')

# num_to_check = int(args[1])

def sieve(sieve_up_to):
    print(f"Find all primes up to, and possibly including, {sieve_up_to}.")

    caught = {1}

    unfiltered = {f for f in range(2, sieve_up_to + 1)}
    while (unfiltered != {}):
        next_prime = min(unfiltered)
        unfiltered.discard(next_prime)
        caught.add(next_prime)

        for multiplier in range(2, int(sieve_up_to / next_prime) + 1):
            unfiltered.discard(next_prime * multiplier)
