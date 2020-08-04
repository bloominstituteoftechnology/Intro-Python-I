'''
Write a program to determine if a number, given on the command line, is prime.
(In math, prime numbers are whole numbers greater than 1, 
 that have only two factors – 1 and the number itself.
 Prime numbers are divisible only by the number 1 or itself.)

- How can you optimize this program?

- Implement The Sieve of Eratosthenes,
  one of the oldest algorithms known (ca. 200 BC).

'''

num = int(input())

def prime_num(number):
    if number <= 1:
        return (f"{number} is NOT a prime number.")
        # return False
    elif number > 1:
        if number == 2:
            return (f"{number} IS a prime number.")
            # return True
        else:
            for i in range(2, (number)):
                if number % i == 0:
                    return(f"{number} is NOT a prime number.")
                    # return False
                else:
                    return (f"{number} IS a prime number.")
                    # return True

print(prime_num(num))
