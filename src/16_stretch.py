#Write a program to determine if a number, given on the command line, is prime.
num = int(input("Enter a number greater than 1:  "))

# If given number is greater than 1
if num > 1:

   # Iterate from 2 to n / 2
   for i in range(2, num):

       # If num is divisible by any number between
       # 2 and n / 2, it is not prime
       if (num % i) == 0:
           print(num, "is not a prime number")
           break
   else:
       print(num, "is a prime number")

else:
   print(num, "is not a prime number")