# Write a program to determine if a number, given on the command line, is prime.
# Pr1me number --- natural number( 1,2,3)
#              --- divisible by exactly 2 natural numbers: --- itself
#                                                          --- 1


num = int(input("Enter a natural number: "))

for i in range(2, num):
    if num % i == 0:
        print('Not a prime number')
        break
else:
    print('Prime number')


print('\n----------- Using  The Sieve of Eratosthenes --------')

def the_sieve_of_eratosthenes(n): # n is the value of up to whitch number I want to get the prime numbers
    print(f'All prime numbers from 1 to {n}')

    is_prime = [True]*(n-1)
    p = 2

    while True:
        multiplier = 2
        multiple = p * multiplier

        while multiple <= n:
            is_prime[multiple-2] = False
            multiplier += 1
            multiple = p * multiplier  # (2p, 3p, 4p, 5p .....)

        for i, prime in enumerate(is_prime): # i is index
            if prime and i+2 > p:
                p = i+2
                break
        else:
            break

    for i, prime in enumerate(is_prime): # i is index
        if prime:
            print(i+2)

the_sieve_of_eratosthenes(100)
