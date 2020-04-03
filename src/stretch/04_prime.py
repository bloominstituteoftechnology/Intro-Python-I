"""determine if a number, given on the command line, is prime"""

import sys
print('Given number: ', sys.argv[1])
num = float(sys.argv[1])
is_prime = True
if num < 2:
    print(f'{str(num)} is not prime because it is less than 2')
    is_prime = False
elif num > int(num):
    print(f'{str(num)} is not prime because it is not an integer')
    is_prime = False
num_int = int(num)
for i in range(2, num_int//2):
    if (num_int % i == 0):
        print(f'{str(num)} is not prime because it is divisible by {str(i)}.')
        is_prime = False
        break

if is_prime:
    print(f'{str(num_int)} is prime!')
