# Stretch Goal
# Write a program to determine if a number, given on the command line, is prime.

import math

# taking into account the user input
number = int(input("Enter any number: "))

# prime number is always > 1
if number > 1:
    for num in range(2, number):
        if (number % num) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if number =< 1 
# it is not a prime number 

else:
    print(number, "is not a prime number")