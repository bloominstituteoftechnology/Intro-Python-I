'''
Sieve for Primes:
Function that uses infamous Sieve of Erasthothenes algorithm to
determine prime numbers.
'''
import time
def sieve(n):
    start_time = time.time()
    is_prime = [True]*(n-1) # begin list with all integers being prime
    p=2 # begin at 2

    while True:
        multiplier = 2
        multiple = p*multiplier # 2p, 3p, 4p these are our sieves

        while multiple<=n: # stop at list


            is_prime[multiple -2] = False
            multiplier += 1
            multiple = p*multiplier

        for i, prime in enumerate(is_prime): #indexes and creates list
            if prime and i+2 > p:
                p = i + 2
                break # keep going

        else:
            break # end of list

    end_time = time.time()
    for i, prime in enumerate(is_prime):
        if prime: print(i+2)

    print("Total time: {:.5f} seconds".format(end_time - start_time))

sieve(100)
