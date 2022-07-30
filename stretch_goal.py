# python3 stretch_goal.py

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
    elif number > 1:
        if number == 2:
            return (f"{number} IS a prime number.")
        else:
            for i in range(2, number):
                current = i
                while current < number:
                    if (number % current) != 0:
                        current = current + 1
                        if current == number and (number % current) == 0:
                          return (f"{number} IS a prime number.")
                    else:
                        return (f"{number} is NOT a prime number.")

print(prime_num(num))
