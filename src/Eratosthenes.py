"""
Allows user to enter 'python primerange.py [number],[number]'
Will return all prime numbers in given range.

If only one number entered will return all prime numbers
less than or equal to number enter

Sieve_of_Eratosthenes Algorithm via Wikipedia:

Input: an integer n > 1.

Let A be an array of Boolean values, indexed by integers 2 to n,
initially all set to true.

for i = 2, 3, 4, ..., not exceeding √n:
  if A[i] is true:
    for j = i^2, i^2+i, i^2+2i, i^2+3i, ..., not exceeding n:
      A[j] := false.

Output: all i such that A[i] is true.
"""

import sys
import math


def Sieve_of_Eratosthenes(min, max):
   A = [True] * (max+1)
   A[0] = A[1] = False

   for i in range(min, int(math.sqrt(max))+1):
       if A[i] is True:
           for j in range(i**2, max+1, i):
               A[j] = False

   print([i for i, x in enumerate(A) if x is True])

try:
   nums = sys.argv[1].split(',')
   print()
   if len(nums) == 2 and int(nums[0]) >= 2:
       Sieve_of_Eratosthenes(int(nums[0]), int(nums[1]))
   elif len(nums) == 2 and int(nums[0]) < 2:
       Sieve_of_Eratosthenes(2, int(nums[1]))
   else:
       Sieve_of_Eratosthenes(2, int(nums[0]))
except:
   print("\nPlease enter 'python primerange.py [number],[number]'.\
          \nNote numbers must be integers.\
          \n")