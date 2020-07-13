import sys

n_input = int(sys.argv[1])


def check_prime(n):
    prime_denominators = [2, 3, 5, 7]
    if n_input in prime_denominators:
        print(str(n) + ' is prime')
        return

    for prime_n in prime_denominators:
        if n_input % prime_n == 0:
            print(str(n) + ' not prime')
            return
    print(str(n) + ' is prime')

check_prime(n_input)