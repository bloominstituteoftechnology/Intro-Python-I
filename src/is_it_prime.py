import math
def is_prime(n):
    if(n == 2):
        return True
    if(n < 2 or n % 2 == 0):
        return False
    start = 3
    end = int(math.sqrt(n))
    for num in range(start, end + 1):
        if num % 2 != 0:
            if n%num == 0:
                return False
    
    return True

print(is_prime(34))
print(is_prime(14))
print(is_prime(67))
print(is_prime(13))
print(is_prime(19))
print(is_prime(347))
