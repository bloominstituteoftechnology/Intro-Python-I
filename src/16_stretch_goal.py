# Write a program to determine if a number, given on the command line, is prime.
# Pr1me number --- natural number( 1,2,3)
#              --- divisible by exactly 2 natural numbers: --- itself
#                                                          --- 1


# num = int(input("Enter a natural number: "))

# for i in range(2, num):
#     if num % i == 0:
#         print('Not a prime number')
#         break
# else:
#     print('Prime number')


print('-------Version that is more time efficient ---------')
import math

def is_prime(n):
    if n == 1:
        return False
    
    # if the number is even and not equal to 2 then it is not a prime number
    if n == 2:
        return True
    if n>2 and n%2==0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2): # the range starts at 3, ends at 1+ max_divisor and increments by 2 (ex (4, 10, 2)----> 4,6,8)
         if n % d == 0:
             return False
    return True

for n in range(1, 21):
    print(n, is_prime(n))


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
