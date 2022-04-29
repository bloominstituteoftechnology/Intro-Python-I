# Write a program to determine if a number, given on the command line, is prime.
# Stretch Goals
from math import sqrt
from itertools import count, islice

n = int(input("Enter a number: ")) 
if (n > 1):
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            print(n, "is not a prime number")
