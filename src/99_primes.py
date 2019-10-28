import math

num = int(input("Is it prime? "))
factors = [*range(2, math.floor(math.sqrt(num)) + 1)]
for n in factors:
    if num % n == 0:
        print(f"{num} is not prime")
        break
    else:
        factors[:] = [x for x in factors if x % n != 0]
else:
    print(f"{num} is prime")
