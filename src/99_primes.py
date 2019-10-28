import sys
import math

num = int(sys.argv[1])
for n in range(2, math.floor(math.sqrt(num)) + 1):
    if num % n == 0:
        print(f"{num} is not prime")
        break
else:
    print(f"{num} is prime")
