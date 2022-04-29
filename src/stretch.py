#sieve of Eratosthenes
def soe(n):
    # This is a boolean array and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    # This boolean array will initialize all entries as true
    is_prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime 
        if(is_prime[p] == True):
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0] = False
    is_prime[1] = False
 # Print all prime numbers 
    for p in range(n + 1):
        if is_prime[p]:
            print(p)

print(soe(120))

