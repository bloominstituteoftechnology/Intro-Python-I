"""
Allows user to enter 'python prime.py [number]'
Will return whether or not prime number entered.
"""

import sys

try:
   num = int(sys.argv[1])
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               print(num, "is not a prime number.")
               break
       else:
           print(num, "is a prime number!")
   else:
       print(num, "is not a prime number.")
except:
   print("\nPlease enter 'python prime.py [number]'.\
          \nNote number must be an integer.\
          \n")