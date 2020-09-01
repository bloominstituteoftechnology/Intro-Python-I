import math

def isprime(num):
    """dumb way to check if an integer is prime
    divide by nums thru sqrt(num) and check remainder
    """
    limit = int(math.sqrt(num))   # use a while loop til index**2 instead
    if num < 2 :
        return False

    for n in range(5,limit):     # python 3 range is lazy
        if num % n == 0:       # O(n) without sqrt
            return False
    return True

assert isprime(2) == True
assert isprime(3) == True
assert isprime(4) == False
assert isprime(5) == True

num = input("Enter an integer : ")
num = int(num)

print(isprime(num))

